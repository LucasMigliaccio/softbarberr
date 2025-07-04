# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adjust_stock.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QToolButton,
    QVBoxLayout, QWidget)

class AdjustStockProducto(object):
    def setupUi(self, add_edit_cliente):
        if not add_edit_cliente.objectName():
            add_edit_cliente.setObjectName(u"add_edit_cliente")
        add_edit_cliente.resize(600, 550)
        add_edit_cliente.setMinimumSize(QSize(600, 0))
        add_edit_cliente.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(add_edit_cliente)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(add_edit_cliente)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setMaximumSize(QSize(600, 16777215))
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setMinimumSize(QSize(0, 0))
        self.content_frame.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.content_frame)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 9, 9, 9)
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
        self.label_tittle.setStyleSheet(u"color: rgb(255, 255, 255) ;")

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


        self.verticalLayout_7.addWidget(self.frame_nav)

        self.frame_inferior = QFrame(self.content_frame)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setMaximumSize(QSize(16777215, 16777215))
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_inferior)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.codigobarra_title = QLabel(self.frame_inferior)
        self.codigobarra_title.setObjectName(u"codigobarra_title")
        self.codigobarra_title.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(True)
        self.codigobarra_title.setFont(font1)
        self.codigobarra_title.setStyleSheet(u"color: rgb(230, 230, 230);")
        self.codigobarra_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.codigobarra_title)

        self.product_name_label = QLabel(self.frame_inferior)
        self.product_name_label.setObjectName(u"product_name_label")
        self.product_name_label.setMaximumSize(QSize(16777215, 40))
        self.product_name_label.setFont(font1)
        self.product_name_label.setStyleSheet(u"color: rgb(230, 230, 230);")
        self.product_name_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.product_name_label)

        self.nombre_tittle = QLabel(self.frame_inferior)
        self.nombre_tittle.setObjectName(u"nombre_tittle")
        self.nombre_tittle.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Black"])
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setUnderline(False)
        self.nombre_tittle.setFont(font2)
        self.nombre_tittle.setLayoutDirection(Qt.LeftToRight)
        self.nombre_tittle.setStyleSheet(u"color: rgb(230, 230, 230);")
        self.nombre_tittle.setTextFormat(Qt.AutoText)
        self.nombre_tittle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.nombre_tittle)

        self.stock_actual_label = QLabel(self.frame_inferior)
        self.stock_actual_label.setObjectName(u"stock_actual_label")
        self.stock_actual_label.setMaximumSize(QSize(16777215, 40))
        self.stock_actual_label.setFont(font1)
        self.stock_actual_label.setStyleSheet(u"color: rgb(230, 230, 230);")
        self.stock_actual_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.stock_actual_label)

        self.stock_tittle = QLabel(self.frame_inferior)
        self.stock_tittle.setObjectName(u"stock_tittle")
        self.stock_tittle.setMaximumSize(QSize(16777215, 40))
        self.stock_tittle.setFont(font1)
        self.stock_tittle.setStyleSheet(u"\n"
"color: rgb(200, 157, 48);")
        self.stock_tittle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.stock_tittle)

        self.spinBox = QSpinBox(self.frame_inferior)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(0, 30))
        self.spinBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #cbcbcb\n"
"")
        self.spinBox.setMaximum(999999)

        self.verticalLayout_3.addWidget(self.spinBox)

        self.frame = QFrame(self.frame_inferior)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 140))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.add_edit_button = QPushButton(self.frame)
        self.add_edit_button.setObjectName(u"add_edit_button")
        self.add_edit_button.setMinimumSize(QSize(0, 45))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(True)
        self.add_edit_button.setFont(font3)
        self.add_edit_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(60, 76, 116);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(30, 38, 57);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.add_edit_button)

        self.cancel_button = QPushButton(self.frame)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(0, 45))
        self.cancel_button.setFont(font3)
        self.cancel_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(148, 52, 68  );\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(97, 35, 45);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.cancel_button)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_7.addWidget(self.frame_inferior)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(add_edit_cliente)

        QMetaObject.connectSlotsByName(add_edit_cliente)
    # setupUi

    def retranslateUi(self, add_edit_cliente):
        add_edit_cliente.setWindowTitle(QCoreApplication.translate("add_edit_cliente", u"Form", None))
        self.label_tittle.setText(QCoreApplication.translate("add_edit_cliente", u"Ajustar Stock", None))
        self.minimize_button.setText(QCoreApplication.translate("add_edit_cliente", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("add_edit_cliente", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("add_edit_cliente", u"...", None))
        self.close_button.setText(QCoreApplication.translate("add_edit_cliente", u"...", None))
        self.codigobarra_title.setText(QCoreApplication.translate("add_edit_cliente", u"PRODUCTO NOMBRE", None))
        self.product_name_label.setText(QCoreApplication.translate("add_edit_cliente", u"product_name", None))
        self.nombre_tittle.setText(QCoreApplication.translate("add_edit_cliente", u"CANTIDAD ACTUAL DE STOCK", None))
        self.stock_actual_label.setText(QCoreApplication.translate("add_edit_cliente", u"stock_actual_label", None))
        self.stock_tittle.setText(QCoreApplication.translate("add_edit_cliente", u"CANTIDAD NUEVA DE STOCK", None))
        self.add_edit_button.setText(QCoreApplication.translate("add_edit_cliente", u"AGREGAR/ACTUALIZAR", None))
        self.cancel_button.setText(QCoreApplication.translate("add_edit_cliente", u"CANCELAR", None))
    # retranslateUi

