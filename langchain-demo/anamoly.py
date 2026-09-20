# reading the file
with open("application.log","r") as file:
    logs = file.readlines()
    # file.seek(0)
    # for i in file:
    #     print(i.strip())
    c=0
    for i in logs:
        logger = i.split()
        print('Date: ',logger[0])
        print('Time: ',logger[1])
        print('Log Level: ',logger[2])
        print('Message: ',logger[3]+" "+logger[4]+" "+logger[5])
        if(logger[2]=='ERROR'):
            c+=1
print("Total Errors: ",c)
#print(logs)

#now we are going to parse
# using the counter function to calculate the no. of errors in a particular time frame
from collections import Counter

error_by_minute = Counter()  #making the object
for log in logs:
    parts= log.split()
    if("ERROR" in log):
        minute = parts[1][:5]
        error_by_minute[minute]+=1
    if("INFO" in log):
        minute = parts[1][:5]
        error_by_minute[minute]+=1
print(error_by_minute)


# performing the rule based detection 

threshold = 3  #defining a threshold
print(error_by_minute.items())
for minute,count in error_by_minute.items():
    if(count>threshold):
        print("ANAMOLY",minute,"had",count,"errors")

l =list(range(0,11))
l=[x*x for x in l]
print(l)

#using isolation forest for anamoly detection
from sklearn.ensemble import IsolationForest

# Each number is its own row (sample)
l = [[5], [20], [12], [10], [13], [14], [100]]

model = IsolationForest(contamination=0.1, random_state=42)
predictions = model.fit_predict(l)

print(predictions)

import matplotlib.pyplot as plt
import numpy as np

# FIX 1: Convert the list to a NumPy array before calling flatten()
#x_values = np.array(l).flatten()
x_values = np.array([item for sublist in l for item in sublist])
y_values = np.zeros_like(x_values)  # Keep everything on a single horizontal baseline

# FIX 2: Correct the misplaced quote index filter from "-1]" to -1
inliers = x_values[predictions == 1]
outliers = x_values[predictions == -1]

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(inliers, np.zeros_like(inliers), color='blue', s=100, label='Normal (Inliers)')
plt.scatter(outliers, np.zeros_like(outliers), color='red', s=150, marker='X', label='Anomaly (Outliers)')

# Formatting
plt.title("Isolation Forest Anomaly Detection")
plt.xlabel("Value")
plt.yticks([])  # Hide y-axis since it's 1D data
plt.legend()
plt.show()


for i in outliers:
    print("ALERT")
