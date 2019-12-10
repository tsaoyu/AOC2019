import numpy as np
import matplotlib.pyplot as plt
with open('input.txt', 'r') as f:
    input_val = f.read()

val = np.array([int(i) for i in input_val])
val = val.reshape(-1, 6, 25)
min_zero = np.argmin((val == 0).sum(axis=(1,2)))

print((val[min_zero]  == 2).sum() * (val[min_zero]  == 1).sum())


out = np.apply_along_axis(lambda x: x[np.argmax(x < 2)], 0, val)
plt.matshow(out)
plt.show()