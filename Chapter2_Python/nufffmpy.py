import numpy as np

my_arrey = np.zeros(shape=(2, 2), dtype=np.int32)
print(my_arrey)

my_reshaped_arrey = np.reshape(my_arrey, newshape=(4,))
print(my_reshaped_arrey)
