import sys,socket
from PyQt5.QtWidgets import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
22125756
svrIP = input(("Server IP(default:127.0.0.1"))
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
        btn2 = QPushButton('학생점수확인버튼')
        btn2.setText('')
        btn2.resize(100,100)
        btn3 = QPushButton('문제출제버튼')
        btn3.setText('')
        btn3.resize(100,100)
        btn4 = QPushButton('상담버튼')
        btn4.setText('')
        btn4.resize(100,100)
        btn5 = QPushButton('확인할 학생버튼')
        btn5.setText('')
        btn5.resize(100,100)

        vbox=QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addWidget(btn5)



if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Myapp()
    sys.exit(app.exec())