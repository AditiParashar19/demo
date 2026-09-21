# Reading the log file
with open ("application.log","r") as file:
    # log: list of string
    logs=file.readlines()

# # Parsing
# i=1
# for log in logs:
#     log=log.split()
#     print(f"-----------LOG {i}----------")
#     print("Date: ",log[0])
#     print("Time: ",log[1])
#     print("Level: ",log[2])
#     print("Information: ",log[3:])
#     i=i+1


# Error Calculation

# total_error=0
# for log in logs:
#     if "ERROR" in log:
#         total_error+=1

# print(f"Total Errors : {total_error}")

# Using the counter function
# from collections import Counter 
# count=Counter()
# for log in logs:
#     log=log.split()
#     if "ERROR" in log:
#         time=log[1][0:5]
#         count[time]+=1
# print("ERROR: ", count)

# #INFO Counter
# info=Counter()
# for log in logs:
#     log=log.split()
#     if "INFO" in log:
#         time=log[1][0:5]
#         info[time]+=1
# print("INFO: ",info)

# Using dictionary
# dict={}
# for log in logs:
#     log=log.split()
#     if "ERROR" in log:
#         time=log[1][0:5]
#         if time in dict:
#             dict[time]+=1
#         dict.add({time:1})
# print("ERROR using dict: ",dict)

# Rule based Detection
# threshold=3
# for key,val in count.items():
#     if(val>threshold):
#         print("Anomaly Detected at : ",key, "Error: ",val)

# ML-Based Detection ( Isolation Forest )
from sklearn.ensemble import IsolationForest
l=[[10],[11],[100],[12],[15]]
model=IsolationForest(contamination=0.1, random_state=42)
model.fit(l)
pred=model.predict(l)
print(pred)

# Plot
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 4))
colors = ['red' if p == -1 else 'blue' for p in pred]
x_axis = range(len(l))
y_axis = [val[0] for val in l]
plt.scatter(x_axis, y_axis, color=colors, s=100)
plt.title('Isolation Forest Detection')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()

file.close()