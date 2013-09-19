import sys

from PyQt4 import QtCore, QtGui
from config import *
from randomClasses import *
from myThread import MyThread
from logs import Log
from modules import Coin, Integers, Floats, Strings, Sequences, Time, Date

class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.n = 1
        self.error = None
        
        self.mdi_area = QtGui.QMdiArea()
        self.sb = self.statusBar()
        self.sb.label1 = QtGui.QLabel("")
        self.sb.label1.setMinimumSize(500, 20)
        self.sb.label2 = QtGui.QLabel("")
        self.sb.label1.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Sunken)
        self.sb.label2.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Sunken)
        self.sb.addWidget(self.sb.label1)
        self.sb.addWidget(self.sb.label2, 1)

        self.randomEngine = {'True Random Generator': TrueRandom(),
                             'Pseudo Random Generator': PseudoRandom()}
                                     
        self.setCentralWidget(self.mdi_area)
        self.setDockOptions(QtGui.QMainWindow.AnimatedDocks | QtGui.QMainWindow.AllowTabbedDocks)
        
        self.add_dock_widget()
        self.add_menu()
        self.add_tool_bar()
        # self.sb.showMessage("Начальный текст в строке состояния")

    def add_dock_widget(self):
        self.dw = QtGui.QDockWidget(" Logs Journal")
        self.logs = Log() # start logging
        self.dw.setWidget(self.logs)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.dw, QtCore.Qt.Vertical)

    def add_menu(self):
        self.actSep = QtGui.QAction(self)
        self.actSep.setSeparator(True)

        
        self.menuModules = QtGui.QMenu("&Modules")
        
        self.actCoin = QtGui.QAction("Coin", self)
        self.actCoin.setIcon(QtGui.QIcon(":/icons/pics/coin-icon.png"))
        self.actCoin.triggered.connect(lambda: self.on_create_sub_window(self.actCoin, Coin))
        self.menuModules.addAction(self.actCoin)
        
        self.actIntegers = QtGui.QAction("Integers", self)
        self.actIntegers.setIcon(QtGui.QIcon(":/icons/pics/integers-icon.png"))
        self.actIntegers.triggered.connect(lambda: self.on_create_sub_window(self.actIntegers, Integers))
        self.menuModules.addAction(self.actIntegers)

        self.actFloats = QtGui.QAction("Floats", self)
        self.actFloats.setIcon(QtGui.QIcon(":/icons/pics/floats-icon.png"))
        self.actFloats.triggered.connect(lambda: self.on_create_sub_window(self.actFloats, Floats))
        self.menuModules.addAction(self.actFloats)

        self.actSequences = QtGui.QAction("Sequences", self)
        self.actSequences.setIcon(QtGui.QIcon(":/icons/pics/sequences-icon.png"))
        self.actSequences.triggered.connect(lambda: self.on_create_sub_window(self.actSequences, Sequences))
        self.menuModules.addAction(self.actSequences)

        self.actStrings = QtGui.QAction("Strings", self)
        self.actStrings.setIcon(QtGui.QIcon(":/icons/pics/strings-icon.png"))
        self.actStrings.triggered.connect(lambda: self.on_create_sub_window(self.actStrings, Strings))
        self.menuModules.addAction(self.actStrings)

        self.actTime = QtGui.QAction("Time Generator", self)
        self.actTime.setIcon(QtGui.QIcon(":/icons/pics/time-icon.png"))
        self.actTime.triggered.connect(lambda: self.on_create_sub_window(self.actTime, Time))
        self.menuModules.addAction(self.actTime)

        self.actDate = QtGui.QAction("Date Generator", self)
        self.actDate.setIcon(QtGui.QIcon(":/icons/pics/date-icon.png"))
        self.actDate.triggered.connect(lambda: self.on_create_sub_window(self.actDate, Date))
        self.menuModules.addAction(self.actDate)
        
        self.menuBar().addMenu(self.menuModules)
        

        self.menuOptions = QtGui.QMenu("&Options")
        self.actGroupEngine = QtGui.QActionGroup(self)
        self.actGroupEngine.triggered["QAction *"].connect(self.changeRandomEngine)
        self.actTrue = QtGui.QAction("True Random Generator", self.actGroupEngine)
        self.actTrue.setCheckable(True)
        self.menuOptions.addAction(self.actTrue)
        self.actPseudo = QtGui.QAction("Pseudo Random Generator", self.actGroupEngine)
        self.actPseudo.setCheckable(True)
        self.menuOptions.addAction(self.actPseudo)
        self.actGroupEngine.triggered.emit(self.actTrue)
        self.actTrue.setChecked(True)
        self.menuBar().addMenu(self.menuOptions)
        
        self.menuWindow = QtGui.QMenu("&Window")
        self.actLog = QtGui.QAction("Show &Log journal", None)
        self.actLog.triggered.connect(lambda: self.dw.show())
        self.menuWindow.addAction(self.actLog)
        self.actCascade = QtGui.QAction("Casca&de", None)
        self.actCascade.triggered.connect(self.mdi_area.cascadeSubWindows)
        self.menuWindow.addAction(self.actCascade)
        self.actTile = QtGui.QAction("&Tile", None)
        self.actTile.triggered.connect(self.mdi_area.tileSubWindows)
        self.menuWindow.addAction(self.actTile)
        self.actCloseActive = QtGui.QAction("CloseActi&ve", None)
        self.actCloseActive.triggered.connect(self.mdi_area.closeActiveSubWindow)
        self.menuWindow.addAction(self.actCloseActive)
        self.actCloseAll = QtGui.QAction("Close&All", None)
        self.actCloseAll.triggered.connect(self.mdi_area.closeAllSubWindows)
        self.menuWindow.addAction(self.actCloseAll)
        self.menuBar().addMenu(self.menuWindow)

        self.menuAbout = QtGui.QMenu("About")
        self.actAbout = QtGui.QAction("About programm", None)
        self.actAbout.triggered.connect(lambda: QtGui.QMessageBox.about(self, "About programm", ABOUTPROG))
        self.menuAbout.addAction(self.actAbout)
        self.actAboutQt = QtGui.QAction("About Qt", None)
        self.actAboutQt.triggered.connect(lambda: QtGui.QMessageBox.aboutQt(self))
        self.menuAbout.addAction(self.actAboutQt)
        self.menuAbout.addAction(self.actSep)
        self.actExit = QtGui.QAction("&Exit", self)
        self.actExit.triggered.connect(QtGui.qApp.quit)
        self.menuAbout.addAction(self.actExit)
        
        self.menuBar().addMenu(self.menuAbout)

    def add_tool_bar(self):
        self.toolBar = QtGui.QToolBar("MyToolBar")
        self.toolBar.addAction(self.actCoin)
        self.toolBar.addAction(self.actIntegers)
        self.toolBar.addAction(self.actFloats)
        self.toolBar.addAction(self.actSequences)
        self.toolBar.addAction(self.actStrings)
        self.toolBar.addAction(self.actTime)
        self.toolBar.addAction(self.actDate)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actTrue)
        self.toolBar.addAction(self.actPseudo)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        
    def on_create_sub_window(self, act, module):
        ico = act.icon()
        w = module.MyWidget(master=self)
        
        sWindow = self.mdi_area.addSubWindow(w)
	# self.mdi_area.addSubWindow(sWindow)
        # sWindow = QtGui.QMdiSubWindow(self.mdi_area)
	# sWindow.setWidget(w)

        sWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        sWindow.setWindowIcon(ico)
        sWindow.setWindowTitle(act.text())
        self.n += 1
        sWindow.show()

    def changeRandomEngine(self, act):
        self.random = self.randomEngine[act.text()]
        self.sb.label1.setText("Current engine: <b>%s</b>. For change engine use <i>'Option'</i> menu" % act.text())
        
        self.showQuota()
          
    def showQuota(self):
        thread = MyThread(self, lambda: self.sb.label2.setText("Your quota (random bits for today): %s" % self.random.quota(format='plain')[0]))
        thread.finished.connect(self.errorHandler)
        thread.start()

    def errorHandler(self):
        if self.error:
            QtGui.QMessageBox.critical(
                self, "Oops!...", self.error,
                buttons = QtGui.QMessageBox.Ok,
                defaultButton = QtGui.QMessageBox.Ok)

            # when random.org is unavaible - use PseudoRandom class instead of TrueRandom
            self.actGroupEngine.triggered.emit(self.actPseudo)
            self.actPseudo.setChecked(True)
            
            self.error = None

            
import rcc

app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("TrueRand - True Random Generator Client v." + VERSION)
window.resize(1024, 768)
window.setWindowIcon(QtGui.QIcon(":/icons/pics/appicon128.png"))
app.setWindowIcon(QtGui.QIcon(":/icons/pics/appicon128.png")) 
window.show()
app.exec_()
window.logs.endLogging() # stop logging
