import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load your data from the CSV file
df = pd.read_csv("qlearning_results.csv")

# Extract the x, y, and z values from the DataFrame
x = df["Learning rate (x)"]
y = df["Discount rate (y)"]
z = df["No. of Eps (z)"]

# Create a 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(x, y, z, cmap='viridis')

# Set labels for the axes
ax.set_xlabel("Learning rate (x)")
ax.set_ylabel("Discount rate (y)")
ax.set_zlabel("No. of Episodes (z)")

# Show the plot
plt.show()
