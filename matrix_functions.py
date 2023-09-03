import math
import numpy as np


def translate(pos):
    tx, ty, tz = pos
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [tx, ty, tz, 1]
    ])


def rotate_x(a):
    return np.array([
        [1, 0, 0, 0],
        [0, math.cos(a), math.sin(a), 0],
        [0, -math.sin(a), math.cos(a), 0],
        [0, 0, 0, 1]
    ])


def rotate_y(a):
    return np.array([
        [math.cos(a), 0, -math.sin(a), 0],
        [0, 1, 0, 0],
        [math.sin(a), 0, math.cos(a), 0],
        [0, 0, 0, 1]
    ])


def rotate_z(a):
    return np.array([
        [math.cos(a), math.sin(a), 0, 0],
        [-math.sin(a), math.cos(a), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def rotate_axis(axis, angle):
    c = math.cos(angle)
    s = math.sin(angle)
    omc = 1 - c
    x, y, z = axis

    return np.array([
        [x*x*omc+c,   y*x*omc+z*s, x*z*omc-y*s, 0],
        [x*y*omc-z*s, y*y*omc+c,   y*z*omc+x*s, 0],
        [x*z*omc+y*s, y*z*omc-x*s, z*z*omc+c,   0],
        [0,           0,           0,           1]
    ])

def rotate_xyz(angle_x: float,
               angle_y: float,
               angle_z: float) -> 'Matrix44':
    cx = math.cos(angle_x)
    sx = math.sin(angle_x)
    cy = math.cos(angle_y)
    sy = math.sin(angle_y)
    cz = math.cos(angle_z)
    sz = math.sin(angle_z)

    sxsy = sx*sy
    cxsy = cx*sy

    return np.array([ 
        [ cy*cz,  sxsy*cz+cx*sz, -cxsy*cz+sx*sz, 0],
        [-cy*sz, -sxsy*sz+cx*cz,  cxsy*sz+sx*cz, 0],
        [    sy,         -sx*cy,          cx*cy, 0],
        [     0,              0,              0, 1]
    ])

def scale(n):
    return np.array([
        [n, 0, 0, 0],
        [0, n, 0, 0],
        [0, 0, n, 0],
        [0, 0, 0, 1]
    ])
