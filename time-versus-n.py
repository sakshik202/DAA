import numpy as np
import matplotlib.pyplot as plt

n_values = np.arange(1, 101)  # Replace 101 with your desired maximum 'n'
runtimes = 1 + n_values**2   # The polynomial curve T(n) = 1 + n^2

plt.plot(n_values, runtimes, label="T(n) = 1 + n^2")
plt.xlabel("n")
plt.ylabel("Time")
plt.legend()
plt.show()
