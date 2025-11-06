import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create a simple line plot
plt.plot(x, y, color='blue', marker='o', linestyle='--')

# Add title and labels
plt.title("Basic Line Chart using Matplotlib")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Display the graph
plt.show()
