# create an x_y grid
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

class Cube:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Hex:
    def __init__(self, q, r):
        self.q = q
        self.r = r

def pixel_to_hex(x, y,size):

    q = (x * sqrt(3)/3 - y / 3) / size
    r = y * 2/3 / size
    return hex_round(Hex(q, r))

def hex_round(h):
    return cube_to_hex(cube_round(hex_to_cube(h)))

def cube_to_hex(h): # axial
    q = h.x
    r = h.z
    return Hex(q, r)

def hex_to_cube(h): # axial
    x = h.q
    z = h.r
    y = -x-z
    return Cube(x, y, z)

def hex_to_pixel(hex):
    x = size * sqrt(3) * (hex.q + hex.r/2)
    y = size * 3/2 * hex.r
    return Point(x, y)

def cube_round(h):
    rx = round(h.x)
    ry = round(h.y)
    rz = round(h.z)

    x_diff = abs(rx - h.x)
    y_diff = abs(ry - h.y)
    z_diff = abs(rz - h.z)

    if x_diff > y_diff and x_diff > z_diff:
        rx = -ry-rz
    elif y_diff > z_diff:
        ry = -rx-rz
    else:
        rz = -rx-ry

    return Cube(rx, ry, rz)

xs = np.arange(0,1,0.01)
ys = np.arange(0,1,0.01)

ps = np.zeros((len(xs)*len(ys),4))

n = 0
for i, x in enumerate(xs):
    for j,y in enumerate(ys):
        ps[n][0] = x
        ps[n][1] = y
        h = pixel_to_hex(x,y,0.2)
        ps[n][2] = h.q
        ps[n][3] = h.r
    
        n = n+1

plt.scatter(ps[:,0],ps[:,1],marker='.',c=ps[:,2] * ps[:,3],s=100)
plt.show()

