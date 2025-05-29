import matplotlib.pyplot as plt

# Temperature readings for the week
temperatures = [20, 22, 19, 23, 21, 24, 20]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Plotting the graph
plt.plot(days, temperatures)
plt.title("Temperature Over the Week")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
