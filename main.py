import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout

class Myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('교사용 창')
        self.move(300,300)
        self.resize(400,200)
        self.show()
        btn1 = QPushButton('학생상담')
        btn1.setCheckable(True)
        btn1.toggle()
        btn1.resize(100,100)
        btn2 = QPushButton('학생점수확인')
        btn2.setText('')



if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Myapp()
    sys.exit(app.exec())