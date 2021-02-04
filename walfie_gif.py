import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import random
from ui_walfie import Ui_Walfie

class Walfie(QMainWindow, Ui_Walfie):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()
        self.show()

    def setup(self):
        self.tray = QSystemTrayIcon()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.icon = QIcon("images/icon.png")
        self.tray.setIcon(self.icon)
        self.setToolTip("Walfie_Gif")
        
        self.index_a = 0
        self.index_b = 0
        self.random_time = 3*1000
        self.height = 200

        self.load_img()
        self.gif()
        self.add_menu()
        self.Timer()
        self.tray.show()

    def add_menu(self):
        self.menu = QMenu()

        exit = QAction("Quit", self, triggered=self.quit)
        exit.setIcon(self.icon)
        self.menu.addAction(exit)

        Next = QAction("Next Gif", self, triggered=self.next_img)
        Next.setIcon(self.icon)
        self.menu.addAction(Next)

        Hide = QAction("Hide", self, triggered=self.hide)
        Hide.setIcon(self.icon)
        self.menu.addAction(Hide)

        Show = QAction("Show", self, triggered=self.show)
        Show.setIcon(self.icon)
        self.menu.addAction(Show)

        ZoomIn = QAction("Zoom In", self, triggered=self.zoom_in)
        ZoomIn.setIcon(self.icon)
        self.menu.addAction(ZoomIn)

        ZoomOut = QAction("Zoom Out", self, triggered=self.zoom_out)
        ZoomOut.setIcon(self.icon)
        self.menu.addAction(ZoomOut)

        ResetSize = QAction("Reset Size", self, triggered=self.reset_size)
        ResetSize.setIcon(self.icon)
        self.menu.addAction(ResetSize)

        About = QAction("About", self, triggered=self.about)
        About.setIcon(self.icon)
        self.menu.addAction(About)

        self.tray.setContextMenu(self.menu)
    
    def load_img(self):
        self.img_frame = [80, 60, 40, 40, 40, 40, 80, 40, 40]
        self.imgs = [["images/example/example(1).png", "images/example/example(2).png", "images/example/example(3).png"], 
                     ["images/ukulele_practice/ukulele_practice(1).png", "images/ukulele_practice/ukulele_practice(2).png", 
                      "images/ukulele_practice/ukulele_practice(3).png", "images/ukulele_practice/ukulele_practice(4).png", 
                      "images/ukulele_practice/ukulele_practice(5).png", "images/ukulele_practice/ukulele_practice(6).png"], 
                     ["images/bee/bee(1).png", "images/bee/bee(2).png", "images/bee/bee(3).png", "images/bee/bee(4).png", 
                      "images/bee/bee(5).png"], 
                     ["images/shark_rap/shark_rap(1).png", "images/shark_rap/shark_rap(2).png", "images/shark_rap/shark_rap(3).png", 
                      "images/shark_rap/shark_rap(4).png", "images/shark_rap/shark_rap(5).png", "images/shark_rap/shark_rap(6).png", 
                      "images/shark_rap/shark_rap(7).png"], 
                     ["images/bongo/bongo(1).png", "images/bongo/bongo(2).png", "images/bongo/bongo(3).png", 
                      "images/bongo/bongo(4).png", "images/bongo/bongo(5).png", "images/bongo/bongo(6).png", 
                      "images/bongo/bongo(7).png"],
                     ["images/cake/cake(1).png", "images/cake/cake(2).png", "images/cake/cake(3).png", 
                      "images/cake/cake(4).png", "images/cake/cake(5).png", "images/cake/cake(6).png", 
                      "images/cake/cake(7).png", "images/cake/cake(8).png", "images/cake/cake(9).png"], 
                     ["images/confession/confession(1).png", "images/confession/confession(2).png", 
                      "images/confession/confession(3).png", "images/confession/confession(4).png", 
                      "images/confession/confession(5).png", "images/confession/confession(6).png", 
                      "images/confession/confession(7).png"], 
                     ["images/fire/fire(1).png", "images/fire/fire(2).png", "images/fire/fire(3).png", "images/fire/fire(4).png", 
                      "images/fire/fire(5).png", "images/fire/fire(6).png", "images/fire/fire(7).png", "images/fire/fire(8).png", 
                      "images/fire/fire(9).png", "images/fire/fire(10).png", "images/fire/fire(11).png", "images/fire/fire(12).png", 
                      "images/fire/fire(13).png", "images/fire/fire(14).png", "images/fire/fire(15).png", "images/fire/fire(16).png", 
                      "images/fire/fire(17).png", "images/fire/fire(18).png", "images/fire/fire(19).png"], 
                     ["images/recorder/recorder(1).png", "images/recorder/recorder(2).png", "images/recorder/recorder(3).png", 
                      "images/recorder/recorder(4).png", "images/recorder/recorder(5).png", "images/recorder/recorder(6).png", 
                      "images/recorder/recorder(7).png"]]

    def gif(self):
        if self.index_b >= len(self.imgs[self.index_a]):
            self.index_b = 0
        img = QPixmap(self.imgs[self.index_a][self.index_b])
        img = img.scaledToHeight(self.height)
        self.label.setPixmap(img)
        img_height = img.height()
        img_width = img.width()
        self.resize(self.height/img_height*img_width, self.height)
        self.index_b += 1
        timer = QTimer()
        timer.singleShot(self.img_frame[self.index_a], self.gif)

    def Timer(self):
        timer = QTimer()
        timer.singleShot(self.random_time, self.random_img)
    
    def random_img(self):
        self.index_a = random.randint(0, len(self.imgs)-1)
        if self.index_a >= len(self.imgs):
            self.index_a = 0
        self.Timer()

    def next_img(self):
        self.index_a += 1
        if self.index_a >= len(self.imgs):
            self.index_a = 0
    
    def zoom_in(self):
        self.height += 100
    
    def zoom_out(self):
        self.height -= 100
    
    def reset_size(self):
        self.height = 200
    
    def about(self):
        QMessageBox.information(self, "About", "About Walfie Gif\n关于Walfie Gif\n\nA simple, non interactive desktop application developed with Python and PySide2\n一个简单的，并无交互的，用Python和Pyside2开发的桌宠程序\n\nDeveloped by Bilibili@FanUCK\n由FanUCK开发\nGif resources from Twitter@walfieee (Not authorized)\nGif素材取自推特用户@walfieee（尚未经原作者授权）\n(I'm sorry, walfieee!)\n（对不住啦，walfieee！）\n\nProtagonists in gifs:\nGif中的人物：\n@Amelia Watson (The girl with yellow hair)\n@Gawr Gura (The girl with blue hair)\n@Shirakami Fubuki (The girl with white hair)\n@Calliope Mori (The girl with pink hair)\n(And as you know, they are all vtubers!)\n（而且如你所知，她们都是虚拟主播！）\n\nContact the developer:\n与开发者联系：\nEmail:\n2920312856@qq.com & qq2920312856@gmail.com\nBilibili:\n@FanUCK\nGitHub:\n@FanUCK\n\nThanks for using!\n感谢使用！\n\n——FanUCK\nWritten on February 3, 2021\n写于2021.02.03")
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
    
    def quit(self):
        self.hide()
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Walfie()
    sys.exit(app.exec_())
