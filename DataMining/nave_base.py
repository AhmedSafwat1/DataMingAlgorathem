# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(898, 465)
        Form.setMinimumSize(QtCore.QSize(898, 465))
        Form.setMaximumSize(QtCore.QSize(898, 465))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/safwat/Desktop/photos/hh.PNg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)

        Form.setStyleSheet("QWidget\n"
"{\n"
"   \n"
"    background-color: rgb(53, 53, 53);\n"
"    color: rgb(170, 0, 0);\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 30, 571, 61))
        self.label.setStyleSheet("QLabel\n"
"{\n"
"font: 75 italic 20pt \"Tempus Sans ITC\";\n"
" color: rgb(186, 200, 196);\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 381, 20))
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"   \n"
"    font: 75 20pt \"OCR A Extended\";\n"
"    color: rgb(85, 85, 127);\n"
"    color: rgb(85, 255, 255);\n"
"  \n"
"    color: rgb(255, 170, 0);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 280, 121, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 280, 121, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 370, 101, 31))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"   border:none;\n"
"    color: rgb(104, 0, 0);\n"
"   \n"
"    background-color: rgb(231, 231, 231);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   border:3px solid  rgb(104, 0, 0);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 240, 131, 20))
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"  \n"
"    color: rgb(85, 85, 0);\n"
"    font: 50 11pt \"MV Boli\";\n"
"    color: rgb(85, 170, 0);\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(380, 240, 121, 20))
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"  \n"
"    color: rgb(85, 85, 0);\n"
"    font: 50 11pt \"MV Boli\";\n"
"    color: rgb(85, 170, 0);\n"
"}")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 360, 201, 51))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"  \n"
"    color: rgb(30, 18, 18);\n"
"    \n"
"    font: 75 12pt \"MS Serif\";\n"
"    background-color: rgb(226, 226, 226);\n"
"   border :none;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"  border:4px solid  rgb(30, 18, 18);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/safwat/Desktop/photos/6.PNg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 360, 201, 51))
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"    font: 75 12pt \"MS Serif\";\n"
"    background-color: rgb(226, 226, 226);\n"
"   border :none;\n"
"    color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"  border:4px solid   rgb(85, 170, 255)\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/safwat/Desktop/photos/Capture.PNg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setGeometry(QtCore.QRect(660, 280, 121, 31))
        self.lineEdit_5.setStyleSheet("QLineEdit\n"
"{\n"
"  \n"
"    color: rgb(107, 0, 0);\n"
"    font: 75 11pt \"MS Reference Sans Serif\";\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(690, 240, 61, 20))
        self.label_7.setStyleSheet("QLabel\n"
"{\n"
"  \n"
"    color: rgb(85, 85, 0);\n"
"    font: 50 11pt \"MV Boli\";\n"
"    color: rgb(85, 170, 0);\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(640, 110, 231, 20))
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"  \n"
"    color: rgb(85, 85, 0);\n"
"    font: 50 11pt \"MV Boli\";\n"
"    color: rgb(85, 170, 0);\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(680, 140, 61, 20))
        self.label_6.setStyleSheet("QLabel\n"
"{\n"
"  \n"
"    color: rgb(85, 85, 0);\n"
"    font: 50 11pt \"MV Boli\";\n"
"    color: rgb(85, 170, 0);\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(780, 140, 61, 20))
        self.label_8.setStyleSheet("QLabel\n"
"{\n"
"  \n"
"    color: rgb(85, 85, 0);\n"
"    font: 50 11pt \"MV Boli\";\n"
"    color: rgb(85, 170, 0);\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(630, 170, 21, 20))
        self.label_9.setStyleSheet("QLabel\n"
"{\n"
"  \n"
"    color: rgb(85, 85, 0);\n"
"    font: 50 11pt \"MV Boli\";\n"
"    color: rgb(85, 170, 0);\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(630, 210, 16, 20))
        self.label_10.setStyleSheet("QLabel\n"
"{\n"
"  \n"
"    color: rgb(85, 85, 0);\n"
"    font: 50 11pt \"MV Boli\";\n"
"    color: rgb(85, 170, 0);\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.label_10.setObjectName("label_10")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(670, 160, 31, 31))
        self.lineEdit_3.setStyleSheet("QLineEdit\n"
"{\n"
" color :#FFF;\n"
" \n"
"    font: 10pt \"MS PGothic\";\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(770, 160, 31, 31))
        self.lineEdit_4.setStyleSheet("QLineEdit\n"
"{\n"
" color :#FFF;\n"
" \n"
"    font: 10pt \"MS PGothic\";\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(670, 200, 31, 31))
        self.lineEdit_6.setStyleSheet("QLineEdit\n"
"{\n"
" color :#FFF;\n"
" \n"
"    font: 10pt \"MS PGothic\";\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(770, 200, 31, 31))
        self.lineEdit_7.setStyleSheet("QLineEdit\n"
"{\n"
" color :#FFF;\n"
" \n"
"    font: 10pt \"MS PGothic\";\n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Nave Base"))
        self.label.setText(_translate("Form", "Nave Base  Trained Sucessfully With Data In Array"))
        self.label_2.setText(_translate("Form", "Enter the new  State :"))
        self.pushButton.setText(_translate("Form", "Clear"))
        self.label_3.setText(_translate("Form", "state2"))
        self.label_4.setText(_translate("Form", "State1"))
        self.pushButton_2.setText(_translate("Form", "Predict"))
        self.pushButton_3.setText(_translate("Form", "Home"))
        self.label_7.setText(_translate("Form", "Predict"))
        self.label_5.setText(_translate("Form", "Confusion matrix  same data"))
        self.label_6.setText(_translate("Form", "1"))
        self.label_8.setText(_translate("Form", "0"))
        self.label_9.setText(_translate("Form", "1"))
        self.label_10.setText(_translate("Form", "0"))
        self.lineEdit_3.setReadOnly(True);
        self.lineEdit_6.setReadOnly(True);
        self.lineEdit_7.setReadOnly(True);
        self.lineEdit_4.setReadOnly(True);
        self.confusion_matrix()
    def confusion_matrix(self):
        from sklearn.naive_bayes import GaussianNB
        import numpy as np
        x = np.array(
            [[-3, 7], [1, 5], [1, 2], [-2, 0], [2, 3], [-4, 0], [-1, 1], [1, 1], [-2, 2], [2, 7], [-4, 1], [-2, 7]])
        y = np.array([3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 4, 4])
        model = GaussianNB()
        model.fit(x, y)

        predicted = model.predict(
            [[-3, 7], [1, 5], [1, 2], [-2, 0], [2, 3], [-4, 0], [-1, 1], [1, 1], [-2, 2], [2, 7], [-4, 1], [-2, 7]])
        from sklearn.metrics import confusion_matrix
        expected = y
        predicted_by_Algorithm = predicted

        results = confusion_matrix(predicted, expected)
        self.lineEdit_3.setText("%d"%(results[0][0]))
        self.lineEdit_4.setText("%d" % (results[0][1]))
        self.lineEdit_6.setText("%d" % (results[1][0]))
        self.lineEdit_7.setText("%d" % (results[1][1]))
        self.lineEdit.setStyleSheet("color:#fff");
        self.lineEdit_2.setStyleSheet("color:#fff");
        self.pushButton_2.clicked.connect(self.predivt)
        self.pushButton.clicked.connect(self.clear_edit)
        self.pushButton_3.clicked.connect(self.home)
    def clear_edit(self):
         self.lineEdit_5.setText("")
         self.lineEdit_2.setText("");
         self.lineEdit.setText("")
    def home(self):
     global Form;
     Form.close()
     runhome()
    def predivt(self):
        from sklearn.naive_bayes import GaussianNB
        import numpy as np
        x = np.array(
            [[-3, 7], [1, 5], [1, 2], [-2, 0], [2, 3], [-4, 0], [-1, 1], [1, 1], [-2, 2], [2, 7], [-4, 1], [-2, 7]])
        y = np.array([3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 4, 4])
        model = GaussianNB()
        model.fit(x, y)
        try:
             x = self.lineEdit.text();
             y =self.lineEdit_2.text();
             if x == "" or y == "":
                 raise NameError
             x = float(x)
             y =float(y)
             output = model.predict([[x,y]]);
             print(output[0])
             output = int(output[0]);
             self.lineEdit_5.setText("%d"%(output))
        except:
            QtWidgets.QMessageBox.information(Form,"info","errror enter the number ....");

def runhome():
    os.system("python main.py")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

