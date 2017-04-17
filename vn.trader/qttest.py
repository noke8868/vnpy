# -*- coding: utf-8 -*-

import sys, os
from PyQt4.QtGui import QApplication
from PyQt4 import QtGui
from mainDialog import Ui_Dialog

class PragramLoader(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.cw = QtGui.QWidget()
        self.setCentralWidget(self.cw)
        self.ui.setupUi(self.cw)
        self.setWindowTitle(u'定时器')
        self.resize(320, 100)
        self.center()
        self.show()
        self.ui.JustButton.clicked.connect(self.loadFile)
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def getFilename(self):
        filename = 'vtMain.py'
        path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(path, filename)

    def loadFile(self):
        extra = ['default']
        fn = self.getFilename()
        if fn is None:
            return
        if sys.platform.startswith('win'):
            os.spawnl(os.P_NOWAIT, sys.executable, '"' + sys.executable + '"', '"' + fn + '"', *extra)
        else:
            os.spawnl(os.P_NOWAIT, sys.executable, sys.executable, fn, *extra)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loader = PragramLoader()
    sys.exit(app.exec_())
