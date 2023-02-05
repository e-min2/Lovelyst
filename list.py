from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QIcon

import random 

categories = []

buttonPressed = 1

positive_affirmations = ["I am successful.", 
                         "I am confident", 
                         "I am filled with focus.",
                         "I am strong.",
                         "I am inspiring people through my work."]

body_image = ["I respect my body.",
              "I am comfortable in my own skin.",
              "I take care of my body.",
              "My body is perfect for me.",
              "I give my body what it needs."]

anxiety = ["I am safe and in control.",
           "I have survived my anxiety before. I will survive it now.",
           "I act with confidence because I know what I am doing.",
           "I am capable and prepared.",
           "This feeling is only temporary."]

personal_growth = ["I'm not stopping until I'm the best I can be.",
           "Challenges won't hold me down.",
           "I am improving for me.",
           "There are always opportunities for me to grow.",
           "Everything I need for success is already here."]

happiness = ["I am creating happiness within myself.",
           "I deserve to be happy.",
           "I am vigorous, energetic, and full of vitality.",
           "I am cultivating a beautiful life free of stress, worries, or fear.",
           "I am proud of my journey and how far I've come."]


class Ui_Widget(object):

    def setupUi(self, Widget):
        Widget.setObjectName("LoveLyst")
        Widget.resize(750, 491)

        self.msgLabel = QLabel("", parent=Widget)
        self.msgLabel.move(540, 240)
        
        self.line_2 = QtWidgets.QFrame(parent=Widget)
        self.line_2.setGeometry(QtCore.QRect(0, 190, 771, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 70, 671, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.affirm = {'positive thinking': 0, 'body image': 0,
            'anxiety': 0, 'personal growth': 0, 'happiness': 0}
        
        self.checkBox_4 = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_2.addWidget(self.checkBox_4)

        self.checkBox_4.stateChanged.connect(self.checkedPositive)
        
        self.checkBox_5 = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_2.addWidget(self.checkBox_5)

        self.checkBox_5.stateChanged.connect(self.checkedBody)
        
        self.checkBox_6 = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_2.addWidget(self.checkBox_6)

        self.checkBox_6.stateChanged.connect(self.checkedAnxiety)
        
        self.checkBox_11 = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        self.checkBox_11.setObjectName("checkBox_11")
        self.horizontalLayout_2.addWidget(self.checkBox_11)

        self.checkBox_11.stateChanged.connect(self.checkedPersonal)
        
        self.checkBox_12 = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        self.checkBox_12.setObjectName("checkBox_12")
        self.horizontalLayout_2.addWidget(self.checkBox_12)

        self.checkBox_12.stateChanged.connect(self.checkedHappy)
        
        self.line = QtWidgets.QFrame(parent=Widget)
        self.line.setGeometry(QtCore.QRect(0, 130, 771, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        
        self.textBrowser = QtWidgets.QTextBrowser(parent=Widget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 20, 181, 41))
        self.textBrowser.setObjectName("textBrowser")
        
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(410, 170, 101, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget, clicked=lambda: self.surprise())
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.verticalLayout.addWidget(self.pushButton_3)
        
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget, clicked=lambda: self.clear_it())
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.verticalLayout.addWidget(self.pushButton_2)
        
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget, clicked=lambda: self.delete_it())
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.verticalLayout.addWidget(self.pushButton_4)
        
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget, clicked=lambda: self.add_it())
        self.pushButton_5.setObjectName("pushButton_5")
        
        self.verticalLayout.addWidget(self.pushButton_5)
        
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=Widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 150, 671, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
       
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.horizontalLayoutWidget_2)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_4.addWidget(self.textBrowser_2)
       
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=Widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 210, 371, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
       
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
       
        self.listWidget = QtWidgets.QListWidget(parent=self.verticalLayoutWidget_2)
        self.listWidget.setObjectName("listWidget")
       
        self.verticalLayout_3.addWidget(self.listWidget)
       
        self.lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
       
        self.verticalLayout_3.addWidget(self.lineEdit)

        def checkButton():
            if (buttonPressed == 1):
                select_category = random.randint(0, len(categories)-1) 
                select_affirmation = random.randint(0, 4)
                self.textBrowser_2.setPlainText(categories[select_category][select_affirmation])

        self.pushButton.clicked.connect(checkButton)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def checkedPositive(self, checked):
        if checked:
            self.affirm['positive thinking'] = 1
            categories.append(positive_affirmations)
        else:
            self.affirm['positive thinking'] = 0
        self.show()

    def checkedBody(self, checked):
        if checked:
            self.affirm['body image'] = 1
            categories.append(body_image)
        else:
            self.affirm['body image'] = 0
        self.show()

    def checkedAnxiety(self, checked):
        if checked:
            self.affirm['anxiety']= 1
            categories.append(anxiety)
        else:
            self.affirm['anxiety']= 0
        self.show()

    def checkedPersonal(self, checked):
        if checked:
            self.affirm['personal growth']= 1
            categories.append(personal_growth)
        else:
            self.affirm['personal growth']= 0
        self.show()

    def checkedHappy(self, checked):
        # print("made it")
        if checked:
            self.affirm['happiness']= 1
            categories.append(happiness)
        else:
            self.affirm['happiness']= 0
        self.show()

    def show(self):
        checkedlangs =', '.join([key for key in self.affirm.keys()
                                         if self.affirm[key]== 1])

        self.textBrowser_2.setText("You are getting affirmatons on " + checkedlangs)

    def add_it(self):
        entry = self.lineEdit.text()
        self.listWidget.addItem(entry)
        self.lineEdit.setText("")
        
    def delete_it(self):
        clicked = self.listWidget.currentRow()
        self.listWidget.takeItem(clicked)
    
    def clear_it(self):
        self.listWidget.clear()
    
    def surprise(self):
        if self.msgLabel.text():
            self.msgLabel.setText("")
        else:
            self.msgLabel.setText("<3 <3 HackViolet2023 <3 <3")
            self.msgLabel.adjustSize()

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))

        self.checkBox_4.setText(_translate("Widget", "Positive Thinking"))
        self.checkBox_5.setText(_translate("Widget", "Body Image"))
        self.checkBox_6.setText(_translate("Widget", "Anxiety"))
        self.checkBox_11.setText(_translate("Widget", "Personal Growth"))
        self.checkBox_12.setText(_translate("Widget", "Happiness"))
        self.textBrowser.setHtml(_translate("Widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700;\">Hello there!</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Widget", "Surprise!"))
        self.pushButton_2.setText(_translate("Widget", "Clear List"))
        self.pushButton_4.setText(_translate("Widget", "Delete Item"))
        self.pushButton_5.setText(_translate("Widget", "Add Item"))
        self.textBrowser_2.setHtml(_translate("Widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Would you like an affirmation? Check at least one box to get one. Then, hit the New Affirmation button.</p></body></html>"))
        self.pushButton.setText(_translate("Widget", "New Affirmation"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    app.setWindowIcon(QtGui.QIcon('heart.png'))
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec())
