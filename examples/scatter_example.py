import numpy as np
import matplotlib.pyplot as plt
import mpldatacursor

x, y, z = np.random.random((3, 10))
x[0] = x[1] + 0.01
y[0] = y[1] + 0.01
fig, ax = plt.subplots()
ax.scatter(x, y, c=z, s=100*np.random.random(10))
mpldatacursor.datacursor()
plt.show()
