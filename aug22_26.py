"""
Problem Statement

You are working as an AIOps Engineer for an online university portal. 
The monitoring system has recorded the following server response times in milliseconds over 20 time intervals:
response_time = [
    120, 125, 118, 130, 122,
    127, 124, 121, 129, 126,
    123, 128, 125, 122, 131,
    700, 127, 119, 650, 124
]

Most of the requests have a response time between approximately 118-131 ms, but some values appear significantly different.

Your task is to build a Python-based anomaly detection system using Isolation Forest.

"""

from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Response Time
response_time=[
    120,125,118,130,122,
    127,124,121,129,126,
    123,125,128,122,131,
    700,127,119,650,124
]

# Convert to 2d list
X=[[val] for val in response_time]

# model
model  =IsolationForest(contamination=0.10, random_state=42)

# Fitting the model
model.fit(X)

# Predicting 
predictions=model.predict(X)

# Printing Anomaly
print("Detected Anomalies:")
for time, pred in zip(response_time, predictions):
    if pred == -1:
        print(f"Anomaly: {time} ms ")

# Scatter Plot 
plt.figure(figsize=(10, 5))
colors = ['red' if p == -1 else 'blue' for p in predictions]
intervals = range(1, len(response_time) + 1)

plt.scatter(intervals, response_time, color=colors, s=100)
plt.title('AIOps Server For Online University Portal')
plt.xlabel('Time Interval')
plt.ylabel('Response Time(ms)')
plt.xticks(intervals)
plt.grid(True, alpha=0.3)
plt.show()