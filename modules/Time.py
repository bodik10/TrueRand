from PyQt4 import QtCore, QtGui
from config import *
from myThread import MyThread
from .resultTableClass import ResultTable

####### BEGIN UI code
# code generated by pyuic.bat (pyuic.bat -x spam.ui -o spam.py)
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
class Ui_MyWidget(object):
    def setupUi(self, MyWidget):
        MyWidget.setObjectName(_fromUtf8("MyWidget"))
        MyWidget.resize(802, 634)
        self.horizontalLayout = QtGui.QHBoxLayout(MyWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(MyWidget)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(20, 458, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.groupParam = QtGui.QGroupBox(MyWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupParam.sizePolicy().hasHeightForWidth())
        self.groupParam.setSizePolicy(sizePolicy)
        self.groupParam.setMinimumSize(QtCore.QSize(300, 0))
        self.groupParam.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupParam.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupParam.setFlat(False)
        self.groupParam.setCheckable(False)
        self.groupParam.setObjectName(_fromUtf8("groupParam"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupParam)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkIsSeconds = QtGui.QCheckBox(self.groupParam)
        self.checkIsSeconds.setChecked(True)
        self.checkIsSeconds.setObjectName(_fromUtf8("checkIsSeconds"))
        self.horizontalLayout_2.addWidget(self.checkIsSeconds)
        self.checkIsMili = QtGui.QCheckBox(self.groupParam)
        self.checkIsMili.setObjectName(_fromUtf8("checkIsMili"))
        self.horizontalLayout_2.addWidget(self.checkIsMili)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupParam)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.timeEditFrom = QtGui.QTimeEdit(self.groupParam)
        self.timeEditFrom.setObjectName(_fromUtf8("timeEditFrom"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.timeEditFrom)
        self.label_2 = QtGui.QLabel(self.groupParam)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.timeEditTo = QtGui.QTimeEdit(self.groupParam)
        self.timeEditTo.setTime(QtCore.QTime(23, 59, 59, 999))
        self.timeEditTo.setObjectName(_fromUtf8("timeEditTo"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.timeEditTo)
        self.label_3 = QtGui.QLabel(self.groupParam)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.comboTimeInterval = QtGui.QComboBox(self.groupParam)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboTimeInterval.sizePolicy().hasHeightForWidth())
        self.comboTimeInterval.setSizePolicy(sizePolicy)
        self.comboTimeInterval.setObjectName(_fromUtf8("comboTimeInterval"))
        self.comboTimeInterval.addItem(_fromUtf8(""), None)
        self.comboTimeInterval.addItem(_fromUtf8(""), 1)
        self.comboTimeInterval.addItem(_fromUtf8(""), 2)
        self.comboTimeInterval.addItem(_fromUtf8(""), 3)
        self.comboTimeInterval.addItem(_fromUtf8(""), 5)
        self.comboTimeInterval.addItem(_fromUtf8(""), 10)
        self.comboTimeInterval.addItem(_fromUtf8(""), 15)
        self.comboTimeInterval.addItem(_fromUtf8(""), 20)
        self.comboTimeInterval.addItem(_fromUtf8(""), 30)
        self.comboTimeInterval.addItem(_fromUtf8(""), 60)
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboTimeInterval)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.spinNum = QtGui.QSpinBox(self.groupParam)
        self.spinNum.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinNum.setMinimum(1)
        self.spinNum.setMaximum(10000)
        self.spinNum.setObjectName(_fromUtf8("spinNum"))
        self.verticalLayout_2.addWidget(self.spinNum)
        self.btnGenerate = QtGui.QPushButton(self.groupParam)
        self.btnGenerate.setObjectName(_fromUtf8("btnGenerate"))
        self.verticalLayout_2.addWidget(self.btnGenerate)
        self.gridLayout.addWidget(self.groupParam, 0, 0, 1, 1)
        
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(MyWidget)
        QtCore.QMetaObject.connectSlotsByName(MyWidget)

    def retranslateUi(self, MyWidget):
        MyWidget.setWindowTitle(QtGui.QApplication.translate("MyWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupParam.setTitle(QtGui.QApplication.translate("MyWidget", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.checkIsSeconds.setText(QtGui.QApplication.translate("MyWidget", "Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.checkIsMili.setText(QtGui.QApplication.translate("MyWidget", "Miliseconds", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MyWidget", "Time between:", None, QtGui.QApplication.UnicodeUTF8))
        self.timeEditFrom.setDisplayFormat(QtGui.QApplication.translate("MyWidget", "H:mm:ss", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MyWidget", "and:", None, QtGui.QApplication.UnicodeUTF8))
        self.timeEditTo.setDisplayFormat(QtGui.QApplication.translate("MyWidget", "H:mm:ss", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MyWidget", "Use intervals of:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboTimeInterval.setItemText(0, QtGui.QApplication.translate("MyWidget", "none", None, QtGui.QApplication.UnicodeUTF8))
        self.comboTimeInterval.setItemText(1, QtGui.QApplication.translate("MyWidget", "1 min", None, QtGui.QApplication.UnicodeUTF8))
        self.comboTimeInterval.setItemText(2, QtGui.QApplication.translate("MyWidget", "2 min", None, QtGui.QApplication.UnicodeUTF8))
        self.comboTimeInterval.setItemText(3, QtGui.QApplication.translate("MyWidget", "3 min", None, QtGui.QApplication.UnicodeUTF8))
        self.comboTimeInterval.setItemText(4, QtGui.QApplication.translate("MyWidget", "5 min", None, QtGui.QApplication.UnicodeUTF8))
        self.comboTimeInterval.setItemText(5, QtGui.QApplication.translate("MyWidget", "10 min", None, QtGui.QApplication.UnicodeUTF8))
        self.comboTimeInterval.setItemText(6, QtGui.QApplication.translate("MyWidget", "15 min", None, QtGui.QApplication.UnicodeUTF8))
        self.comboTimeInterval.setItemText(7, QtGui.QApplication.translate("MyWidget", "20 min", None, QtGui.QApplication.UnicodeUTF8))
        self.comboTimeInterval.setItemText(8, QtGui.QApplication.translate("MyWidget", "30 min", None, QtGui.QApplication.UnicodeUTF8))
        self.comboTimeInterval.setItemText(9, QtGui.QApplication.translate("MyWidget", "60 min", None, QtGui.QApplication.UnicodeUTF8))
        self.spinNum.setPrefix(QtGui.QApplication.translate("MyWidget", "amount of times - ", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGenerate.setText(QtGui.QApplication.translate("MyWidget", "Generate", None, QtGui.QApplication.UnicodeUTF8))

####### END UI code
   
class MyWidget(QtGui.QWidget, Ui_MyWidget, ResultTable):
    def __init__(self, parent=None, master=None):
        QtGui.QWidget.__init__(self, parent)
        self.master = master
        self.error = self.result = self.model = None
        
        self.column = 1
        
        self.setupUi(self)          # set UI (method from Ui_MyWidget)
        ResultTable.__init__(self)  # set UI for result group widget (result table etc...)
        
        self.btnGenerate.clicked.connect(self.generate)
        self.checkIsSeconds.toggled.connect(self.allowSeconds)
        self.checkIsMili.toggled.connect(self.allowMiliseconds)
                
        self.thread = MyThread(self, self.getRandom)
        self.thread.finished.connect(self.errorHandler)



    # secToTime(64835555, True, True)   -> QTime(18, 0, 35, 555)
    # secToTime(64835, True, False)     -> QTime(18, 0, 35)
    # secToTime(1080, False, False)     -> QTime(18, 0)
    def secToTime(self, units, isSeconds=True, isMilisec=True):   # miliseconds to QTime (65482833 -> QTime(18, 11, 22, 833) 18:11:22.833)
        hour = min = sec = msec = 0
        if isMilisec:
            msec = units % 1000
            units /= 1000
        if isSeconds:
            sec = units % 60
            units /= 60
        min = units % 60
        units /= 60
        hour = units
        return QtCore.QTime(hour, min, sec, msec)

    # timeToSec(QTime(18, 0, 35, 555), True, True)      -> 64835555
    # timeToSec(QTime(18, 0, 35, 555), True, False)     -> 64835
    # timeToSec(QTime(18, 0, 35, 555), False, False)    -> 1080
    def timeToSec(self, qTime, isSeconds=True, isMilisec=True):     # QTime to miliseconds (QTime(23, 59, 59, 999) -> 86399999)
        if isSeconds:
            if isMilisec:
                return (qTime.hour()*3600 + qTime.minute()*60 + qTime.second())*1000 + qTime.msec()
            return qTime.hour()*3600 + qTime.minute()*60 + qTime.second()
        return qTime.hour()*60 + qTime.minute()

    # formatTime(QTime(18, 0, 35, 555)) -> 18:00:35.555
    # formatTime(QTime(18, 0))          -> 18:00
    def formatTime(self, qTime):
        format = self.timeEditFrom.displayFormat()
        return qTime.toString(format)
        

    def allowSeconds(self, isChecked):
        self.checkIsMili.setCheckState(QtCore.Qt.Unchecked)
        self.checkIsMili.setDisabled(not isChecked)
        if isChecked:
            self.timeEditFrom.setDisplayFormat("H:mm:ss")
            self.timeEditTo.setDisplayFormat("H:mm:ss")
        else:
            self.timeEditFrom.setDisplayFormat("H:mm")
            self.timeEditTo.setDisplayFormat("H:mm")
        
    def allowMiliseconds(self, isChecked):
        if isChecked:
            self.timeEditFrom.setDisplayFormat("H:mm:ss.zzz")
            self.timeEditTo.setDisplayFormat("H:mm:ss.zzz")
        else:
            self.timeEditFrom.setDisplayFormat("H:mm:ss")
            self.timeEditTo.setDisplayFormat("H:mm:ss")
        
    def generate(self):       
        self.btnGenerate.setDisabled(True)
        self.thread.start()
        
    def getRandom(self):
        num = self.spinNum.value()
        isSec = self.checkIsSeconds.isChecked()
        isMsec = self.checkIsMili.isChecked()
        interval = self.comboTimeInterval.itemData(self.comboTimeInterval.currentIndex())
        timeStart   = time1 = self.timeToSec( self.timeEditFrom.time(), isSec, isMsec )
        timeEnd     = time2 = self.timeToSec( self.timeEditTo.time(), isSec, isMsec )

        if interval:
            if      isMsec: coef = interval * 60 * 1000
            elif    isSec: coef = interval * 60
            else:   coef = interval
            time1 = 0
            time2 = (timeEnd-timeStart) // coef
        
        
        result = self.master.random.integers(num=num, min=time1, max=time2,
                                             base='10', col=1, format='plain', rnd='new')                   # ['64835555', '573755', '73753'...]
        if interval:
            result = list( map(lambda x: self.secToTime(timeStart + int(x)*coef, isSec, isMsec), result) )  # [QTime(18, 0, 35, 555), QTime(01, 10, 35, 105)...]
        else:
            result = list( map(lambda x: self.secToTime(int(x), isSec, isMsec), result) )                   # [QTime(18, 0, 35, 555), QTime(01, 10, 35, 105)...]
        result = list( map(self.formatTime, result) )                                                       # ['18:00:35.555', '01:10:35.105'...]
        
        if self.checkAdd.isChecked() and type(self.result) is list:
            self.result.extend(result)
        else:
            self.result = result
        # print(self.result)
        self.makeTable()
        
        
    def log(self, error=None):
        from time import strftime
        self.master.logs.addRow(strftime("%d-%m-%Y"),
                                strftime("%H:%M:%S"),
                                self.master.random.__class__.__name__,
                                "Time Generator",
                                error if error else "Generated %s clock time(s) between %s and %s with interval %s" % (
                                    self.spinNum.value(),
                                    self.timeEditFrom.textFromDateTime(self.timeEditFrom.dateTime()),
                                    self.timeEditTo.textFromDateTime(self.timeEditTo.dateTime()),
                                    self.comboTimeInterval.currentText())
                                )
