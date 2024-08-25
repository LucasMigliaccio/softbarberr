# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'carritocompras.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTableView, QToolButton,
    QVBoxLayout, QWidget)

class CarritoCompras(object):
    def setupUi(self, add_edit_menu):
        if not add_edit_menu.objectName():
            add_edit_menu.setObjectName(u"add_edit_menu")
        add_edit_menu.resize(600, 811)
        add_edit_menu.setMinimumSize(QSize(600, 0))
        add_edit_menu.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(add_edit_menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(add_edit_menu)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setMaximumSize(QSize(600, 16777215))
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.central_widget_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.background_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setMinimumSize(QSize(0, 0))
        self.content_frame.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.content_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_nav = QFrame(self.content_frame)
        self.frame_nav.setObjectName(u"frame_nav")
        self.frame_nav.setMinimumSize(QSize(0, 40))
        self.frame_nav.setMaximumSize(QSize(16777215, 40))
        self.frame_nav.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_nav.setFrameShape(QFrame.StyledPanel)
        self.frame_nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_nav)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_tittle = QLabel(self.frame_nav)
        self.label_tittle.setObjectName(u"label_tittle")
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        self.label_tittle.setFont(font)
        self.label_tittle.setStyleSheet(u"\n"
"color: rgb(189, 189, 189);")

        self.horizontalLayout_6.addWidget(self.label_tittle)

        self.butttons_holder_frame = QFrame(self.frame_nav)
        self.butttons_holder_frame.setObjectName(u"butttons_holder_frame")
        self.butttons_holder_frame.setMinimumSize(QSize(110, 30))
        self.butttons_holder_frame.setMaximumSize(QSize(110, 16777215))
        self.butttons_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.butttons_holder_frame.setFrameShadow(QFrame.Raised)
        self.minimize_button = QToolButton(self.butttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(0, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"./assets/icons/minimize-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_button.setIcon(icon)
        self.restore_button = QToolButton(self.butttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(30, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/restore-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restore_button.setIcon(icon1)
        self.maximize_button = QToolButton(self.butttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(30, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/maximize-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximize_button.setIcon(icon2)
        self.close_button = QToolButton(self.butttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(60, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/close-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_button.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.butttons_holder_frame)


        self.verticalLayout.addWidget(self.frame_nav)

        self.frame_productos = QFrame(self.content_frame)
        self.frame_productos.setObjectName(u"frame_productos")
        self.frame_productos.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.frame_productos.setFrameShape(QFrame.StyledPanel)
        self.frame_productos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_productos)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.productos_tableView = QTableView(self.frame_productos)
        self.productos_tableView.setObjectName(u"productos_tableView")
        self.productos_tableView.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_3.addWidget(self.productos_tableView)


        self.verticalLayout.addWidget(self.frame_productos)

        self.frame_button = QFrame(self.content_frame)
        self.frame_button.setObjectName(u"frame_button")
        self.frame_button.setMinimumSize(QSize(0, 40))
        self.frame_button.setMaximumSize(QSize(16777215, 40))
        self.frame_button.setFrameShape(QFrame.StyledPanel)
        self.frame_button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_button)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_button)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.contador_spinBox = QSpinBox(self.frame_button)
        self.contador_spinBox.setObjectName(u"contador_spinBox")
        self.contador_spinBox.setMinimumSize(QSize(100, 37))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(True)
        self.contador_spinBox.setFont(font2)
        self.contador_spinBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.contador_spinBox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.contador_spinBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.add_pushButton = QPushButton(self.frame_button)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setMinimumSize(QSize(0, 40))
        self.add_pushButton.setMaximumSize(QSize(16666666, 40))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        font3.setBold(True)
        self.add_pushButton.setFont(font3)
        self.add_pushButton.setStyleSheet(u"QPushButton {\n"
"background-color: #7c7c7c;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(11, 168, 16);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.add_pushButton)


        self.verticalLayout.addWidget(self.frame_button)

        self.frame_carrito = QFrame(self.content_frame)
        self.frame_carrito.setObjectName(u"frame_carrito")
        self.frame_carrito.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.frame_carrito.setFrameShape(QFrame.StyledPanel)
        self.frame_carrito.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_carrito)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.carrito_tableView = QTableView(self.frame_carrito)
        self.carrito_tableView.setObjectName(u"carrito_tableView")
        self.carrito_tableView.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.carrito_tableView)


        self.verticalLayout.addWidget(self.frame_carrito)

        self.add_edit_button = QPushButton(self.content_frame)
        self.add_edit_button.setObjectName(u"add_edit_button")
        self.add_edit_button.setMinimumSize(QSize(0, 50))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Black"])
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(True)
        self.add_edit_button.setFont(font4)
        self.add_edit_button.setStyleSheet(u"QPushButton {\n"
"background-color: #7c7c7c;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(11, 168, 16);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout.addWidget(self.add_edit_button)

        self.add_edit_button_2 = QPushButton(self.content_frame)
        self.add_edit_button_2.setObjectName(u"add_edit_button_2")
        self.add_edit_button_2.setMinimumSize(QSize(0, 50))
        self.add_edit_button_2.setFont(font4)
        self.add_edit_button_2.setStyleSheet(u"QPushButton {\n"
"background-color: #7c7c7c;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(194, 0, 0);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout.addWidget(self.add_edit_button_2)


        self.horizontalLayout.addWidget(self.content_frame)


        self.gridLayout_2.addWidget(self.background_frame, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.central_widget_frame, 0, 0, 1, 1)


        self.retranslateUi(add_edit_menu)

        QMetaObject.connectSlotsByName(add_edit_menu)
    # setupUi

    def retranslateUi(self, add_edit_menu):
        add_edit_menu.setWindowTitle(QCoreApplication.translate("add_edit_menu", u"Form", None))
        self.label_tittle.setText(QCoreApplication.translate("add_edit_menu", u"Carrito de Compras", None))
        self.minimize_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.close_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.label.setText(QCoreApplication.translate("add_edit_menu", u"Cantidad:", None))
        self.add_pushButton.setText(QCoreApplication.translate("add_edit_menu", u"Agregar Al Carrito", None))
        self.add_edit_button.setText(QCoreApplication.translate("add_edit_menu", u"AGREGAR PRODUCTO", None))
        self.add_edit_button_2.setText(QCoreApplication.translate("add_edit_menu", u"SALIR", None))
    # retranslateUi

