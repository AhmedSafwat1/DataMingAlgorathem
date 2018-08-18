from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import subprocess
import sys
import os
from mainhome import Ui_MainWindow
from Decision_tree2 import Ui_Form;
import webbrowser

class main2(QWidget,Ui_Form):
    def home(self):
     self.close()
     w = main();
     w.show()

    def clear_lineedit(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
    def predict(self):
         from sklearn import tree
         from sklearn.datasets import load_iris
         iris = load_iris()
         clf = tree.DecisionTreeClassifier()
         clf = clf.fit(iris.data, iris.target)


         x = self.lineEdit.text()
         print(x)
         y = self.lineEdit_2.text()
         z = self.lineEdit_3.text()
         k = self.lineEdit_4.text()
         print(x,z,y,k)
         try :
             if x == "" or y=="" or z == "" or k =="":
                 raise NameError("error")

             x = float(x);
             y= float(y);
             z = float(z);
             k = float(k);
             output = clf.predict([[x,y,z,k]])
             ot = int(output)
             m = ['setosa', 'versicolor' ,'virginica']
             print(m[ot])
             self.lineEdit_5.setText(m[ot])
         except:
              # window = QMainWindow();
             window = QWidget()
             window.move(400,200)
             print(x,z,y,k)
             QMessageBox.information( window ,"info","erroe....must enter the number ")   ;


    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.clear_lineedit)
        self.pushButton_2.clicked.connect(self.predict)
        self.pushButton_3.clicked.connect(self.home);
        self.lineEdit_5.setStyleSheet("color:red;font-size:18px ;font-weight:bold");



class main(QMainWindow,Ui_MainWindow):
    def kmeans(self):
        self.close()
        runkmean()
    def go_link(self):
        webbrowser.open("https://www.Facebook.com")
    def nav(self):
        self.close()
        runnav()
    def knn(self):
        self.close();
        runknn()
    def classific(self):

        from sklearn import tree
        from sklearn.datasets import load_iris
        iris = load_iris()
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(iris.data, iris.target)
        window = QWidget()
        window.move(400,200)
        Result = QMessageBox.question( window, "message", "Do you want make a pdf for the Decision Tree",
                                      QMessageBox.Yes | QMessageBox.No)
        if Result == QMessageBox.Yes:
            import graphviz
            dot_data = tree.export_graphviz(clf, out_file=None)
            graph = graphviz.Source(dot_data)

            dot_data = tree.export_graphviz(clf, out_file=None,
                                            feature_names=iris.feature_names,
                                            class_names=iris.target_names,
                                            filled=True, rounded=True,
                                            special_characters=True)

            graph = graphviz.Source(dot_data)
            graph.render("iris", view=True)
            QMessageBox.information(window,"info","Pdf sucessful created....")
            self.close()
            run()
        if Result == QMessageBox.No:
            self.close()
            run()


    def __init__(self):
        QMainWindow.__init__(self)

        self.setupUi(self);
        self.flag=0
        self.centralwidget.setStyleSheet("background-color:rgb(40, 40, 40)");
        self.pushButton_2.setStyleSheet("background-color: rgb(234, 234, 234)");
        self.pushButton_4.setStyleSheet("background-color: rgb(234, 234, 234)");
        self.pushButton_5.setStyleSheet("background-color: rgb(234, 234, 234)");
        self.pushButton.clicked.connect(self.classific)
        self.pushButton_3.clicked.connect(self.nav)
        self.pushButton_2.clicked.connect(self.knn)
        self.pushButton_5.clicked.connect(self.kmeans);
        self.actionDecision_Tree.triggered.connect(self.classific)
        self.actionNaive_Base.triggered.connect(self.nav)
        self.actionKNN.triggered.connect(self.knn)
        self.actionK_Means.triggered.connect(self.kmeans);
        # w = QWidget()
        # self.help = QAction("Contact_US")
        # icon12 = QIcon()
        # icon12.addPixmap(QPixmap("C:/Users/safwat/Desktop/photos/13.PNg"), QIcon.Normal, QIcon.Off)
        # self.help.setIcon(icon12)
        # self.menuHelp.addAction(self.help);
        # self.help.triggered.connect(self.go_link)
        self.pushButton_4.setEnabled(False)


def run():
    os.system("python Decision_tree2.py")
def runnav():
    os.system("python nave_base.py")
def runknn():
    os.system("python knn2.py")

def runkmean():
    os.system("python kmeans.py")
app = QApplication(sys.argv)
w = main()
w.show();
app.exec_()
