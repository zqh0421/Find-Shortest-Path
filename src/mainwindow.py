from src.config import *
from ui.uisettings import Ui_Widgets


class MainWindow(QMainWindow):
    def __init__(self):
        # 初始化界面
        super().__init__()
        self.ui = Ui_Widgets()
        self.initialUI()
        # 初始值
        self.scene = None
        self.delay = 0.25
        self.searchDirection = 0
        self.neighborNumber = 4
        self.startNode = Node(0, 0)
        self.endNode = Node(ROW - 1, COL - 1)
        self.isClearing = False
        self.isPathCleared = True
        self.isWallsCleared = True
        self.heuristicWeight = 1
        self.heuristicMethod = "Manhattan"

        self.initialSlider()  # 演示速度设定
        self.initialSignal()  # 信号初始化
        self.matrix = np.zeros((ROW, COL))  # 地图数据矩阵
        self.visualize()  # 数据可视化

    # 前端部分
    def initialUI(self):
        self.ui.setupUi(self)
        self.setWindowTitle("Shortest Path Finding Algorithms")
        self.ui.checkShortest.setEnabled(False)
        self.ui.checkShortest.setChecked(False)
        self.ui.lineEditWeight.setEnabled(False)
        self.ui.lineEditWeight.setText("0")
        validator = QDoubleValidator()
        validator.setRange(0, 999999)
        self.ui.lineEditWeight.setValidator(validator)
        self.ui.lineEditWeight.setMaxLength(6)
        self.ui.boxHeuristicMethod.setEnabled(False)
        self.ui.buttonPlay.setText("Select Algorithm and Data")

    def initialSignal(self):
        # 演示速度
        self.ui.slider.valueChanged.connect(self.speedChange)
        # 开始演示信号
        self.ui.buttonPlay.pressed.connect(self.algorithm)
        # 清除按钮
        self.ui.buttonClearAll.pressed.connect(self.clearAll)
        self.ui.buttonClearPath.pressed.connect(self.clearPath)
        # enabled设置（data）
        self.ui.boxData.currentIndexChanged.connect(self.matrixMethod)
        self.ui.boxData.currentIndexChanged.connect(self.readyToPlay)
        # enabled设置（algorithm）
        self.ui.boxAlgorithm.currentIndexChanged.connect(self.readyToPlay)
        self.ui.boxAlgorithm.currentIndexChanged.connect(self.checkShortest)
        # 是否支持对角线前进
        self.ui.checkDiagonal.clicked.connect(self.isDiagonal)
        # 搜索方向from start/end
        self.ui.boxDirection.currentIndexChanged.connect(self.setSearchDirection)
        # 启发式算法的数值及按键设置
        self.ui.boxAlgorithm.currentIndexChanged.connect(self.checkHeuristic)
        self.ui.boxHeuristicMethod.currentIndexChanged.connect(self.setHeuristicMethod)
        self.ui.lineEditWeight.textChanged.connect(self.setHeuristicWeight)
        self.ui.boxHeuristicMethod.currentIndexChanged.connect(self.readyToPlay)

    def initialSlider(self):
        self.ui.slider.setMinimum(0)
        self.ui.slider.setMaximum(500)
        self.ui.slider.setValue(250)
        self.ui.slider.setTickInterval(200)

    def visualize(self):
        # 初始化图形平面
        self.scene = QGraphicsScene()
        # 清除绘图界面的滚动条
        self.ui.visualizer.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.visualizer.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # 背景颜色
        self.scene.setBackgroundBrush(BLANK_COLOR)
        # 绘制网格
        self.drawGrid()
        self.paintStartNode()
        self.paintEndNode()

    def matrixMethod(self):
        message = self.ui.boxData.itemText(self.ui.boxData.currentIndex())
        self.clearAll(False)
        if message == "- Select -":
            print(f"You are not allowed to start with None data.")
        else:
            self.matrix = readSampleData(message)
            self.showData()
            self.paintStartNode()
            self.paintEndNode()

    # 在play/clear时禁用左侧功能栏，结束后启用
    def setAllEnabled(self, state):
        self.ui.boxAlgorithm.setEnabled(state)
        self.ui.boxData.setEnabled(state)
        self.ui.boxDirection.setEnabled(state)
        self.ui.checkDiagonal.setEnabled(state)
        self.ui.buttonPlay.setEnabled(state)
        self.ui.buttonClearAll.setEnabled(state)
        self.ui.buttonClearPath.setEnabled(state)
        if self.ui.boxAlgorithm.itemText(self.ui.boxAlgorithm.currentIndex()) == "Depth-First Search":
            self.ui.checkShortest.setEnabled(state)
        if self.ui.boxAlgorithm.itemText(self.ui.boxAlgorithm.currentIndex()) == "A-Star Search":
            self.ui.lineEditWeight.setEnabled(state)
            self.ui.boxHeuristicMethod.setEnabled(state)

    def setSearchDirection(self):
        self.searchDirection = self.ui.boxDirection.currentIndex()

    def setHeuristicWeight(self):
        self.heuristicWeight = float(self.ui.lineEditWeight.text())

    def setHeuristicMethod(self):
        self.heuristicMethod = self.ui.boxHeuristicMethod.itemText(self.ui.boxHeuristicMethod.currentIndex())

    def checkHeuristic(self):
        message = self.ui.boxAlgorithm.itemText(self.ui.boxAlgorithm.currentIndex())
        if message == "A-Star Search":
            self.ui.boxHeuristicMethod.setEnabled(True)
            self.ui.boxHeuristicMethod.setCurrentIndex(1)
            self.ui.lineEditWeight.setEnabled(True)
            self.ui.lineEditWeight.setText("1")
        else:
            self.ui.boxHeuristicMethod.setEnabled(False)
            self.ui.boxHeuristicMethod.setCurrentIndex(0)
            self.ui.lineEditWeight.setEnabled(False)
            self.ui.lineEditWeight.setText("0")

    def isDiagonal(self):
        if self.ui.checkDiagonal.isChecked():
            self.neighborNumber = 8
        else:
            self.neighborNumber = 4

    def checkShortest(self):
        message = self.ui.boxAlgorithm.itemText(self.ui.boxAlgorithm.currentIndex())
        if message == "- Select -":
            self.ui.checkShortest.setEnabled(False)
            self.ui.checkShortest.setChecked(False)
        elif message == "Depth-First Search":
            self.ui.checkShortest.setEnabled(True)
            self.ui.checkShortest.setChecked(False)
        else:
            self.ui.checkShortest.setEnabled(False)
            self.ui.checkShortest.setChecked(True)

    def readyToPlay(self):
        m1 = self.ui.boxAlgorithm.itemText(self.ui.boxAlgorithm.currentIndex())
        m2 = self.ui.boxData.itemText(self.ui.boxData.currentIndex())
        if m1 == "- Select -" and m2 == "- Select -":
            self.ui.buttonPlay.setEnabled(False)
            self.ui.buttonPlay.setText("Select Algorithm and Data")
        elif m1 == "- Select -":
            self.ui.buttonPlay.setEnabled(False)
            self.ui.buttonPlay.setText("Select Algorithm")
        elif m2 == "- Select -":
            self.ui.buttonPlay.setEnabled(False)
            self.ui.buttonPlay.setText("Select Data")
        elif self.isClearing:
            self.ui.buttonPlay.setEnabled(False)
        elif m1 == "A-Star Search" and self.heuristicMethod == "None":
                self.ui.buttonPlay.setEnabled(False)
                self.ui.buttonPlay.setText("Select Heuristic Method")
        else:
            self.ui.buttonPlay.setEnabled(True)
            self.ui.buttonPlay.setText("Start To Play")

    def clearAll(self, default=True):
        if self.isPathCleared == False or self.isWallsCleared == False:
            self.setAllEnabled(False)
            self.ui.buttonClearAll.setText("Clearing")
            self.ui.buttonPlay.setText("Clearing All")
            self.isClearing = True
            self.readyToPlay()
            self.matrix = np.zeros((ROW, COL))
            self.showData()
            self.isPathCleared = True
            self.isWallsCleared = True
            if default:
                self.ui.boxData.setCurrentIndex(0)
            self.isClearing = False
            self.ui.buttonPlay.setText("Start To Play")
            self.ui.buttonClearAll.setText("Clear All")
            self.setAllEnabled(True)
            self.readyToPlay()

    def clearPath(self):
        if not self.isPathCleared:
            self.setAllEnabled(False)
            self.ui.buttonClearPath.setText("Clearing")
            self.isClearing = True
            self.readyToPlay()
            self.ui.buttonPlay.setText("Clearing Path")
            self.paintStartNode()
            self.paintEndNode()
            (s, e) = (self.startNode, self.endNode)
            for i in range(ROW):
                for j in range(COL):
                    if self.matrix[i][j] == BLANK and (i, j) != (s.x, s.y) and (i, j) != (e.x, e.y):
                        self.paint(j * SQUARE_SIZE, i * SQUARE_SIZE, BLANK_COLOR)
            self.isPathCleared = True
            self.isClearing = False
            self.ui.buttonPlay.setText("Start To Play")
            self.ui.buttonClearPath.setEnabled(True)
            self.ui.buttonClearAll.setEnabled(True)
            self.ui.buttonClearPath.setText("Clear Path")
            self.setAllEnabled(True)
            self.readyToPlay()

    def speedChange(self):
        self.delay = 0.5 - self.ui.slider.value() * 0.001  # 单位：秒

    def drawGrid(self):
        # 添加竖直网格线
        for x in range(0, 560, SQUARE_SIZE):
            self.scene.addLine(x, 0, x, 560, GRID_LINE_COLOR)
        # 添加水平网格线
        for y in range(0, 560, SQUARE_SIZE):
            self.scene.addLine(0, y, 560, y, GRID_LINE_COLOR)
        # 更新显示屏幕
        self.ui.visualizer.setScene(self.scene)
        # 事件过滤器
        self.ui.visualizer.viewport().installEventFilter(self)

    def showData(self):
        s = self.startNode
        e = self.endNode
        for i in range(ROW):
            for j in range(COL):
                if self.matrix[i][j] == BLANK and (i, j) != (s.x, s.y) and (i, j) != (e.x, e.y):
                    self.paint(j * SQUARE_SIZE, i * SQUARE_SIZE, BLANK_COLOR)
                if self.matrix[i][j] == WALL:
                    self.paint(j * SQUARE_SIZE, i * SQUARE_SIZE, WALL_COLOR)
        self.isWallsCleared = False

    def paintStartNode(self):
        brush = QBrush()
        brush.setColor(START_COLOR)
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        self.scene.addRect(QRectF(self.startNode.y * SQUARE_SIZE, self.startNode.x * SQUARE_SIZE,
                                  SQUARE_SIZE, SQUARE_SIZE), GRID_LINE_COLOR, brush)
        QApplication.processEvents()

    def paintEndNode(self):
        brush = QBrush()
        brush.setColor(END_COLOR)
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        self.scene.addRect(QRectF(self.endNode.y * SQUARE_SIZE, self.endNode.x * SQUARE_SIZE,
                                  SQUARE_SIZE, SQUARE_SIZE), GRID_LINE_COLOR, brush)
        QApplication.processEvents()

    def paint(self, x, y, fillColor, isDelayed=False):
        brush = QBrush()
        brush.setColor(fillColor)
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        self.scene.addRect(QRectF(x, y, SQUARE_SIZE, SQUARE_SIZE), GRID_LINE_COLOR, brush)
        QApplication.processEvents()
        if isDelayed:
            time.sleep(self.delay)

    def printData(self, searched, length, interval):
        self.ui.displayVisitedNode.setText(f"{searched}")
        self.ui.displayPathLength.setText(f"{length:.2f}")
        self.ui.displayTotalTime.setText(f"{interval:.2f}s")

    def printPath(self, path):  # 打印以列表形式存储的路径节点
        if not path:
            return
        if self.searchDirection == 1:
            path = reversed(path)
        for (x, y) in path:
            if (x, y) != (self.endNode.x, self.endNode.y) and (x, y) != (self.startNode.x, self.startNode.y):
                self.paint(y * SQUARE_SIZE, x * SQUARE_SIZE, PATH_COLOR, True)
        if (self.endNode.x, self.endNode.y) != (self.startNode.x, self.startNode.y):
            self.paint(self.endNode.y * SQUARE_SIZE, self.endNode.x * SQUARE_SIZE, ARRIVAL_COLOR, True)  # touch end

    def algorithm(self):
        message = self.ui.boxAlgorithm.itemText(self.ui.boxAlgorithm.currentIndex())
        self.clearPath()
        self.setAllEnabled(False)
        self.ui.buttonPlay.setText("Playing...")
        print(message)
        if message == "Breadth-First Search":
            self.printPath(self.bfs())
        elif message == "Depth-First Search":
            self.printPath(self.dfs())
        elif message == "A-Star Search":
            self.printPath(self.astar())
        self.ui.buttonPlay.setText("Start To Play")
        self.isPathCleared = False
        self.setAllEnabled(True)

    # 后端算法
    def backtrace(self, u, curPath=None):  # 回溯父结点的同时打印
        if curPath is None:
            curPath = []
        if u is None:
            return curPath
        if u.x == self.startNode.x and u.y == self.startNode.y:
            return curPath
        self.backtrace(u.parent, curPath)
        curPath.append((u.x, u.y))
        return curPath

    def bfs(self):
        tik = time.perf_counter()
        if self.searchDirection == 0:
            s = self.startNode.copy()
            e = self.endNode.copy()
        else:
            s = self.endNode.copy()
            e = self.startNode.copy()
        q = Queue()
        q.put(s)
        visited = {(s.x, s.y)}
        while not q.empty():
            u = q.get()
            # 到达终点
            if (u.x, u.y) == (e.x, e.y):
                #  打印数据
                tok = time.perf_counter()
                self.printData(len(visited), u.step, tok - tik)
                print(f"Path is found!")
                while not q.empty():  # 清空队列并更新visited颜色标记
                    w = q.get()
                    if (w.x, w.y) != (s.x, s.y) and (w.x, w.y) != (e.x, e.y):
                        self.paint(w.y * SQUARE_SIZE, w.x * SQUARE_SIZE, VISITED_COLOR, True)
                return self.backtrace(u.parent)
            # 对过程结点进行标记
            if (u.x, u.y) != (s.x, s.y) and (u.x, u.y) != (e.x, e.y):
                self.paint(u.y * SQUARE_SIZE, u.x * SQUARE_SIZE, VISITED_COLOR)  # visited
            # 前进
            for i in range(self.neighborNumber):
                w = u.copy()
                w.x = u.x + H[i]
                w.y = u.y + V[i]
                if 0 <= w.x < ROW and 0 <= w.y < COL:  # 范围判断
                    if self.matrix[w.x][w.y] == BLANK and (w.x, w.y) not in visited:
                        visited.add((w.x, w.y))  # 标记已访问
                        w.parent = u  # 记录前继结点
                        w.step = u.step + moveCost(i)  # 前进
                        q.put(w)  # 入队列
                        if (w.x, w.y) != (s.x, s.y) and (w.x, w.y) != (e.x, e.y):
                            self.paint(w.y * SQUARE_SIZE, w.x * SQUARE_SIZE, PROCESSING_COLOR, True)
        print(f"Path does not exist!")
        return []

    def dfs(self):
        tik = time.perf_counter()
        if self.searchDirection == 0:
            s = self.startNode.copy()
            e = self.endNode.copy()
        else:
            s = self.endNode.copy()
            e = self.startNode.copy()
        stack = deque()
        stack.append(s)
        visited = {(s.x, s.y)}
        minStep = 401
        minPath = None
        while stack:
            u = stack.pop()
            # 到达终点
            if (u.x, u.y) == (e.x, e.y):
                #  打印数据
                tok = time.perf_counter()
                self.printData(len(visited), u.step, tok - tik)
                print(f"Path is found!")
                while stack:  # 清空stack并更新visited颜色标记
                    w = stack.pop()
                    if (w.x, w.y) != (s.x, s.y) and (w.x, w.y) != (e.x, e.y):
                        self.paint(w.y * SQUARE_SIZE, w.x * SQUARE_SIZE, VISITED_COLOR)
                # 存储路径
                path = self.backtrace(u.parent, [])
                if len(path) < minStep:
                    # store path
                    minPath = path
                    minStep = len(path)
                return minPath
            # 对过程结点进行标记
            visited.add((u.x, u.y))
            if (u.x, u.y) != (s.x, s.y) and (u.x, u.y) != (e.x, e.y):
                self.paint(u.y * SQUARE_SIZE, u.x * SQUARE_SIZE, VISITED_COLOR)  # visited
            # 前进
            for i in range(self.neighborNumber):
                w = u.copy()
                w.x = u.x + H[i]
                w.y = u.y + V[i]
                if 0 <= w.x < ROW and 0 <= w.y < COL:  # 范围判断
                    if self.matrix[w.x][w.y] == BLANK and (w.x, w.y) not in visited:
                        w.parent = u  # 记录前继结点
                        w.step = u.step + moveCost(i)  # 距离增加
                        stack.append(w)  # 入栈
                        if (w.x, w.y) != (s.x, s.y) and (w.x, w.y) != (e.x, e.y):
                            self.paint(w.y * SQUARE_SIZE, w.x * SQUARE_SIZE, PROCESSING_COLOR, True)
        print(f"Path does not exist!")
        return []

    def astar(self):
        tik = time.perf_counter()
        # 初始化
        if self.searchDirection == 0:
            s = self.startNode.copy()
            e = self.endNode.copy()
        else:
            s = self.endNode.copy()
            e = self.startNode.copy()
        priorityQueue = [(s, 0, s.x * COL + s.y)]
        visited = {(s.x, s.y)}
        while len(priorityQueue):
            priorityQueue = sortMin(priorityQueue)
            # 从优先队列q中删除第一个状态，称之为cur
            u = priorityQueue[0][0]
            priorityQueue.remove(priorityQueue[0])
            # 到达终点
            if (u.x, u.y) == (e.x, e.y):
                #  打印数据
                tok = time.perf_counter()
                self.printData(len(visited), u.step, tok - tik)
                print(f"Path is found!")
                for i in range(len(priorityQueue)):  # 清空队列并更新visited颜色标记
                    w = priorityQueue[i][0]
                    if (w.x, w.y) != (s.x, s.y) and (w.x, w.y) != (e.x, e.y):
                        self.paint(w.y * SQUARE_SIZE, w.x * SQUARE_SIZE, VISITED_COLOR)
                return self.backtrace(u.parent)
            # 对过程结点进行标记
            if (u.x, u.y) != (s.x, s.y) and (u.x, u.y) != (e.x, e.y):
                self.paint(u.y * SQUARE_SIZE, u.x * SQUARE_SIZE, VISITED_COLOR, True)  # visited
            # 生成cur的所有子状态near
            for i in range(self.neighborNumber):
                near = u.copy()
                near.x = u.x + H[i]
                near.y = u.y + V[i]
                newStep = u.step + moveCost(i)
                if 0 <= near.x < ROW and 0 <= near.y < COL and self.matrix[near.x][near.y] == BLANK:
                    if (near.x, near.y) not in visited or newStep < near.step:  # 没有搜索过的点规定为距离无穷大
                        # 计算子状态的估计函数值
                        near.step = newStep
                        visited.add((near.x, near.y))
                        near.parent = u
                        np1 = near.x * COL + near.y
                        np2 = near.step + self.heuristicWeight + heuristic(near, e, self.heuristicMethod)
                        priorityQueue.append((near, np1, np2))
                        if (near.x, near.y) != (s.x, s.y) and (near.x, near.y) != (e.x, e.y):
                            self.paint(near.y * SQUARE_SIZE, near.x * SQUARE_SIZE, PROCESSING_COLOR, True)
        print(f"Path does not exist!")
        return []
