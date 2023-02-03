import matplotlib.pyplot as plt
import numpy as np

# Finding the slope and Intercept of ToF vs sqrt(M/Q graph)
x_data= [1, 3.741657387, 6.633249581]
y_data = [1115, 4092, 7227]

z = np.polyfit(x_data, y_data, 1)
p = np.poly1d(z)
plt.plot(x_data, p(x_data), "r-o")
print("Slope and Interecept are respectively: ", z)
plt.xlabel("Sqrt(m/q)")
plt.ylabel("ToF")
plt.title("ToF vs Sqrt(m/q)")
plt.show()

