import json 
import sys
import os   
import pyautogui

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget

configures = {
    'ClickInterval': 1000,
    'ImageAddress':[
        'Cap 2021-06-02 02-15-00-602.png'
    ]
}

def CreateConfigureFile(jsonData):
    f = open("configures.json", "w")
    json.dump(jsonData, f, indent='\t')
    f.close()
    
def LoadConfigureFile():
    f = open("configures.json", "r")
    jsonData = f.read().replace(' ', '').replace('\n','').replace('\t','')
    f.close()
    configures = json.loads(jsonData)

CreateConfigureFile(configures)
def Macro():
    for name in configures['ImageAddress']:
        name = "resource/" + name

        if os.path.isfile(name):
            btnLocation = pyautogui.locateOnScreen(name)

            if btnLocation != None:
                pyautogui.doubleClick(btnLocation)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setTimer()
        
    def initUI(self):
        self.setWindowTitle("JMacro")
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

    def setTimer(self):
        self.timer = QTimer()
        self.timer.setInterval(configures['ClickInterval'])
        self.timer.timeout.connect(Macro)
        self.timer.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
