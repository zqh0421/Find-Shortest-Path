import sys
import time
import math
import numpy as np
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from collections import deque
from queue import Queue

# 常数
inf = 1e8
ROW = COL = 20
SQUARE_SIZE = 28
BLANK = 0
WALL = 1

# 移动方向
V = [-1, 0, 0, 1, -1, -1, 1, 1]
H = [0, 1, -1, 0, -1, 1, -1, 1]

# 颜色设置
BLANK_COLOR = QColor("#FFFFFF")
WALL_COLOR = QColor("#575255")
START_COLOR = QColor("#00CB00")
END_COLOR = QColor("#4D53D5")
GRID_LINE_COLOR = QColor("#D7D7D7")
VISITED_COLOR = QColor("#CFF4F4")
ARRIVAL_COLOR = QColor("#FF8322")
PATH_COLOR = QColor("#8485BB")
PROCESSING_COLOR = QColor("#98FB98")


# 类声明
class Node:
    def __init__(self, x=-1, y=-1, step=0):
        self.x = x
        self.y = y
        self.parent = None
        self.step = step

    def copy(self):
        N = Node(self.x, self.y, self.step)
        N.parent = self.parent
        return N


def heuristic(a, b, method="Manhattan"):
    dx = abs(a.x - b.x)
    dy = abs(a.y - b.y)
    if method == "Manhattan":
        return dx + dy

    elif method == "Euclidean":
        return math.sqrt(dx * dx + dy * dy)
    elif method == "Octile":
        k = math.sqrt(2.) - 1.
        return k * min(dx, dy) + max(dx, dy)
    elif method == "Chebyshev":
        return max(dx, dy)
    else:
        print(f'{method} is not an available method!')
        print(f'Please choose method from "Manhattan", "Euclidean", "Octile" and "Chebyshev')


def readSampleData(message):
    matrix = np.zeros((ROW, COL))
    file = open('data/' + message + '.txt')
    data = file.read()
    dataList = data.split('\n')
    for i in range(len(dataList)):
        for j in range(len(dataList[0])):
            matrix[i][j] = int(dataList[i][j])
    return matrix


def moveCost(i):
    if i < 4:
        return 1.0
    return math.sqrt(2.0) * 1.0
