import matplotlib.pyplot as plt
import math

n_values = list(range(1, 100))
linear = [n for n in n_values]
quadratic = [n**2 for n in n_values]
logarithmic = [math.log2(n) for n in n_values]

plt.plot(n_values, linear, label="O(n)")
plt.plot(n_values, quadratic, label="O(n²)")
plt.plot(n_values, logarithmic, label="O(log n)")
plt.xlabel("Input size n")
plt.ylabel("Operations")
plt.title("Growth of Time Complexities")
plt.legend()
plt.grid(True)
plt.show()
