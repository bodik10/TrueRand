from PyQt4 import QtCore, QtGui
from config import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class ResultTable():
    def __init__(self):
        self.groupResult = QtGui.QGroupBox(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupResult.sizePolicy().hasHeightForWidth())
        self.groupResult.setSizePolicy(sizePolicy)
        self.groupResult.setObjectName(_fromUtf8("groupResult"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupResult)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        self.tableResult = QtGui.QTableView(self.groupResult)
        self.tableResult.setSortingEnabled(True)
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableResult.sizePolicy().hasHeightForWidth())
        self.tableResult.setSizePolicy(sizePolicy)
        self.tableResult.setObjectName(_fromUtf8("tableResult"))
        self.verticalLayout.addWidget(self.tableResult)
        self.frame_2 = QtGui.QFrame(self.groupResult)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        #self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btnClear = QtGui.QPushButton(self.frame_2)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.horizontalLayout_5.addWidget(self.btnClear)
        self.btnSave = QtGui.QPushButton(self.frame_2)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.horizontalLayout_5.addWidget(self.btnSave)
        self.btnCopy = QtGui.QPushButton(self.frame_2)
        self.btnCopy.setObjectName(_fromUtf8("btnCopy"))
        self.horizontalLayout_5.addWidget(self.btnCopy)
        self.spinCol = QtGui.QSpinBox(self.frame_2)
        self.spinCol.setMinimum(1)
        self.spinCol.setMaximum(10)
        self.spinCol.setObjectName(_fromUtf8("spinCol"))
        self.horizontalLayout_5.addWidget(self.spinCol)
        self.checkAdd = QtGui.QCheckBox(self.frame_2)
        self.checkAdd.setObjectName(_fromUtf8("checkAdd"))
        self.horizontalLayout_5.addWidget(self.checkAdd)
        self.verticalLayout.addWidget(self.frame_2)
        
        self.gridLayout.addWidget(self.groupResult, 0, 1, 2, 1)

        self.groupResult.setTitle(QtGui.QApplication.translate("MyWidget", "Results", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClear.setText(QtGui.QApplication.translate("MyWidget", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSave.setText(QtGui.QApplication.translate("MyWidget", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCopy.setText(QtGui.QApplication.translate("MyWidget", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.spinCol.setPrefix(QtGui.QApplication.translate("MyWidget", "columns - ", None, QtGui.QApplication.UnicodeUTF8))
        self.checkAdd.setText(QtGui.QApplication.translate("MyWidget", "Add to the end", None, QtGui.QApplication.UnicodeUTF8))


        self.spinCol.valueChanged["int"].connect(self.changeColumn)
        self.btnClear.clicked.connect(self.clearTable)
        self.btnCopy.clicked.connect(self.copyResult)
        self.btnSave.clicked.connect(self.saveResult)
            
    def makeTable(self):        
        if not self.result: return False
        
        length = len(self.result)
        if length <= self.column:
            row = 1; col = length
        else:
            col = self.column
            row = length // col if length % col==0 else length // col + 1
            
        self.model = QtGui.QStandardItemModel(row, col)
        index = 0
        for i in range(row):
            for j in range(col):
                if index >= length: break

                # add cell to table (model)
                item = QtGui.QStandardItem("%s" % self.result[index])
                item.setEditable(False)
                item.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
                item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                self.model.setItem(i, j, item)
                
                index += 1
                
        self.tableResult.setModel(self.model) # apply Model (self.model) to View (self.tableResult)
        self.tableResult.resizeColumnsToContents()
        #self.tableResult.resizeRowsToContents()
        
    def changeColumn(self, col):
        self.column = col
        self.makeTable()

    def clearTable(self):
        if self.model:
            self.model.clear()
        self.result = None

    def formatResult(self):
        # from os import linesep 
        result = newline = ""
        for i in range(self.model.rowCount()):
            result += newline
            for j in range(self.model.columnCount()):
                result += (self.model.item(i, j).text() if self.model.item(i, j) else "") + ","
            newline = "\n"
        return result

    def copyResult(self):
        res = self.formatResult()
        if len(res) != 0:
            QtGui.qApp.clipboard().setText(res)

    def saveResult(self):
        res = self.formatResult()
        if len(res) != 0:
            path = QtGui.QFileDialog.getSaveFileName(
                parent=self, caption="Save result", directory=QtCore.QDir.currentPath(),
                filter="CSV-files (*.csv)")
            try:
                open(path, "w+").write(res)
            except:
                pass
    
    def errorHandler(self):
        if self.error:
            QtGui.QMessageBox.critical(
                self, "Oops!...", self.error,
                buttons = QtGui.QMessageBox.Ok,
                defaultButton = QtGui.QMessageBox.Ok)
            
            if not self.checkAdd.isChecked(): self.clearTable()
            self.log(error=self.error) # log into journal
            #self.error = None
        else:
            self.master.showQuota()
            self.log() # log into journal 
        self.btnGenerate.setDisabled(False)
