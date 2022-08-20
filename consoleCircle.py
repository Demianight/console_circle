from math import sin
import numpy as np
from numba import njit, prange


@njit(fastmath=True, parallel=True)
def makeList(num):
    width = 120
    height = 30
    div = width / height
    div1 = 11 / 24
    mainList = np.zeros(height * width)
    num /= 1000
    for i in prange(width):
        for j in prange(height):

            x = (i / width * 2 - 1) * div * div1
            y = j / height * 2 - 1
            x += sin(num)
            if x ** 2 + y ** 2 > 0.5:
                mainList[i + j * width] = 1
            else:
                mainList[i + j * width] = 0
    return mainList


def drawing():
    pic = ''
    for x in range(10000000000):
        for elm in makeList(x):
            if elm == 0:
                pic += '@'
            elif elm == 1:
                pic += ' '
        print(pic)
        pic = ''


drawing()
