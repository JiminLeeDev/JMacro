import sys
import os
import pyautogui

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

f = open('resource/data.txt', 'r')
imageName = f.readlines()
f.close()

def Macro():
    for name in imageName: 
        name = name.split('\n')[0]

        if os.path.isfile(name):
            btnLocation = pyautogui.locateOnScreen(name)

            if btnLocation != None:
                pyautogui.doubleClick(btnLocation)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("JMacro")
        self.move(300, 300)
        self.resize(400, 200)
        self.show()
        self.timer=QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(Macro)
        self.timer.start() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
