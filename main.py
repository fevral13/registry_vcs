import sys
from PyQt4 import QtCore, QtGui, uic
from snapshot import Snapshot


class SnapshotThread(QtCore.QThread):
    def run(self):
        s = Snapshot()
        print(len(s.values))


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('main.ui', self)
        self.snapshotButton.clicked.connect(self.make_snapshot)
        self.snapshots_list = []
        self.commits_list = []

        self.commitsModel = QtGui.QStringListModel([])
        self.commitsView.setModel(self.commitsModel)
        self.snapshots_list.append(Snapshot())

    def make_snapshot(self):
        # self.st = SnapshotThread()
        # self.st.start()
        s = Snapshot()
        commit = s.compare_to(self.snapshots_list[-1])
        self.commits_list.append(commit)
        self.commitsModel.setStringList(self.commitsModel.stringList() + [commit.name])
        # self.statusBar().showMessage('Pressed')
        # self.progressBar.setValue(self.progressBar.value() + 1)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())