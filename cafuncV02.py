from calculater02 import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QWidget,QDialog,QMessageBox
import sys

#第二版本用来实现复杂的列表计算
class cal_function(QDialog,Ui_MainWindow):
    displaystring = ''
    operation = ''
    fNum = 0
    sNum = 0
    result = 0
    numList = []
    right_bracket = 0
    tmpList = []

#错误
    #1,  空.数    数.数.数
    #2，   2（3+1）    2（3+1      2）3+1
    #     3/空
    #    0一个 000003
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
        #按下括号
        self.b_left.clicked.connect(self.lbracketClicked)
        self.b_right.clicked.connect(self.rbracketClicked)

    def numClicked(self):
        if len(cal_function.displaystring) <= 7:
            cal_function.displaystring = cal_function.displaystring  + self.sender().text()
            if cal_function.displaystring =='.':
                cal_function.displaystring ='0.'
            elif cal_function.displaystring.count('.') > 1:
                cal_function.displaystring = cal_function.displaystring[:-1]
            else:
                # cal_function.tmpList.append(cal_function.displaystring)
                # # tmpString = cal_function.tmpList[-1]
                # cal_function.numList.append(tmpString)
                self.label.setText(cal_function.displaystring)
        else:
            pass
        # cal_function.tmpList.append(cal_function.displaystring)
        # tmpString = cal_function.tmpList[-1]
        # cal_function.numList.append(tmpString)

        # if len(cal_function.displaystring) <= 7:
        #     cal_function.displaystring = cal_function.displaystring  + self.sender().text()
        #     if cal_function.displaystring =='.':
        #         cal_function.displaystring =='0.'
        #     else:
        #         if cal_function.displaystring.count('.') > 1:
        #             cal_function.displaystring = cal_function.displaystring[:-1]
        #         else:
        #             cal_function.numList.append(cal_function.displaystring)
        #             self.label.setText(cal_function.displaystring)
        #             cal_function.fNum = float(cal_function.displaystring)
        # else:
        #     pass


    #左括号如果左面有数则去掉
    def lbracketClicked(self):
        if cal_function.numList[-1].isdigit():
            cal_function.numList.pop()
        cal_function.displaystring =''
        cal_function.numList.append(self.sender().text())
        cal_function.right_bracket += 1
        self.label.setText(''.join(cal_function.numList))

    #右括号根据左括号的数目来添加
    def rbracketClicked(self):
        if cal_function.right_bracket > 0:
            cal_function.numList.append(self.sender().text())
            cal_function.right_bracket -= 1
            self.label.setText(''.join(cal_function.numList))
        else:
            pass

    def operationClicked(self):
        # cal_function.numList.append(cal_function.displaystring)
        # print(cal_function.numList)
        # cal_function.sNum = cal_function.fNum
        # 下面代码不行 ['1.1', '+', '2.1']，['3.2', '2.1', '+', '3.1']
        if cal_function.numList ==[]:
            cal_function.numList.append(cal_function.displaystring)
        else:
            if cal_function.result == cal_function.numList[0]:
                pass
            else:
                cal_function.numList.append(cal_function.displaystring)
        # if cal_function.result == 0:
        #     cal_function.numList.append(cal_function.tmpList[-1])
        # else:
        #     cal_function.numList = [cal_function.result,]
        cal_function.displaystring = ''
        # cal_function.operation = self.sender().objectName()
        cal_function.numList.append(self.sender().text())
        self.label.setText(''.join(cal_function.numList))
      #  self.label.setText(self.sender().text())


    def clearClicked(self):
        cal_function.fNum = cal_function.sNum = cal_function.result = 0
        cal_function.displaystring = ''
        cal_function.operation = ''
        cal_function.numList = []
        self.label.setText(cal_function.displaystring)


    def equalClicked(self):
        #如果右括号数目不够，则自动添加右括号，否则eval计算报错
        cal_function.numList.append(cal_function.displaystring)
        if cal_function.right_bracket != 0:
            cal_function.numList.append(')' * cal_function.right_bracket)
        print(cal_function.numList)
        cal_function.result = eval(''.join(cal_function.numList))

        self.label.setText(str(cal_function.result))
        # cal_function.fNum = cal_function.result
        cal_function.displaystring = ''
        cal_function.numList = [str(cal_function.result)]
        cal_function.right_bracket = 0   #按下= 后括号计数器清0

    #关闭时提示框
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
    sys.exit(app.exec_())