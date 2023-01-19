import matplotlib.pyplot as plt
import numpy as np

# so that undefined values are ignored
np.seterr(divide='ignore', invalid='ignore')

# x-values to evaluate from [-10, 10] increasing by 0.0005 each time
x = np.arange(-10, 10, 0.0005)

# Equations
y1 = 2 * np.sqrt((-abs(abs(x) - 1)) * abs(3 - abs(x)) / ((abs(x) - 1) * (3 - abs(x)))) * (
        1 + abs(abs(x) - 3) / (abs(x) - 3)) * np.sqrt(1 - (x / 7) ** 2) + (
            5 + 0.97 * (abs(x - 0.5) + abs(x + 0.5)) - 3 * (abs(x - 0.75) + abs(x + 0.75))) * (
            1 + abs(1 - abs(x)) / (1 - abs(x)))
y2 = (-3) * np.sqrt(1 - (x / 7) ** 2) * np.sqrt(abs(abs(x) - 4) / (abs(x) - 4))
y3 = abs(x / 2) - 0.0913722 * x ** 2 - 3 + np.sqrt(1 - (abs(abs(x) - 2) - 1) ** 2)
y4 = (2.71052 + 1.5 - 0.5 * abs(x) - 1.35526 * np.sqrt(4 - (abs(x) - 1) ** 2)) * np.sqrt(abs(abs(x) - 1) /
                                                                                         (abs(x) - 1)) + 0.9
# plotting the equations on to the graph
plt.plot(x, y1, color='black')
plt.plot(x, y2, color='black')
plt.plot(x, y3, color='black')
plt.plot(x, y4, color='black')

# Title
plt.title('Batman')

# Save to batman.png image output
plt.savefig("batman.png", bbox_inches='tight')

# show the graph
plt.show()

# close it
plt.close()
