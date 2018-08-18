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
        icon.addPixmap(QtGui.QPixmap("C:/Users/safwat/Desktop/photos/4.PNg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget\n"
"{\n"
"   \n"
"    background-color: rgb(53, 53, 53);\n"
"    color: rgb(170, 0, 0);\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 30, 591, 61))
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
        self.label_7.setGeometry(QtCore.QRect(670, 240, 101, 20))
        self.label_7.setStyleSheet("QLabel\n"
"{\n"
"  \n"
"    color: rgb(85, 85, 0);\n"
"    font: 50 11pt \"MV Boli\";\n"
"    color: rgb(85, 170, 0);\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(750, 120, 31, 51))
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"  \n"
"    color: rgb(85, 85, 0);\n"
"    font: 50 11pt \"MV Boli\";\n"
"    color: rgb(85, 170, 0);\n"
"    font: 75 italic 16pt \"MS Shell Dlg 2\";\n"
"    font: 75 24pt \"Myanmar Text\";\n"
"    color: rgb(85, 170, 127);\n"
"}")
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(700, 170, 113, 41))
        self.lineEdit_3.setStyleSheet("QLineEdit\n"
"{\n"
"    color: rgb(161, 181, 200);\n"
"  \n"
"    font: 75 italic 22pt \"Nirmala UI\";\n"
"  padding-left:45px;;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "KNN"))
        self.label.setText(_translate("Form", "KNN  Trained Sucessfully With Data In Output File"))
        self.label_2.setText(_translate("Form", "Enter the new  State :"))
        self.pushButton.setText(_translate("Form", "Clear"))
        self.label_3.setText(_translate("Form", "Test 1"))
        self.label_4.setText(_translate("Form", "Test 2"))
        self.pushButton_2.setText(_translate("Form", "Predict"))
        self.pushButton_3.setText(_translate("Form", "Home"))
        self.label_7.setText(_translate("Form", "Predict_Cancer"))
        self.label_5.setText(_translate("Form", "K"))
        self.lineEdit.setStyleSheet("color:#55557f");
        self.lineEdit_2.setStyleSheet("color:#55557f");
        self.lineEdit_3.setText("3");
        self.pushButton.clicked.connect(self.clear_edit)
        self.pushButton_3.clicked.connect(self.home)
        self.pushButton_2.clicked.connect(self.predict)


    def clear_edit(self):
        self.lineEdit_5.setText("")
        self.lineEdit_2.setText("");
        self.lineEdit.setText("")
        self.lineEdit_3.setText("3");

    def home(self):
        global Form;
        Form.close()
        runhome()
    def predict(self):
        import numpy as np
        from sklearn.neighbors import KNeighborsClassifier
        data = np.genfromtxt("date.csv", delimiter=";")
        x = data.astype(int)
        targat = np.genfromtxt("output.csv", delimiter=";")
        y = targat.astype(int)
        try:
            t1= self.lineEdit.text();
            t2 = self.lineEdit_2.text();
            k = self.lineEdit_3.text();
            if t1 == "" or t2 == "" or k =="":
                raise NameError("error")
            t1 = int(t1);
            t2 = int(t2);
            k = int(k);
            print(t1,t2,k)
            neigh = KNeighborsClassifier(n_neighbors=k)
            neigh.fit(x, y)
            output = ""
            pred = neigh.predict([[t1,t2]])[0];
            print(pred)
            if pred == 1:
                output = " Hava cancer";
            else:
                output = " No Have cancer"
            print(output)
            self.lineEdit_5.setText(output);
        except:
            QtWidgets.QMessageBox.information(Form,"info" ,"have erroe plz enter correct date")

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

