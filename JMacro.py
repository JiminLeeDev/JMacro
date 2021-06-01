import json 
import sys
import os   
import pyautogui

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget

class ConfigureManager():
    def __init__(self):
        self.configures = {}
        
    def SaveConfigureFile(self):
        f = open("configures.json", "w")
        json.dump(self.configures, f, indent='\t')
        f.close()

    def CreateConfigureFile(self):
        self.configures = {    
            'ClickInterval': 1000,
            'ImageAddress':[
                'Cap 2021-06-02 02-15-00-602.png'
            ]
        }

    def LoadConfigureFile(self):
        f = open("configures.json", "r")
        jsonData = f.read().replace(' ', '').replace('\n','').replace('\t','')
        f.close()
        self.configures = json.loads(jsonData)



class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.configureManager = ConfigureManager()
        self.configureManager.CreateConfigureFile()
        self.initUI()
        self.setTimer()
        
    def initUI(self):
        self.configureSaveBtn = QPushButton(self)
        self.configureSaveBtn.setText('save configure')
        self.configureSaveBtn.setGeometry(10,10,100,30)   
        self.configureSaveBtn.clicked.connect(self.configureManager.SaveConfigureFile)   

        self.setWindowTitle('JMacro')
        self.setGeometry(300,300,500,500) 
        self.show()

    def setTimer(self):
        self.timer = QTimer()
        self.timer.setInterval(self.configureManager.configures['ClickInterval'])
        self.timer.timeout.connect(self.Macro)
        self.timer.start()

    def Macro(self):
        for name in self.configureManager.configures['ImageAddress']:
            name = "resource/" + name

            if os.path.isfile(name):
                btnLocation = pyautogui.locateOnScreen(name)

                if btnLocation != None:
                    pyautogui.doubleClick(btnLocation)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
