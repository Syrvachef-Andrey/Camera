import sys
import cv2
import os

from datetime import datetime
from leb import *

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, QThread, pyqtSignal


fourcc = cv2.VideoWriter_fourcc(*'DIVX')

cap1 = cv2.VideoCapture(cv2.CAP_DSHOW, 0)
cap1.set(3, 480)
cap1.set(4, 640)
cap1.set(5, 30)

cap2 = cv2.VideoCapture(2, cv2.CAP_DSHOW)
cap2.set(3, 480)
cap2.set(4, 640)
cap2.set(5, 30)


class Thread1(QThread):
    changePixmap1 = pyqtSignal(QImage)

    def __init__(self, *args, **kwargs):
        super().__init__()

    def run(self):
        while cap1.isOpened():
            ret1, image1 = cap1.read()
            if ret1:
                im1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
                height1, width1, channel1 = im1.shape
                step1 = channel1 * width1
                qImg1 = QImage(im1.data, width1, height1, step1, QImage.Format_RGB888)
                self.changePixmap1.emit(qImg1)

            # self.msleep(7)


class Thread2(QThread):
    changePixmap2 = pyqtSignal(QImage)

    def __init__(self, *args, **kwargs):
        super().__init__()

    def run(self):
        while cap2.isOpened():
            ret2, image2 = cap2.read()
            if ret2:
                im2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
                height2, width2, channel2 = im2.shape
                step2 = channel2 * width2
                qImg2 = QImage(im2.data, width2, height2, step2, QImage.Format_RGB888)
                self.changePixmap2.emit(qImg2)

            # self.msleep(7)


class Thread3(QThread):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.active = True

    def run(self):
        if self.active:
            self.path = os.makedirs('C:/camera/' + datetime.now().strftime('%Y-%m-%d__%H-%M-%S'))
            self.out1 = cv2.VideoWriter(
                os.path.join('C:/camera/' + datetime.now().strftime('%Y-%m-%d__%H-%M-%S'), 'cam1.avi'), fourcc, 30,
                (640, 480))
            while self.active:
                ret1, image1 = cap1.read()
                if ret1:
                    self.out1.write(image1)

                # self.msleep(7)

    def stop(self):
        self.out1.release()


class Thread4(QThread):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.active = True

    def run(self):
        if self.active:
            self.out2 = cv2.VideoWriter(
                os.path.join('C:/camera/' + datetime.now().strftime('%Y-%m-%d__%H-%M-%S'), 'cam2.avi'), fourcc, 30,
                (640, 480))
            while self.active:
                ret2, image2 = cap2.read()
                if ret2:
                    self.out2.write(image2)

                # self.msleep(7)

    def stop(self):
        self.out2.release()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.saveTimer = QTimer()
        self.ui.control_bt.clicked.connect(self.controlTimer)
        self.th1 = Thread1(self)
        self.th2 = Thread2(self)
        self.th1.changePixmap1.connect(self.setImage1)
        self.th2.changePixmap2.connect(self.setImage2)
        self.th1.start()
        self.th2.start()

    @QtCore.pyqtSlot(QImage)
    def setImage1(self, qImg1):
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg1))

    @QtCore.pyqtSlot(QImage)
    def setImage2(self, qImg2):
        self.ui.image_label_2.setPixmap(QPixmap.fromImage(qImg2))

    def controlTimer(self):
        if not self.saveTimer.isActive():
            self.saveTimer.start()
            self.th3 = Thread3(self)
            self.th3.start()
            self.th3.active = True
            self.th4 = Thread4(self)
            self.th4.start()
            self.th4.active = True
            self.ui.control_bt.setText("STOP")
        else:
            self.saveTimer.stop()
            self.th3.active = False
            self.th3.stop()
            self.th3.terminate()
            self.th4.active = False
            self.th4.stop()
            self.th4.terminate()
            self.ui.control_bt.setText("START")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())