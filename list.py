
import random
from PyQt6 import QtCore, QtGui, QtWidgets


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
        Widget.setObjectName("Widget")
        Widget.resize(718, 600)
        self.textBrowser = QtWidgets.QTextBrowser(parent=Widget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 201, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.line = QtWidgets.QFrame(parent=Widget)
        self.line.setGeometry(QtCore.QRect(-10, 130, 771, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 611, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.affirm = {'positive thinking': 0, 'body image': 0,
            'anxiety': 0, 'personal growth': 0, 'happiness': 0}

        self.checkBox_3 = QtWidgets.QCheckBox(
            parent=self.horizontalLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout.addWidget(self.checkBox_3)

        self.checkBox_3.stateChanged.connect(self.checkedPositive)

        self.checkBox_2 = QtWidgets.QCheckBox(
            parent=self.horizontalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)

        self.checkBox_2.stateChanged.connect(self.checkedBody)

        self.checkBox = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)

        self.checkBox.stateChanged.connect(self.checkedAnxiety)

        self.checkBox_10 = QtWidgets.QCheckBox(
            parent=self.horizontalLayoutWidget)
        self.checkBox_10.setObjectName("checkBox_10")
        self.horizontalLayout.addWidget(self.checkBox_10)

        self.checkBox_10.stateChanged.connect(self.checkedPersonal)

        self.checkBox_9 = QtWidgets.QCheckBox(
            parent=self.horizontalLayoutWidget)
        self.checkBox_9.setObjectName("checkBox_9")
        self.horizontalLayout.addWidget(self.checkBox_9)

        self.checkBox_9.stateChanged.connect(self.checkedHappy)

        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=Widget)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 150, 541, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")

        def checkButton():
            if (buttonPressed == 1):
                select_category = random.randint(0, len(categories)-1) 
                select_affirmation = random.randint(0, 4)
                self.textBrowser_2.setText(categories[select_category][select_affirmation])
                categories = []
           

        self.line_2 = QtWidgets.QFrame(parent=Widget)
        self.line_2.setGeometry(QtCore.QRect(-10, 190, 771, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(parent=Widget)
        self.label.setGeometry(QtCore.QRect(20, 210, 91, 20))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 540, 83, 29))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 240, 271, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_6 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout.addWidget(self.checkBox_8)
        self.checkBox_12 = QtWidgets.QCheckBox(
            parent=self.verticalLayoutWidget)
        self.checkBox_12.setObjectName("checkBox_12")
        self.verticalLayout.addWidget(self.checkBox_12)
        self.checkBox_11 = QtWidgets.QCheckBox(
            parent=self.verticalLayoutWidget)
        self.checkBox_11.setObjectName("checkBox_11")
        self.verticalLayout.addWidget(self.checkBox_11)
        self.pushButton_3 = QtWidgets.QPushButton(parent=Widget)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 540, 83, 29))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=Widget)
        self.textBrowser_3.setGeometry(QtCore.QRect(440, 280, 171, 191))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.pushButton = QtWidgets.QPushButton(parent=Widget)
        self.pushButton.setGeometry(QtCore.QRect(570, 150, 121, 29))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(checkButton) 

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

   # 'positive thinking':0, 'body image':0, 'anxiety':0, 'personal growth':0, 'happiness':0

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
        if checked:
            self.affirm['happiness']= 1
            categories.append(happiness)
        else:
            self.affirm['happiness']= 0
        self.show()

            # For showing updated list of all selected languages.    

    def show(self):
        checkedlangs =', '.join([key for key in self.affirm.keys()
                                         if self.affirm[key]== 1])

        # Updates message having list of all selected languages.
        self.textBrowser_2.setText("You know "+checkedlangs)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.textBrowser.setHtml(_translate("Widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700;\">Hello there!</span></p></body></html>"))
        self.checkBox_3.setText(_translate("Widget", "Positive Thinking"))
        self.checkBox_2.setText(_translate("Widget", "Body Image"))
        self.checkBox.setText(_translate("Widget", "Anxiety"))
        self.checkBox_10.setText(_translate("Widget", "Personal Growth"))
        self.checkBox_9.setText(_translate("Widget", "Happiness"))
        self.textBrowser_2.setHtml(_translate("Widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Would you like an affirmation? Check at least one box to get one.</p></body></html>"))
        self.label.setText(_translate("Widget", "Today\'s Goals"))
        self.pushButton_2.setText(_translate("Widget", "Clear List"))
        self.checkBox_6.setText(_translate("Widget", "drink water"))
        self.checkBox_7.setText(_translate("Widget", "skip school"))
        self.checkBox_8.setText(_translate("Widget", "buy milk"))
        self.checkBox_12.setText(_translate("Widget", "take nap"))
        self.checkBox_11.setText(_translate("Widget", "scream"))
        self.pushButton_3.setText(_translate("Widget", "Surprise!"))
        self.textBrowser_3.setHtml(_translate("Widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\',\'sans-serif\'; font-size:16px; color:#000000; background-color:#ffffff;\">　　　　　  /＞----フ</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\',\'sans-serif\'; font-size:16px; color:#000000; background-color:#ffffff;\">　　　　　 | 　 _　 _ l</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\',\'sans-serif\'; font-size:16px; color:#000000; background-color:#ffffff;\">　 　　　／` ミ＿xノ</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\',\'sans-serif\'; font-size:16px; color:#000000; background-color:#ffffff;\">　　 　 /　　　         |</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\',\'sans-serif\'; font-size:16px; color:#000000; background-color:#ffffff;\">　　　 /　   ヽ　　   ﾉ</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\',\'sans-serif\'; font-size:16px; color:#000000; background-color:#ffffff;\">　 　 │　    　 |　|　|</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\',\'sans-serif\'; font-size:16px; color:#000000; background-color:#ffffff;\">　／￣|　　   |　|　|</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\',\'sans-serif\'; font-size:16px; color:#000000; background-color:#ffffff;\">　| (￣ヽ＿_ヽ_)__)</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\',\'sans-serif\'; font-size:16px; color:#000000; background-color:#ffffff;\">　＼二つ</span></p></body></html>"))
        self.pushButton.setText(_translate("Widget", "New Affirmation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec())
