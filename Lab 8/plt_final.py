import matplotlib.pyplot as plt
from pandas import *
from scipy import stats

data = read_csv('cpudata.csv')
# changed from 'rpidata1.csv' to 'cpudata.csv'

x = data['CPU Usage %']
y = data['Memory Available GB']
# changed from 'Temperature' to 'Memory Available GB'

# Time series
plt.plot(y, 'r', lw=2, label='Memory Available (GB)')
plt.plot(x, 'b', lw=2, label='CPU Usage %')
plt.xticks([209,452,703,957],['21:00','21:30','22:00','22:30'])
plt.xlabel('Time')
plt.legend(loc='lower center')
plt.title('Time Series of CPU Usage and Memory Available')

# Histogram of CPU usage
plt.figure()
num_bins = 35
n, bins, patches = plt.hist(x, num_bins, density=1, facecolor='blue', alpha=0.5)
plt.xlabel('CPU Usage %')
plt.ylabel('Probability')
plt.title('Frequency vs. CPU Usage')

# Histogram of memory available
plt.figure()
num_bins = 30
n, bins, patches = plt.hist(y, num_bins, density=1, facecolor='red', alpha=0.5)
plt.xlabel('Memory Available GB')
plt.ylabel('Probability')
plt.title('Frequency vs. Memory Available')

# Horizontal box plot of CPU usage
plt.figure()
plt.boxplot(x, 0, '+', 0)
plt.xlabel('CPU Usage %')
plt.title('CPU Usage Box Plot')

# Vertical box plot of memory
plt.figure()
plt.boxplot(y, 0, '+')
plt.ylabel('Memory Available GB')
plt.title('Memory Available Box Plot')

# Scatter diagram with a linear regression line
plt.figure()
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
plt.xlabel('CPU Usage %')
plt.ylabel('Memory Available GB')
plt.plot(x, y, 'bo')
l = [slope * i + intercept for i in x]
plt.plot(x, l, 'r', lw=2)
plt.title('Memory Available vs CPU Usage')
plt.legend()

plt.show()
