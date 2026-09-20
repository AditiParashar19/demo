'''
problem statement
Your are working as an AIOps Engineer for an online university protal  The monitoring system has recorded the following server response 
times in milliseconds over 20 time intervals.

response_time = [
120,125,118,130,122,
127,124,121,129,126,
123,128,125,122,131,
700,127,119,650,124
]
Most of the requests have a response time between aprrox 118-131 but some values apprear significantly different
Your task is to build a python-based anamoly detection system using Isolation forest
'''

import numpy as np
from sklearn.ensemble import IsolationForest
response_time = [
120,125,118,130,122,
127,124,121,129,126,
123,128,125,122,131,
700,127,119,650,124
]

l = [[x] for x in response_time]
model = IsolationForest(contamination=0.1,random_state=42)
predictions = model.fit_predict(l)
print(predictions)

print("Detected Anomalies:")
for usage, pred in zip(response_time, predictions):
    if pred == -1:
        print(f"Anomaly: {usage}")

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
colors = ['red' if p == -1 else 'orange' for p in predictions]
intervals = range(1, len(response_time) + 1)

plt.scatter(intervals, response_time, color=colors, s=100)
#plt.plot(intervals,response_time, color='gray')
plt.title('AIOps Server ')
plt.xlabel('Time Interval')
plt.ylabel('Response Time')
plt.xticks(intervals)
plt.grid(True, alpha=0.3)

plt.show()

