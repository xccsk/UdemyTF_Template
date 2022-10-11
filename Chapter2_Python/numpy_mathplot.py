import numpy as np
import matplotlib.pyplot as plt

my_array = np.array([2, 3, 4, 5, 6, 7], dtype=np.int32)
my_array2 = np.array([4, 5, 6, 7, 8, 9, ], dtype=np.int32)

print(my_array)


# Scatter Plot
plt.scatter(my_array, my_array2, color="black")
plt.legend(["f(x)"])
plt.title("das ist der titel")
plt.xlabel("gewinnprognose")
plt.ylabel("zeit")
plt.show()

#  Plot
plt.plot(my_array, my_array2, color="black")
plt.legend(["f(x)"])
plt.title("das ist der titel")
plt.xlabel("gewinnprognose")
plt.ylabel("zeit")
plt.show()
