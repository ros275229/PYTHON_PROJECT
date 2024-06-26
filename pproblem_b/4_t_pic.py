import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Loading the data again
data = pd.read_excel("C:\\Users\\Redmi\\Desktop\\b_yss\\fj.xlsx", header=None)

# Create meshgrid for the 3D plot
x = np.linspace(0, 4, data.shape[1])
y = np.linspace(0, 5, data.shape[0])
X, Y = np.meshgrid(x, y)

# Plotting the 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, data, cmap='viridis')
fig.colorbar(surf, ax=ax, label='Depth (m)')
ax.set_xlabel('west-East Distance (nautical miles) ')
ax.set_ylabel(' South-North Distance (nautical miles)')
ax.set_zlabel('Depth (m) ')
ax.set_title(' 3D Sea Depth Distribution ')
plt.show()
