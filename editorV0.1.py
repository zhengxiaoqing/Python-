from Editor02 import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QWidget,QDialog,QMessageBox,QMainWindow,QFileDialog,qApp
import sys

#第二版本用来实现复杂的列表计算
class cal_function(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(cal_function,self).__init__()
        self.setupUi(self)
        self.action()

    def action(self):
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_as.triggered.connect(self.saveAsFile)
        self.actionExit.triggered.connect(qApp.quit)
        self.actionCopy.triggered.connect(self.plainTextEdit.copy)
        self.actionPaste.triggered.connect(self.plainTextEdit.paste)
        self.actionCut.triggered.connect(self.plainTextEdit.cut)
        self.actionFind.triggered.connect(self.findStr)
        self.actionRelace.triggered.connect(self.replaceStr)

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self,'open file','.\\')
        with open(filename[0], 'r') as f:
            my_txt = f.read()
            self.plainTextEdit.setPlainText(my_txt)
    def saveFile(self):
        filename = QFileDialog.getSaveFileName(self,'save file', '.\\')
        with open(filename[0], 'w') as f:
            my_text = self.plainTextEdit.toPlainText()
            f.write(my_text)

    def saveAsFile(self):
        pass


    def findStr(self):
        pass

    def replaceStr(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mycal = cal_function()
    mycal.show()
    sys.exit(app.exec_())