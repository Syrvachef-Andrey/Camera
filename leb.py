from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(1320, 652)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1320, 652))
        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setGeometry(QtCore.QRect(570, 510, 171, 81))
        self.control_bt.setMinimumSize(QtCore.QSize(171, 81))
        self.control_bt.setMaximumSize(QtCore.QSize(171, 81))
        self.control_bt.setCheckable(True)
        self.control_bt.setChecked(False)
        self.control_bt.setAutoExclusive(False)
        self.control_bt.setObjectName("control_bt")
        self.image_label_2 = QtWidgets.QLabel(Form)
        self.image_label_2.setGeometry(QtCore.QRect(670, 10, 640, 480))
        self.image_label_2.setMinimumSize(QtCore.QSize(640, 480))
        self.image_label_2.setMaximumSize(QtCore.QSize(640, 480))
        self.image_label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.image_label_2.setObjectName("image_label_2")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.image_label.setMinimumSize(QtCore.QSize(640, 480))
        self.image_label.setMaximumSize(QtCore.QSize(640, 480))
        self.image_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.image_label.setObjectName("image_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Camera"))
        self.control_bt.setText(_translate("Form", "START"))
        self.image_label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.image_label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())