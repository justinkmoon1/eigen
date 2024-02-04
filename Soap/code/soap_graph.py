import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file = "Soap/data/last_exp.csv"

data = pd.read_csv(file)

print(data)
x = data['Height']
y = data['Time']

x1 = data['Height1']
y1 = data['Time1']

x2 = data['Height2']
y2 = data['Time2']

x3 = data['Height3']
y3 = data['Time3']

x4 = data['Height4']
y4 = data['Time4']

x5 = data['Height5']
y5 = data['Time5']

x6 = data['Height6']
y6 = data['Time6']

x7 = data['Height7']
y7 = data['Time7']

fig, ax = plt.subplots()
# slope, intercept = np.polyfit(x, y, 1)
# slope1, intercept1 = np.polyfit(x1, y1, 1)
# regression_line = slope * x + intercept
# regression_line1 = slope1 * x1 + intercept1

# plt.plot(x, regression_line, color= 'red', label='9:1')
# plt.plot(x1, regression_line1, color = 'green', label = '14:1')
ax.plot(x, y, label='2:1')
ax.plot(x1, y1, label='1:1')
ax.plot(x2, y2, label= '1:2')
ax.plot(x3, y3, label= '1:4')
ax.plot(x4, y4, label='1:8')
ax.plot(x5, y5, label='1:12')
ax.plot(x6, y6, label='1:16')
ax.plot(x7, y7, label='1:20')
plt.xlabel('Height(cm)')
plt.ylabel('Time(s)')
plt.title('Soap Film Experiment')
leg = ax.legend()
ax.legend()
plt.show()