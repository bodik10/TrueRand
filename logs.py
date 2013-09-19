from PyQt4 import QtCore, QtGui
from datetime import datetime, timedelta
import pickle

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(716, 321)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.comboLogPeriod = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboLogPeriod.sizePolicy().hasHeightForWidth())
        self.comboLogPeriod.setSizePolicy(sizePolicy)
        self.comboLogPeriod.setObjectName(_fromUtf8("comboLogPeriod"))
        self.comboLogPeriod.addItem(_fromUtf8(""), 'today')
        self.comboLogPeriod.addItem(_fromUtf8(""), timedelta(days=7))
        self.comboLogPeriod.addItem(_fromUtf8(""), timedelta(days=31))
        self.comboLogPeriod.addItem(_fromUtf8(""), timedelta(days=90))
        self.comboLogPeriod.addItem(_fromUtf8(""), timedelta(days=180))
        self.comboLogPeriod.addItem(_fromUtf8(""), timedelta(days=366))
        self.comboLogPeriod.addItem(_fromUtf8(""), None)
        self.horizontalLayout.addWidget(self.comboLogPeriod)
        self.btnLogSave = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLogSave.sizePolicy().hasHeightForWidth())
        self.btnLogSave.setSizePolicy(sizePolicy)
        self.btnLogSave.setObjectName(_fromUtf8("btnLogSave"))
        self.horizontalLayout.addWidget(self.btnLogSave)
        self.btnLogClear = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLogClear.sizePolicy().hasHeightForWidth())
        self.btnLogClear.setSizePolicy(sizePolicy)
        self.btnLogClear.setObjectName(_fromUtf8("btnLogClear"))
        self.horizontalLayout.addWidget(self.btnLogClear)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listLog = QtGui.QListWidget(Form)
        self.listLog.setMinimumSize(QtCore.QSize(0, 150))
        self.listLog.setObjectName(_fromUtf8("listLog"))
        self.listLog.setFont(QtGui.QFont("Courier"))
        self.verticalLayout.addWidget(self.listLog)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Show logs for:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLogPeriod.setItemText(0, QtGui.QApplication.translate("Form", "Today", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLogPeriod.setItemText(1, QtGui.QApplication.translate("Form", "Week", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLogPeriod.setItemText(2, QtGui.QApplication.translate("Form", "Month", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLogPeriod.setItemText(3, QtGui.QApplication.translate("Form", "3 Months", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLogPeriod.setItemText(4, QtGui.QApplication.translate("Form", "6 Months", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLogPeriod.setItemText(5, QtGui.QApplication.translate("Form", "Year", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLogPeriod.setItemText(6, QtGui.QApplication.translate("Form", "All period", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLogSave.setText(QtGui.QApplication.translate("Form", "Save Logs", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLogClear.setText(QtGui.QApplication.translate("Form", "Clear Logs", None, QtGui.QApplication.UnicodeUTF8))

def formatRow(args):
    string = "{0:<12}{1:<13}{2:<18}{3:<30}{4}".format(*args) # make columns - date | time | engine | module | result
    return string.replace("\n", " ")
    
class Log(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        # load datafrom PKL file
        try:
            self.logfile = open('log.pkl', 'rb')
            self.log = pickle.load(self.logfile)
            self.logfile.close()
        except (IOError, EOFError):
            self.log = []

        
        self.comboLogPeriod.activated["int"].connect(self.setLogPeriod)
        self.btnLogClear.clicked.connect(self.clearLog)
        self.btnLogSave.clicked.connect(self.saveLog)
        
        self.setLogPeriod(self.comboLogPeriod.currentIndex())

    def setLogPeriod(self, index):
        today = datetime.now() # datatime object
        period = self.comboLogPeriod.itemData(index) # period saves in comboBox itemData as timedelta(days=..)
        
        if period is None: # show all logs
            self.currentViewList = self.log[:]
        else:
            self.currentViewList = []
            for row in self.log:
                date = datetime.strptime(row[0], "%d-%m-%Y") # datatime object
                if period == 'today' and date.date() == today.date():
                    self.currentViewList.append(row)
                elif isinstance(period, timedelta) and date >= today - period:
                    self.currentViewList.append(row)
        self.showList()
    
    def showList(self):
        self.listLog.clear()
        if not self.currentViewList: return
        
        # in listLog apear only records from self.currentViewList not from self.log
        self.listLog.addItems(list(map(formatRow, self.currentViewList)))
        self.listLog.scrollToItem(self.listLog.item(self.listLog.count()-1), hint=QtGui.QAbstractItemView.PositionAtTop)
        self.listLog.setCurrentItem(self.listLog.item(self.listLog.count()-1))

    def addRow(self, *args):
        self.log.append(list(args))
        self.currentViewList.append(list(args))
        self.showList()
        
    def endLogging(self):
        # save data to PKL file
        self.logfile = open('log.pkl', 'wb')
        pickle.dump(self.log, self.logfile)
        self.logfile.close()

    def saveLog(self):
        res = "\n".join([",".join(row) for row in self.currentViewList])
        if len(res) != 0:
            path = QtGui.QFileDialog.getSaveFileName(
                parent=self, caption="Save log", directory=QtCore.QDir.currentPath(),
                filter="CSV-files (*.csv)")
            try:    open(path, "w+").write(res)
            except: pass
        
    def clearLog(self):
        confirm = QtGui.QMessageBox.question(
            self, "Clear entire log", "Are you really want to wipe all logs?",
            buttons = QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, defaultButton = QtGui.QMessageBox.No)

        if confirm == QtGui.QMessageBox.Yes:
            import os
            if os.path.isfile("log.pkl"):
                os.remove("log.pkl")
                self.log = self.currentViewList = []
                self.listLog.clear()
