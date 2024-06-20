# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detail_producto.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class DetailProducto(object):
    def setupUi(self, add_edit_menu):
        if not add_edit_menu.objectName():
            add_edit_menu.setObjectName(u"add_edit_menu")
        add_edit_menu.resize(600, 802)
        add_edit_menu.setMinimumSize(QSize(600, 0))
        add_edit_menu.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(add_edit_menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(add_edit_menu)
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
        icon.addFile(u"./assets/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.restore_button = QToolButton(self.butttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(30, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.maximize_button = QToolButton(self.butttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(30, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.close_button = QToolButton(self.butttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(60, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.butttons_holder_frame)


        self.verticalLayout_7.addWidget(self.frame_nav)

        self.frame_inferior = QFrame(self.content_frame)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setMinimumSize(QSize(10, 0))
        self.frame_inferior.setMaximumSize(QSize(16777215, 16777215))
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_inferior)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.frame_inferior)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pedido_tittle_10 = QLabel(self.frame_13)
        self.pedido_tittle_10.setObjectName(u"pedido_tittle_10")
        font1 = QFont()
        font1.setFamilies([u"Algerian"])
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        self.pedido_tittle_10.setFont(font1)
        self.pedido_tittle_10.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 18pt \"Algerian\";")
        self.pedido_tittle_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.pedido_tittle_10)

        self.idproducto_label = QLabel(self.frame_13)
        self.idproducto_label.setObjectName(u"idproducto_label")
        self.idproducto_label.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"font: 12pt \"impact\";")
        self.idproducto_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.idproducto_label)


        self.horizontalLayout_4.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_14)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pedido_tittle_11 = QLabel(self.frame_14)
        self.pedido_tittle_11.setObjectName(u"pedido_tittle_11")
        self.pedido_tittle_11.setFont(font1)
        self.pedido_tittle_11.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 18pt \"Algerian\";")
        self.pedido_tittle_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.pedido_tittle_11)

        self.nombre_label = QLabel(self.frame_14)
        self.nombre_label.setObjectName(u"nombre_label")
        self.nombre_label.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"font: 12pt \"impact\";")
        self.nombre_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.nombre_label)


        self.horizontalLayout_4.addWidget(self.frame_14)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pedido_tittle_4 = QLabel(self.frame_4)
        self.pedido_tittle_4.setObjectName(u"pedido_tittle_4")
        self.pedido_tittle_4.setFont(font1)
        self.pedido_tittle_4.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 18pt \"Algerian\";")
        self.pedido_tittle_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.pedido_tittle_4)

        self.numero_label = QLabel(self.frame_4)
        self.numero_label.setObjectName(u"numero_label")
        self.numero_label.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"font: 12pt \"impact\";")
        self.numero_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.numero_label)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pedido_tittle_5 = QLabel(self.frame_6)
        self.pedido_tittle_5.setObjectName(u"pedido_tittle_5")
        self.pedido_tittle_5.setFont(font1)
        self.pedido_tittle_5.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 18pt \"Algerian\";")
        self.pedido_tittle_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.pedido_tittle_5)

        self.stock_label = QLabel(self.frame_6)
        self.stock_label.setObjectName(u"stock_label")
        self.stock_label.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"font: 12pt \"impact\";")
        self.stock_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.stock_label)


        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pedido_tittle_8 = QLabel(self.frame_10)
        self.pedido_tittle_8.setObjectName(u"pedido_tittle_8")
        font2 = QFont()
        font2.setFamilies([u"Algerian"])
        font2.setPointSize(17)
        font2.setBold(False)
        font2.setItalic(False)
        self.pedido_tittle_8.setFont(font2)
        self.pedido_tittle_8.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 17pt \"Algerian\";")
        self.pedido_tittle_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.pedido_tittle_8)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.descripcion_plainTextEdit = QPlainTextEdit(self.frame_10)
        self.descripcion_plainTextEdit.setObjectName(u"descripcion_plainTextEdit")
        self.descripcion_plainTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #cbcbcb\n"
"")

        self.verticalLayout_11.addWidget(self.descripcion_plainTextEdit)


        self.horizontalLayout_3.addWidget(self.frame_10)


        self.verticalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_3.addWidget(self.frame)

        self.add_edit_button_2 = QPushButton(self.frame_inferior)
        self.add_edit_button_2.setObjectName(u"add_edit_button_2")
        self.add_edit_button_2.setMinimumSize(QSize(550, 50))
        self.add_edit_button_2.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(True)
        self.add_edit_button_2.setFont(font3)
        self.add_edit_button_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(148, 52, 68  );\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(97, 35, 45);\n"
"}\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.add_edit_button_2)


        self.verticalLayout_7.addWidget(self.frame_inferior)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(add_edit_menu)

        QMetaObject.connectSlotsByName(add_edit_menu)
    # setupUi

    def retranslateUi(self, add_edit_menu):
        add_edit_menu.setWindowTitle(QCoreApplication.translate("add_edit_menu", u"Form", None))
        self.label_tittle.setText(QCoreApplication.translate("add_edit_menu", u"Producto Detalle", None))
        self.minimize_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.close_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.pedido_tittle_10.setText(QCoreApplication.translate("add_edit_menu", u"ID PRODUCTO", None))
        self.idproducto_label.setText(QCoreApplication.translate("add_edit_menu", u"TextLabel", None))
        self.pedido_tittle_11.setText(QCoreApplication.translate("add_edit_menu", u"NOMBRE", None))
        self.nombre_label.setText(QCoreApplication.translate("add_edit_menu", u"TextLabel", None))
        self.pedido_tittle_4.setText(QCoreApplication.translate("add_edit_menu", u"PRECIO", None))
        self.numero_label.setText(QCoreApplication.translate("add_edit_menu", u"TextLabel", None))
        self.pedido_tittle_5.setText(QCoreApplication.translate("add_edit_menu", u"CANTIDAD DE STOCK", None))
        self.stock_label.setText(QCoreApplication.translate("add_edit_menu", u"TextLabel", None))
        self.pedido_tittle_8.setText(QCoreApplication.translate("add_edit_menu", u"DESCRIPCI\u00d3N", None))
        self.add_edit_button_2.setText(QCoreApplication.translate("add_edit_menu", u"SALIR", None))
    # retranslateUi

