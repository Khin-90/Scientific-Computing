step = 0.1
volume = 0.0

x = 0.0
while x <= 1:
    y = 0.0
    while y <= 1:
        z = x**2 + y**2
        volume += z * (step * step)
        y += step
    x += step

print("Approximate volume under the surface:", volume)
