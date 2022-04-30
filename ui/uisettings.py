# Form implementation generated from reading ui file 'ui/uisettings.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Widgets(object):
    def setupUi(self, Widgets):
        Widgets.setObjectName("Widgets")
        Widgets.resize(800, 600)
        Widgets.setMaximumSize(QtCore.QSize(800, 600))
        Widgets.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.visualizer = QtWidgets.QGraphicsView(Widgets)
        self.visualizer.setGeometry(QtCore.QRect(230, 20, 560, 560))
        self.visualizer.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.visualizer.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.visualizer.setObjectName("visualizer")
        self.verticalLayoutWidget = QtWidgets.QWidget(Widgets)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 182, 53))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layoutAlgorithm = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layoutAlgorithm.setContentsMargins(0, 0, 0, 0)
        self.layoutAlgorithm.setObjectName("layoutAlgorithm")
        self.labelAlgorithm = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelAlgorithm.setMinimumSize(QtCore.QSize(0, 0))
        self.labelAlgorithm.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelAlgorithm.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelAlgorithm.setObjectName("labelAlgorithm")
        self.layoutAlgorithm.addWidget(self.labelAlgorithm)
        self.boxAlgorithm = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.boxAlgorithm.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxAlgorithm.sizePolicy().hasHeightForWidth())
        self.boxAlgorithm.setSizePolicy(sizePolicy)
        self.boxAlgorithm.setMinimumSize(QtCore.QSize(0, 22))
        self.boxAlgorithm.setMaximumSize(QtCore.QSize(16777215, 22))
        self.boxAlgorithm.setObjectName("boxAlgorithm")
        self.boxAlgorithm.addItem("")
        self.boxAlgorithm.addItem("")
        self.boxAlgorithm.addItem("")
        self.boxAlgorithm.addItem("")
        self.layoutAlgorithm.addWidget(self.boxAlgorithm)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Widgets)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 350, 181, 41))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.layoutSlider = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.layoutSlider.setContentsMargins(0, 0, 0, 0)
        self.layoutSlider.setObjectName("layoutSlider")
        self.labelSlider = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.labelSlider.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelSlider.setObjectName("labelSlider")
        self.layoutSlider.addWidget(self.labelSlider)
        self.slider = QtWidgets.QSlider(self.verticalLayoutWidget_5)
        self.slider.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.slider.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider.setObjectName("slider")
        self.layoutSlider.addWidget(self.slider)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(Widgets)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 400, 181, 31))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.layoutPlay = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.layoutPlay.setContentsMargins(0, 0, 0, 0)
        self.layoutPlay.setObjectName("layoutPlay")
        self.buttonPlay = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.buttonPlay.setEnabled(False)
        self.buttonPlay.setMouseTracking(False)
        self.buttonPlay.setTabletTracking(False)
        self.buttonPlay.setAcceptDrops(False)
        self.buttonPlay.setCheckable(False)
        self.buttonPlay.setAutoDefault(False)
        self.buttonPlay.setDefault(False)
        self.buttonPlay.setFlat(False)
        self.buttonPlay.setObjectName("buttonPlay")
        self.layoutPlay.addWidget(self.buttonPlay)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(Widgets)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(20, 480, 181, 91))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.layoutDisplay = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.layoutDisplay.setContentsMargins(0, 0, 0, 0)
        self.layoutDisplay.setObjectName("layoutDisplay")
        self.layout_1 = QtWidgets.QHBoxLayout()
        self.layout_1.setObjectName("layout_1")
        self.labelVisitedNode = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.labelVisitedNode.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelVisitedNode.setObjectName("labelVisitedNode")
        self.layout_1.addWidget(self.labelVisitedNode)
        self.displayVisitedNode = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.displayVisitedNode.setMaximumSize(QtCore.QSize(75, 16777215))
        self.displayVisitedNode.setAcceptDrops(False)
        self.displayVisitedNode.setMaxLength(45)
        self.displayVisitedNode.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.displayVisitedNode.setReadOnly(True)
        self.displayVisitedNode.setObjectName("displayVisitedNode")
        self.layout_1.addWidget(self.displayVisitedNode)
        self.layoutDisplay.addLayout(self.layout_1)
        self.layout_2 = QtWidgets.QHBoxLayout()
        self.layout_2.setObjectName("layout_2")
        self.labelPathLength = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.labelPathLength.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelPathLength.setObjectName("labelPathLength")
        self.layout_2.addWidget(self.labelPathLength)
        self.displayPathLength = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.displayPathLength.setMaximumSize(QtCore.QSize(75, 16777215))
        self.displayPathLength.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.displayPathLength.setReadOnly(True)
        self.displayPathLength.setObjectName("displayPathLength")
        self.layout_2.addWidget(self.displayPathLength)
        self.layoutDisplay.addLayout(self.layout_2)
        self.layout_3 = QtWidgets.QHBoxLayout()
        self.layout_3.setObjectName("layout_3")
        self.labelTotalTime = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.labelTotalTime.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelTotalTime.setObjectName("labelTotalTime")
        self.layout_3.addWidget(self.labelTotalTime)
        self.displayTotalTime = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.displayTotalTime.setMaximumSize(QtCore.QSize(75, 16777215))
        self.displayTotalTime.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.displayTotalTime.setReadOnly(True)
        self.displayTotalTime.setObjectName("displayTotalTime")
        self.layout_3.addWidget(self.displayTotalTime)
        self.layoutDisplay.addLayout(self.layout_3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Widgets)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 440, 181, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layoutClear = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layoutClear.setContentsMargins(0, 0, 0, 0)
        self.layoutClear.setObjectName("layoutClear")
        self.buttonClearPath = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonClearPath.setObjectName("buttonClearPath")
        self.layoutClear.addWidget(self.buttonClearPath)
        self.buttonClearAll = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonClearAll.setObjectName("buttonClearAll")
        self.layoutClear.addWidget(self.buttonClearAll)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Widgets)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 70, 181, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layoutData = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layoutData.setContentsMargins(0, 0, 0, 0)
        self.layoutData.setObjectName("layoutData")
        self.labelData = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelData.setMinimumSize(QtCore.QSize(0, 0))
        self.labelData.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelData.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelData.setObjectName("labelData")
        self.layoutData.addWidget(self.labelData)
        self.boxData = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.boxData.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxData.sizePolicy().hasHeightForWidth())
        self.boxData.setSizePolicy(sizePolicy)
        self.boxData.setMinimumSize(QtCore.QSize(0, 0))
        self.boxData.setEditable(False)
        self.boxData.setObjectName("boxData")
        self.boxData.addItem("")
        self.boxData.addItem("")
        self.boxData.addItem("")
        self.boxData.addItem("")
        self.boxData.addItem("")
        self.boxData.addItem("")
        self.layoutData.addWidget(self.boxData)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Widgets)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 120, 181, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.layoutDirection = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.layoutDirection.setContentsMargins(0, 0, 0, 0)
        self.layoutDirection.setObjectName("layoutDirection")
        self.labelDirection = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelDirection.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelDirection.setObjectName("labelDirection")
        self.layoutDirection.addWidget(self.labelDirection)
        self.boxDirection = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.boxDirection.setObjectName("boxDirection")
        self.boxDirection.addItem("")
        self.boxDirection.addItem("")
        self.layoutDirection.addWidget(self.boxDirection)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Widgets)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 290, 181, 51))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkDiagonal = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkDiagonal.setObjectName("checkDiagonal")
        self.verticalLayout.addWidget(self.checkDiagonal)
        self.checkShortest = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkShortest.setObjectName("checkShortest")
        self.verticalLayout.addWidget(self.checkShortest)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Widgets)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 250, 181, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.layoutWeight = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layoutWeight.setContentsMargins(0, 0, 0, 0)
        self.layoutWeight.setObjectName("layoutWeight")
        self.labelWeight = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.labelWeight.setObjectName("labelWeight")
        self.layoutWeight.addWidget(self.labelWeight)
        self.lineEditWeight = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEditWeight.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditWeight.setText("")
        self.lineEditWeight.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEditWeight.setObjectName("lineEditWeight")
        self.layoutWeight.addWidget(self.lineEditWeight)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(Widgets)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(20, 190, 181, 51))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.layoutHeuristicMethod = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.layoutHeuristicMethod.setContentsMargins(0, 0, 0, 0)
        self.layoutHeuristicMethod.setObjectName("layoutHeuristicMethod")
        self.labelHeuristicMethod = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.labelHeuristicMethod.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelHeuristicMethod.setObjectName("labelHeuristicMethod")
        self.layoutHeuristicMethod.addWidget(self.labelHeuristicMethod)
        self.boxHeuristicMethod = QtWidgets.QComboBox(self.verticalLayoutWidget_8)
        self.boxHeuristicMethod.setObjectName("boxHeuristicMethod")
        self.boxHeuristicMethod.addItem("")
        self.boxHeuristicMethod.addItem("")
        self.boxHeuristicMethod.addItem("")
        self.boxHeuristicMethod.addItem("")
        self.boxHeuristicMethod.addItem("")
        self.layoutHeuristicMethod.addWidget(self.boxHeuristicMethod)

        self.retranslateUi(Widgets)
        QtCore.QMetaObject.connectSlotsByName(Widgets)

    def retranslateUi(self, Widgets):
        _translate = QtCore.QCoreApplication.translate
        Widgets.setWindowTitle(_translate("Widgets", "Form"))
        self.labelAlgorithm.setText(_translate("Widgets", "Select Algorithm"))
        self.boxAlgorithm.setItemText(0, _translate("Widgets", "- Select -"))
        self.boxAlgorithm.setItemText(1, _translate("Widgets", "A-Star Search"))
        self.boxAlgorithm.setItemText(2, _translate("Widgets", "Breadth-First Search"))
        self.boxAlgorithm.setItemText(3, _translate("Widgets", "Depth-First Search"))
        self.labelSlider.setText(_translate("Widgets", "Play Speed"))
        self.buttonPlay.setText(_translate("Widgets", "Start To Play"))
        self.labelVisitedNode.setText(_translate("Widgets", "Searched Nodes"))
        self.labelPathLength.setText(_translate("Widgets", "Path Length"))
        self.labelTotalTime.setText(_translate("Widgets", "Total Time"))
        self.buttonClearPath.setText(_translate("Widgets", "Clear Path"))
        self.buttonClearAll.setText(_translate("Widgets", "Clear All"))
        self.labelData.setText(_translate("Widgets", "Select Data"))
        self.boxData.setItemText(0, _translate("Widgets", "- Select -"))
        self.boxData.setItemText(1, _translate("Widgets", "sampledata1"))
        self.boxData.setItemText(2, _translate("Widgets", "sampledata2"))
        self.boxData.setItemText(3, _translate("Widgets", "sampledata3"))
        self.boxData.setItemText(4, _translate("Widgets", "sampledata4"))
        self.boxData.setItemText(5, _translate("Widgets", "sampledata5"))
        self.labelDirection.setText(_translate("Widgets", "Search Direction"))
        self.boxDirection.setItemText(0, _translate("Widgets", "From Start"))
        self.boxDirection.setItemText(1, _translate("Widgets", "From End"))
        self.checkDiagonal.setText(_translate("Widgets", "Allow Diagonal Movement"))
        self.checkShortest.setText(_translate("Widgets", "Find Shortest Path"))
        self.labelWeight.setText(_translate("Widgets", "Heuristic Weight"))
        self.labelHeuristicMethod.setText(_translate("Widgets", "Select Heuristic Method"))
        self.boxHeuristicMethod.setItemText(0, _translate("Widgets", "None"))
        self.boxHeuristicMethod.setItemText(1, _translate("Widgets", "Manhattan"))
        self.boxHeuristicMethod.setItemText(2, _translate("Widgets", "Euclidean"))
        self.boxHeuristicMethod.setItemText(3, _translate("Widgets", "Octile"))
        self.boxHeuristicMethod.setItemText(4, _translate("Widgets", "Chebyshev"))
