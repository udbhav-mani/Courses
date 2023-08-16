from math import pi

def volume(h, r=10):
    a = (4 * pi * (r**3)) / 3
    b = (pi * (h**2) * ((3 * r) - h)) / 3
    return a - b


print(volume(2))
