import sys
from PyQt4 import QtCore, QtGui, uic
from snapshot import Snapshot

class SnapshotThread(QtCore.QThread):
    def run(self):
        s = Snapshot()
        print(len(s.values))

class MainWindow(QtGui.QMainWindow):
    snapshots = []

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('main.ui', self)
        QtCore.QObject.connect(self.snapshotButton,QtCore.SIGNAL("clicked()"), self.make_snapshot)


    def make_snapshot(self):
        self.st = SnapshotThread()
        self.st.start()
        # self.statusBar().showMessage('Pressed')
        # self.progressBar.setValue(self.progressBar.value() + 1)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())