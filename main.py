import subprocess
import re
from PIL import Image, ImageDraw, ImageFont
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
        output = subprocess.check_output("ping -c 4 8.8.8.8", shell=True)
        output = output.decode("utf-8")  # Convert bytes to string

        times = re.findall("time=\d+\.?\d*", output)

        times = [float(t.split("=")[1]) for t in times]
        average = int(sum(times) / len(times))

        print("Average: ", average)
        if average < 80:
            font_color = (0, 255, 0)  # green
        elif 80 <= average <= 150:
            font_color = (255, 255, 0)  # yellow
        else:
            font_color = (255, 0, 0)  # red

        if average < 100:
            fsize = 240
        elif 100 <= average < 1000:
            fsize = 180
        else:
            fsize = 120
        # Create an image
        img = Image.new("RGBA", (300, 300), color=(0, 0, 0, 0))  # bg color
        font_size = ImageFont.truetype("/usr/share/fonts/X11/Type1/c0632bt_.pfb", fsize)
        d = ImageDraw.Draw(img)
        d.text(
            (5, 5),
            str(average),
            fill=font_color,
            align="center",
            font=font_size,
        )  # text color

        img.save("average.png")  

        self.setIcon(QtGui.QIcon("average.png")) 
def main():
    app = QtWidgets.QApplication([])
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("average.png"), w)
    tray_icon.show()
    app.exec()


if __name__ == "__main__":
    main()
