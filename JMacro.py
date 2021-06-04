import json
import sys
import os
import pyautogui

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QWidget


class ConfigureManager:
    def __init__(self):
        self.configures = {}

    def SaveConfigureFile(self):
        f = open("configures.json", "w")
        json.dump(self.configures, f, indent="\t")
        f.close()

    def CreateConfigureFile(self):
        self.configures = {
            "ClickInterval": 1000,
            "ImageAddress": ["Cap 2021-06-02 02-15-00-602.png"],
        }

    def LoadConfigureFile(self):
        f = open("configures.json", "r")
        jsonData = f.read().replace(" ", "").replace("\n", "").replace("\t", "")
        f.close()
        self.configures = json.loads(jsonData)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.configureManager = ConfigureManager()

        if (
            "ImageAddress" not in self.configureManager.configures.keys()
            or "ClickInterval" not in self.configureManager.configures.keys()
        ):
            self.configureManager.CreateConfigureFile()

        self.initUI()
        self.setTimer()

    def initUI(self):
        self.macroBtn = QPushButton(self)
        self.macroBtn.setText("macro on")
        self.macroBtn.setGeometry(10, 10, 120, 30)
        self.macroBtn.clicked.connect(self.MacroBtnClicked)

        self.configureSaveBtn = QPushButton(self)
        self.configureSaveBtn.setText("save configure")
        self.configureSaveBtn.setGeometry(10, 50, 120, 30)
        self.configureSaveBtn.clicked.connect(self.configureManager.SaveConfigureFile)

        self.addAddressBtn = QPushButton(self)
        self.addAddressBtn.setText("add address")
        self.addAddressBtn.setGeometry(10, 90, 120, 30)
        self.addAddressBtn.clicked.connect(self.addAddressBtnClicked)

        self.removeAddressBtn = QPushButton(self)
        self.removeAddressBtn.setText("remove address")
        self.removeAddressBtn.setGeometry(10, 130, 120, 30)
        self.removeAddressBtn.clicked.connect(self.RemoveAddressBtnClicked)

        self.addressTBox = QLineEdit(self)
        self.addressTBox.setGeometry(10, 170, 120, 30)
        self.setWindowTitle("JMacro")
        self.setGeometry(300, 300, 500, 500)
        self.show()

    def MacroBtnClicked(self):
        btn = self.sender()

        if btn.text() == "macro off":
            btn.setText("macro on")
            self.timer.stop()
        else:
            btn.setText("macro off")
            self.timer.start()

    def addAddressBtnClicked(self):
        if self.addressTBox.text().find(".") == -1:
            return

        self.configureManager.configures["ImageAddress"].append(self.addressTBox.text())
        self.configureManager.configures["ImageAddress"] = list(
            set(self.configureManager.configures["ImageAddress"])
        )

    def RemoveAddressBtnClicked(self):
        if self.addressTBox.text() in self.configureManager.configures["ImageAddress"]:
            self.configureManager.configures.pop(self.tbox.text())

    def setTimer(self):
        self.timer = QTimer()
        self.timer.setInterval(self.configureManager.configures["ClickInterval"])
        self.timer.timeout.connect(self.Macro)

    def Macro(self):
        for name in self.configureManager.configures["ImageAddress"]:
            name = "resource/" + name

            if os.path.isfile(name):
                btnLocation = pyautogui.locateOnScreen(name)

                if btnLocation != None:
                    pyautogui.doubleClick(btnLocation)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
