from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setIcon(icon)

        menu = QtWidgets.QMenu(parent)
        exit_action = menu.addAction("Exit")
        exit_action.triggered.connect(QtWidgets.qApp.quit)
        self.setContextMenu(menu)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_icon)
        self.timer.start(4500)  # Refresh every 4.5 seconds

    def update_icon(self):
        self.setIcon(
            QtGui.QIcon("/home/arush/Net_check/Net_Check/average.png")
        )  # Replace with your icon path


def main():
    app = QtWidgets.QApplication([])
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(
        QtGui.QIcon("D:/average.png"), w
    )  # Replace with your icon path
    tray_icon.show()
    app.exec()


if __name__ == "__main__":
    main()
