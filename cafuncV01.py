from calculater02 import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QWidget,QDialog,QMessageBox
import sys


class cal_function(QDialog,Ui_MainWindow):
    displaystring = ''
    operation = ''
    fNum = 0
    sNum = 0
    result = 0

    def __init__(self ,parent=None):
        QDialog.__init__(self,parent)
        self.setupUi(self)
        self.action()


    def action(self):
        #按下数字的执行方法
        # for i in ['b'+ str(i) for i in range(0,10)]:
        #    self.i.clicked.connect(self.numClicked)
        self.b0.clicked.connect(self.numClicked)
        self.b1.clicked.connect(self.numClicked)
        self.b2.clicked.connect(self.numClicked)
        self.b3.clicked.connect(self.numClicked)
        self.b4.clicked.connect(self.numClicked)
        self.b5.clicked.connect(self.numClicked)
        self.b6.clicked.connect(self.numClicked)
        self.b7.clicked.connect(self.numClicked)
        self.b8.clicked.connect(self.numClicked)
        self.b9.clicked.connect(self.numClicked)
        self.b_point.clicked.connect(self.numClicked)
        #按下操作符
        self.b_plus.clicked.connect(self.operationClicked)
        self.b_minus.clicked.connect(self.operationClicked)
        self.b_multi.clicked.connect(self.operationClicked)
        self.b_div.clicked.connect(self.operationClicked)
        #按下C
        self.b_clear.clicked.connect(self.clearClicked)
        #按下=
        self.b_equal.clicked.connect(self.equalClicked)

    def numClicked(self):
        if len(cal_function.displaystring) <= 7:
            cal_function.displaystring = cal_function.displaystring  + self.sender().text()
            if cal_function.displaystring =='.':
                cal_function.displaystring =='0.'
            else:
                if cal_function.displaystring.count('.') > 1:
                    cal_function.displaystring = cal_function.displaystring[:-1]
                else:
                    self.label.setText(cal_function.displaystring)
                    print('displaystring is'  , cal_function.displaystring)
                    cal_function.fNum = float(cal_function.displaystring)
        else:
            pass

    def operationClicked(self):
        cal_function.sNum = cal_function.fNum
        cal_function.displaystring = ''
        cal_function.operation = self.sender().objectName()
      #  self.label.setText(self.sender().text())


    def clearClicked(self):
        cal_function.fNum = cal_function.sNum = cal_function.result = 0
        cal_function.displaystring = ''
        cal_function.operation = ''
        self.label.setText(cal_function.displaystring)
        #self.label.display(0)

    def equalClicked(self):
        if cal_function.operation == 'b_plus':
            cal_function.result = cal_function.sNum + cal_function.fNum
            self.label.setText(str(cal_function.result))
        elif cal_function.operation == 'b_minus':
            cal_function.result = cal_function.sNum - cal_function.fNum
            self.label.setText(str(cal_function.result))

        elif cal_function.operation == 'b_multi':
            cal_function.result = cal_function.sNum * cal_function.fNum
            self.label.setText(str(cal_function.result))

        elif cal_function.operation == 'b_div':
            if cal_function.fNum == 0:
                self.label.setText("Error")
                cal_function.result = 0
                cal_function.sNum = 0
            else:
                cal_function.result = cal_function.sNum / cal_function.fNum
                self.label.setText(str(cal_function.result))

        cal_function.fNum = cal_function.result
        cal_function.displaystring = ''

    def closeEvent(self, event):
        reply = QMessageBox.question(self,'Message',
                                      "确定要退出么?", QMessageBox.Yes |
                                      QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mycal = cal_function()
    mycal.show()
    # widget = QWidget()
    # ui = Ui_MainWindow()
    # ui.setupUi(widget)
    # widget.show()
    sys.exit(app.exec_())