import numpy as np

# Finding the Mass/Charge Ratio
ToF = [65, 1115, 4092, 4372, 4506, 4636, 5773, 5976, 6167, 7227]
Slope = [1084.97918037]
Intercept = [30.82092038]

ToF = np.asarray(ToF)
Slope = np.asarray(Slope)
Intercept = np.asarray(Intercept)

def final (x, a, c):
    return ((x-c)/a)

MbyQ = final(ToF, Slope, Intercept)
print(MbyQ ** 2)