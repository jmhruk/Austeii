from PyQt5 import QtCore, QtGui, QtWidgets
import wikipedia
import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):from PyQt5 import QtCore, QtGui, QtWidgets
import wikipedia
import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(988, 582)
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mTitle = QtWidgets.QLabel(self.centralwidget)
        self.mTitle.setGeometry(QtCore.QRect(280, 10, 411, 131))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.mTitle.setFont(font)
        self.mTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.mTitle.setObjectName("mTitle")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 220, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.askLabel = QtWidgets.QLabel(self.centralwidget)
        self.askLabel.setGeometry(QtCore.QRect(310, 180, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.askLabel.setFont(font)
        self.askLabel.setTextFormat(QtCore.Qt.AutoText)
        self.askLabel.setScaledContents(False)
        self.askLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.askLabel.setWordWrap(True)
        self.askLabel.setOpenExternalLinks(False)
        self.askLabel.setObjectName("askLabel")
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.resultBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.resultBox.setEnabled(False)
        self.resultBox.setGeometry(QtCore.QRect(250, 330, 471, 161))
        self.resultBox.setDocumentTitle("")
        self.resultBox.setReadOnly(True)
        self.resultBox.setPlainText("")
        self.resultBox.setBackgroundVisible(False)
        self.resultBox.setObjectName("resultBox")


        def search():
            print("Hello")  

            info = self.lineEdit.text().lower()

            if info == "":
                self.resultBox.setEnabled(False)

            else:

                if info.startswith("who is "):
                    info = info.removeprefix("who is ")

                    if info.startswith("the "):
                        try:
                            result = wikipedia.summary(info, auto_suggest=False, sentences=1)
                        except:
                            result = "Sorry, I couldn't find any information on this topic.\nTry using the prefix: 'what', 'why', 'who' "

                    else:
                        try:
                            result = wikipedia.summary(info, auto_suggest=False, sentences=1)
                        except:
                            result = "Sorry, I couldn't find any information on this topic.\nTry using the prefix: 'what', 'why', 'who' "


                elif info.startswith("what is "):
                    info = info.removeprefix("what is ")

                    if info.startswith("an "):
                        info = info.removeprefix("an ")
                        try:
                            result = wikipedia.summary(info, auto_suggest=False, sentences=1)
                        except:
                            result = "Sorry, I couldn't find any information on this topic.\nTry using the prefix: 'what', 'why', 'who' "

                    elif info.startswith("a "):
                        info = info.removeprefix("a ")
                        try:
                            result = wikipedia.summary(info, auto_suggest=False, sentences=1)
                        except:
                            result = "Sorry, I couldn't find any information on this topic.\nTry using the prefix: 'what', 'why', 'who' "
                    
                    elif info.startswith("the "):
                        info = info.removeprefix("the ")
                        try:
                            result = wikipedia.summary(info, auto_suggest=False, sentences=1)
                        except:
                            result = "Sorry, I couldn't find any information on this topic.\nTry using the prefix: 'what', 'why', 'who' "

                    else:
                        try:
                            result = wikipedia.summary(info, auto_suggest=False, sentences=1)
                        except:
                            result = "Sorry, I couldn't find any information on this topic.\nTry using the prefix: 'what', 'why', 'who' "
            

                #elif info.startswith("when"):
                 #   info = info.removeprefix("when")
                  #  print(info)
                   # result = wikipedia.summary(info, auto_suggest=False, sentences=1)

                elif info.startswith("why"):
                    info = info.removeprefix("why")
            
                    try:
                        result = wikipedia.summary(info, auto_suggest=False, sentences=1)
                    except:
                        result = "Sorry, I couldn't find any information on this topic.\nTry using the prefix: 'what', 'why', 'who' "



                else:
                    try:
                        result = wikipedia.summary(info, auto_suggest=False, sentences=1)
                    except:
                        result = "Sorry, I couldn't find any information on this topic.\nTry using the prefix: 'what', 'why', 'who' "

                #special tags
                if info == "what is the time":
                    result = "The time is " + datetime.now().strftime('%I:%M %p')



                print(result)  
                self.resultBox.setEnabled(True)
                self.resultBox.setPlainText(result)
                
            return
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 270, 141, 41))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(search)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 988, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Help_Page = QtWidgets.QAction(MainWindow)
        self.actionOpen_Help_Page.setObjectName("actionOpen_Help_Page")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuHelp.addAction(self.actionOpen_Help_Page)
        self.menuHelp.addAction(self.actionQuit)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Austei - AI"))
        self.mTitle.setText(_translate("MainWindow", "Austei"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Type in here"))
        self.askLabel.setText(_translate("MainWindow", "Ask me anything..."))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_Help_Page.setText(_translate("MainWindow", "Open Help Page"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())