from PyQt4 import QtCore, QtGui
from config import *
from myThread import MyThread

class MyPixmap(QtGui.QGraphicsPixmapItem):
    def __init__(self, parent):
        QtGui.QGraphicsPixmapItem.__init__(self)
        self.parent = parent
        self.currentSide = 0
        
        self.thread = MyThread(self.parent, self.parent.getRandom)
        self.thread.finished.connect(self.parent.errorHandler)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.swapCoin)
        
    def mousePressEvent(self, e):
        if self.thread.isRunning() and self.timer.isActive():
            e.ignore()
        else:
            self.parent.hint.hide() 
            self.count = 0 # counter for coin's swaping
            self.timer.start(50)     
            self.thread.start()
            e.accept()

    def swapCoin(self):
        if self.count < 50 or self.thread.isRunning():
            self.currentSide = int(not self.currentSide) # 1 turns to 0, 0 to 1
            self.setPixmap (self.parent.comboBox.itemData(self.parent.comboBox.currentIndex())[ self.currentSide ])
            self.count += 1
        else:
            self.timer.stop()
            if not self.parent.error and self.parent.result:
                self.setPixmap (self.parent.comboBox.itemData(self.parent.comboBox.currentIndex())[ int(self.parent.result[0]) ]) # SHOW RESULT!
                
            self.parent.log(error=self.parent.error) # log into journal
            
        
class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None, master=None):
        QtGui.QWidget.__init__(self, parent)
        self.master = master
        self.error = None
        self.result = 0
            
        self.coinScene = QtGui.QGraphicsScene(0.0, 0.0, 250, 250)
        #self.coin.setBackgroundBrush(QtCore.Qt.white)
        self.img = MyPixmap(parent=self)
        
        self.hint = QtGui.QGraphicsTextItem()
        self.hint.setPlainText("Click on the coin to flip it")
        self.hint.setDefaultTextColor(QtCore.Qt.red)
        self.hint.setFont(QtGui.QFont("Verdana", 12, QtGui.QFont.Bold))
        #self.hint.setPos(QtCore.QPointF(25, 0))
        
        self.coinScene.addItem(self.img)
        self.coinScene.addItem(self.hint)
        
        view = QtGui.QGraphicsView(self.coinScene)
        view.setStyleSheet("background: transparent; border: 0px") # remove border and background of canvas 

        self.comboBox = QtGui.QComboBox()
        self.comboBox.currentIndexChanged["int"].connect(self.change_coin)
        self.get_coins()
        
        self.box = QtGui.QVBoxLayout()
        self.box.addWidget(self.comboBox)
        self.box.addWidget(view)
        self.setLayout(self.box)

    def get_coins(self):
        import glob, os

        for path in glob.glob(PICSCOINS + "*-[0].png"):
            file = os.path.basename(path).split("-")[0]
            if self.comboBox.findText(file, flags=QtCore.Qt.MatchFixedString) != -1:
                continue
            if os.path.isfile(PICSCOINS + file + "-1.png"):
                self.comboBox.setIconSize(QtCore.QSize(24, 24))
                ico = QtGui.QIcon(PICSCOINS + file + "-0.png")
                self.comboBox.addItem(ico, file, 
                                     [QtGui.QPixmap(PICSCOINS + file + "-0.png", "PNG"),  # (icon, caption, itemData)
                                      QtGui.QPixmap(PICSCOINS + file + "-1.png", "PNG")]) # coins images saved directly into combobox itemData
                                                                                          # as list where 0 - HEAD, 1 - TAIL
                
    def change_coin(self, index):
        self.img.setPixmap(self.comboBox.itemData(index)[0])

    def getRandom(self):
        self.result = self.master.random.integers(num=1, min=0, max=1, col=1, base='10', format='plain', rnd='new')

    def errorHandler(self):
        if self.error:
            QtGui.QMessageBox.critical(
                self, "Oops!...", self.error,
                buttons = QtGui.QMessageBox.Ok,
                defaultButton = QtGui.QMessageBox.Ok)
            self.hint.show()
            self.hint.setPlainText("Result is not correct!!!\nClick on coin to flip it again")
            #self.error = None
        else:
            self.master.showQuota()
            
    def log(self, error=None):
        from time import strftime
        self.master.logs.addRow(strftime("%d-%m-%Y"),
                                strftime("%H:%M:%S"),
                                self.master.random.__class__.__name__,
                                "Coin thrower",
                                error if error else "%s coin has been flipped and result - %s [%s]" % (self.comboBox.itemText(self.comboBox.currentIndex()),
                                                                                                       "HEAD" if self.result[0]=='0' else "TAIL",
                                                                                                       self.result[0]))

