import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------
# 1. Create sample server log dataset
# ------------------------------------------------

data = {
    "Timestamp": [
        "10:00", "10:01", "10:02", "10:03", "10:04",
        "10:05", "10:06", "10:07", "10:08", "10:09",
        "10:10", "10:11", "10:12", "10:13", "10:14",
        "10:15", "10:16", "10:17", "10:18", "10:19"
    ],

    "CPU": [
        45, 52, 48, 55, 50,
        95, 53, 49, 51, 54,
        56, 50, 97, 52, 48,
        55, 57, 53, 92, 51
    ],

    "Memory": [
        60, 62, 61, 63, 60,
        64, 62, 61, 63, 65,
        64, 62, 66, 63, 61,
        62, 64, 63, 65, 62
    ],

    "Response_Time": [
        120, 130, 125, 135, 128,
        150, 132, 125, 130, 128,
        135, 130, 160, 132, 125,
        128, 135, 130, 155, 128
    ]
}

df = pd.DataFrame(data)

# ------------------------------------------------
# 2. Basic statistics
# ------------------------------------------------

print("========== AIOps Log Anomaly Detection ==========")

print("\nTotal records:", len(df))

print("\nBasic Statistics:")
print(df[["CPU", "Memory", "Response_Time"]].describe())

# ------------------------------------------------
# 3. Threshold-based anomaly detection
# ------------------------------------------------

# CPU threshold
CPU_THRESHOLD = 90

# Memory threshold
MEMORY_THRESHOLD = 90

# Response time threshold
RESPONSE_THRESHOLD = 200

# Detect anomaly if ANY metric crosses its threshold
df["Anomaly"] = (
    (df["CPU"] > CPU_THRESHOLD) |
    (df["Memory"] > MEMORY_THRESHOLD) |
    (df["Response_Time"] > RESPONSE_THRESHOLD)
)

# ------------------------------------------------
# 4. Print anomalous records
# ------------------------------------------------

anomalies = df[df["Anomaly"]]

print("\nAnomalies detected:", len(anomalies))

print("\nAnomalous Records:")
print(
    anomalies[
        ["Timestamp", "CPU", "Memory", "Response_Time"]
    ].to_string(index=False)
)

print("\nTimestamp    CPU       Status")

for _, row in anomalies.iterrows():
    print(
        f"{row['Timestamp']}       "
        f"{row['CPU']}%       "
        f"ANOMALY"
    )

# ------------------------------------------------
# 5. Display graph
# ------------------------------------------------

plt.figure(figsize=(12, 6))

# Normal CPU values
normal = df[~df["Anomaly"]]
anomaly = df[df["Anomaly"]]

plt.plot(
    df["Timestamp"],
    df["CPU"],
    marker="o",
    label="CPU Usage"
)

# Highlight anomalies
plt.scatter(
    anomaly["Timestamp"],
    anomaly["CPU"],
    marker="x",
    s=100,
    label="Anomaly"
)

# Threshold line
plt.axhline(
    y=CPU_THRESHOLD,
    linestyle="--",
    label="CPU Threshold"
)

plt.xlabel("Timestamp")
plt.ylabel("CPU Usage (%)")
plt.title("AIOps CPU Usage and Anomalies")

plt.xticks(rotation=45)

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.show()