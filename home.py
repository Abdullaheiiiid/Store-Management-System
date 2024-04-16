from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_home_window(object):
    def setupUi(self, home_window):
        home_window.setObjectName("home_window")
        home_window.resize(1000, 800)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        home_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/Logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        home_window.setWindowIcon(icon)
        home_window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.home_categories_label = QtWidgets.QLabel(home_window)
        self.home_categories_label.setGeometry(QtCore.QRect(520, 350, 341, 321))
        self.home_categories_label.setStyleSheet("background-image: url(:/newPrefix/Users/abdo mohsen/Pictures/Saved Pictures/980848.jpg);")
        self.home_categories_label.setText("")
        self.home_categories_label.setPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/CATEGORY.jpg"))
        self.home_categories_label.setScaledContents(True)
        self.home_categories_label.setObjectName("home_categories_label")
        self.home_home_label = QtWidgets.QLabel(home_window)
        self.home_home_label.setGeometry(QtCore.QRect(160, 390, 311, 101))
        self.home_home_label.setStyleSheet("background-image: url(:/newPrefix/Users/abdo mohsen/Pictures/download.png);")
        self.home_home_label.setText("")
        self.home_home_label.setPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/home.jpg"))
        self.home_home_label.setScaledContents(True)
        self.home_home_label.setObjectName("home_home_label")
        self.home_order_label = QtWidgets.QLabel(home_window)
        self.home_order_label.setGeometry(QtCore.QRect(160, 520, 311, 101))
        self.home_order_label.setStyleSheet("background-image: url(:/newPrefix/Users/abdo mohsen/Pictures/download.png);")
        self.home_order_label.setText("")
        self.home_order_label.setPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/order.jpg"))
        self.home_order_label.setScaledContents(True)
        self.home_order_label.setObjectName("home_order_label")
        self.frame = QtWidgets.QFrame(home_window)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1111, 251))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.category1_b3b3Logo_label = QtWidgets.QLabel(self.frame)
        self.category1_b3b3Logo_label.setGeometry(QtCore.QRect(30, 10, 80, 80))
        self.category1_b3b3Logo_label.setStyleSheet("background-color: transparent;")
        self.category1_b3b3Logo_label.setText("")
        self.category1_b3b3Logo_label.setPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/Logo.jpg"))
        self.category1_b3b3Logo_label.setScaledContents(True)
        self.category1_b3b3Logo_label.setObjectName("category1_b3b3Logo_label")
        self.category1_background_label = QtWidgets.QLabel(self.frame)
        self.category1_background_label.setGeometry(QtCore.QRect(-10, 0, 1121, 251))
        self.category1_background_label.setStyleSheet("background-color:rgb(6, 160, 170);")
        self.category1_background_label.setText("")
        self.category1_background_label.setObjectName("category1_background_label")
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/icons8-home-1000.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/orders.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.category1_cart_pushButton = QtWidgets.QPushButton(self.frame)
        self.category1_cart_pushButton.setGeometry(QtCore.QRect(900, 30, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        self.category1_cart_pushButton.setFont(font)
        self.category1_cart_pushButton.setStyleSheet("border: 5px solid white;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(5, 159, 169);\n"
"border-radius:10px;\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/icons8-cart-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.category1_cart_pushButton.setIcon(icon4)
        self.category1_cart_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.category1_cart_pushButton.setObjectName("category1_cart_pushButton")
        self.home_search_text_label = QtWidgets.QLabel(self.frame)
        self.home_search_text_label.setGeometry(QtCore.QRect(320, 120, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(20)
        self.home_search_text_label.setFont(font)
        self.home_search_text_label.setStyleSheet("background-color:transparent;\n"
"color:white;")
        self.home_search_text_label.setObjectName("home_search_text_label")
        self.category1_background_label.raise_()
        self.category1_b3b3Logo_label.raise_()
        self.category1_cart_pushButton.raise_()
        self.home_search_text_label.raise_()
        # self.home_search_lineEdit = QtWidgets.QLineEdit(home_window)
        # self.home_search_lineEdit.setGeometry(QtCore.QRect(210, 180, 571, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        # self.home_search_lineEdit.setFont(font)
        # self.home_search_lineEdit.setStyleSheet("background-color:transparent;\n"
        # "border: 5px solid white;\n"
        # "color:white;\n"
        # "border-radius:25px;\n"
        # "padding-left:20px;")
        # self.home_search_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        # self.home_search_lineEdit.setDragEnabled(False)
        # self.home_search_lineEdit.setObjectName("home_search_lineEdit")

        self.retranslateUi(home_window)
        QtCore.QMetaObject.connectSlotsByName(home_window)

    def retranslateUi(self, home_window):
        _translate = QtCore.QCoreApplication.translate
        home_window.setWindowTitle(_translate("home_window", "B3B3 - Home"))
        self.category1_cart_pushButton.setText(_translate("home_window", "Cart"))
        self.home_search_text_label.setText(_translate("home_window", f"Welcome to B3B3 Store"))
        # self.home_search_lineEdit.setText(_translate("home_window", "search any thing"))
#import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    home_window = QtWidgets.QDialog()
    ui = Ui_home_window()
    ui.setupUi(home_window)
    home_window.show()
    sys.exit(app.exec_())