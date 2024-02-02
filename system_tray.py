from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import QTimer

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setIcon(icon)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_icon)
        self.timer.start(4500)  # Refresh every 4.5 seconds

    def update_icon(self):
        self.setIcon(QtGui.QIcon("D:/average.png"))

def main():
    app = QtWidgets.QApplication([])
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("D:/average.png"), w)
    tray_icon.show()
    app.exec()

if __name__ == '__main__':
    main()