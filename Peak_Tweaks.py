import csv
from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []

with open('N2O_1st_Hit.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

# recasting the x and y data into numpy arrays
x = np.asarray(x)
y = np.asarray(y)

# finding and plotting peaks of the graph
peaks, _ = find_peaks(y, prominence=100000)
plt.plot(x, y, peaks, y[peaks], "ob")
plt.plot(y)
plt.legend(['Peaks'])
plt.xlabel("Time of Flight (ns)")
plt.ylabel("Counts")
plt.title("N20 Hit count graph")
p_list = [peaks]

# Save the data of the Peaks into FinalData file
# noinspection PyTypeChecker
np.savetxt("Data.csv", p_list, delimiter=", ", fmt='% s')

# Printing the values of Peaks
print(peaks)

plt.show()
