
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(750, 491)
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=Widget)
        self.textBrowser_3.setGeometry(QtCore.QRect(540, 240, 161, 181))
        self.textBrowser_3.setObjectName("textBrowser_3")
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
        self.checkBox_4 = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_2.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_2.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_2.addWidget(self.checkBox_6)
        self.checkBox_11 = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        self.checkBox_11.setObjectName("checkBox_11")
        self.horizontalLayout_2.addWidget(self.checkBox_11)
        self.checkBox_12 = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        self.checkBox_12.setObjectName("checkBox_12")
        self.horizontalLayout_2.addWidget(self.checkBox_12)
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
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
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

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Affirmations and stuff</p></body></html>"))
        self.pushButton.setText(_translate("Widget", "New Affirmation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec())
