from PyQt4 import QtCore, QtGui
import sys

# custom Thread class
class MyThread(QtCore.QThread):
    def __init__(self, parent=None, func=None):
        QtCore.QThread.__init__(self, parent)
        self.func = func        # this function/method is run in the thread
        self.parent = parent
        
    def run(self):
        try:
            self.func()
        except:
            # If you try to show error dialog from within the thread
            # dialog will NOT! be shown correctly
            
            # Thats why I'm using here special 'error' property
            # when thread is finished (QThread's signal 'finished'), I check this var,
            # and if it's not empty - error dialog box will be shown
            
            self.parent.error = str(sys.exc_info()[1])
        else:
            self.parent.error = None
