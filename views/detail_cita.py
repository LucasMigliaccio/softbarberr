# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detail_cita.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)

class DetailsCita(object):
    def setupUi(self, add_edit_menu):
        if not add_edit_menu.objectName():
            add_edit_menu.setObjectName(u"add_edit_menu")
        add_edit_menu.resize(600, 906)
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
        self.verticalLayout_2 = QVBoxLayout(self.content_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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


        self.verticalLayout_2.addWidget(self.frame_nav)

        self.frame_inferior = QFrame(self.content_frame)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setMinimumSize(QSize(0, 60))
        self.frame_inferior.setMaximumSize(QSize(16777215, 16777215))
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_inferior)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_fecha_hora = QFrame(self.frame_inferior)
        self.frame_fecha_hora.setObjectName(u"frame_fecha_hora")
        self.frame_fecha_hora.setFrameShape(QFrame.StyledPanel)
        self.frame_fecha_hora.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_fecha_hora)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pedido_tittle_7 = QLabel(self.frame_fecha_hora)
        self.pedido_tittle_7.setObjectName(u"pedido_tittle_7")
        font1 = QFont()
        font1.setFamilies([u"Algerian"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.pedido_tittle_7.setFont(font1)
        self.pedido_tittle_7.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 16pt \"Algerian\";")
        self.pedido_tittle_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.pedido_tittle_7, 0, 0, 3, 1)

        self.cita_id_label = QLabel(self.frame_fecha_hora)
        self.cita_id_label.setObjectName(u"cita_id_label")
        font2 = QFont()
        font2.setFamilies([u"impact"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.cita_id_label.setFont(font2)
        self.cita_id_label.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"font: 12pt \"impact\";")
        self.cita_id_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.cita_id_label, 2, 1, 3, 1)

        self.fechahora_label = QLabel(self.frame_fecha_hora)
        self.fechahora_label.setObjectName(u"fechahora_label")
        self.fechahora_label.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"font: 12pt \"impact\";")
        self.fechahora_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.fechahora_label, 3, 0, 1, 1)

        self.pedido_tittle = QLabel(self.frame_fecha_hora)
        self.pedido_tittle.setObjectName(u"pedido_tittle")
        self.pedido_tittle.setFont(font1)
        self.pedido_tittle.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 16pt \"Algerian\";")
        self.pedido_tittle.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.pedido_tittle, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_fecha_hora)

        self.frame_barbero = QFrame(self.frame_inferior)
        self.frame_barbero.setObjectName(u"frame_barbero")
        self.frame_barbero.setFrameShape(QFrame.StyledPanel)
        self.frame_barbero.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_barbero)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pedido_tittle_2 = QLabel(self.frame_barbero)
        self.pedido_tittle_2.setObjectName(u"pedido_tittle_2")
        self.pedido_tittle_2.setFont(font1)
        self.pedido_tittle_2.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 16pt \"Algerian\";")
        self.pedido_tittle_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.pedido_tittle_2, 0, 0, 1, 1)

        self.pedido_tittle_3 = QLabel(self.frame_barbero)
        self.pedido_tittle_3.setObjectName(u"pedido_tittle_3")
        self.pedido_tittle_3.setFont(font1)
        self.pedido_tittle_3.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 16pt \"Algerian\";")
        self.pedido_tittle_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.pedido_tittle_3, 0, 1, 1, 1)

        self.cliente_label = QLabel(self.frame_barbero)
        self.cliente_label.setObjectName(u"cliente_label")
        self.cliente_label.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"font: 12pt \"impact\";")
        self.cliente_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.cliente_label, 1, 0, 1, 1)

        self.barbero_label = QLabel(self.frame_barbero)
        self.barbero_label.setObjectName(u"barbero_label")
        self.barbero_label.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"font: 12pt \"impact\";")
        self.barbero_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.barbero_label, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_barbero)

        self.frame_cliente = QFrame(self.frame_inferior)
        self.frame_cliente.setObjectName(u"frame_cliente")
        self.frame_cliente.setMinimumSize(QSize(0, 90))
        self.frame_cliente.setFrameShape(QFrame.StyledPanel)
        self.frame_cliente.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_cliente)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pedido_tittle_6 = QLabel(self.frame_cliente)
        self.pedido_tittle_6.setObjectName(u"pedido_tittle_6")
        self.pedido_tittle_6.setFont(font1)
        self.pedido_tittle_6.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 16pt \"Algerian\";")
        self.pedido_tittle_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.pedido_tittle_6, 0, 1, 1, 1)

        self.telefono_label = QLabel(self.frame_cliente)
        self.telefono_label.setObjectName(u"telefono_label")
        self.telefono_label.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"font: 12pt \"impact\";")
        self.telefono_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.telefono_label, 1, 0, 1, 1)

        self.pedido_tittle_5 = QLabel(self.frame_cliente)
        self.pedido_tittle_5.setObjectName(u"pedido_tittle_5")
        self.pedido_tittle_5.setFont(font1)
        self.pedido_tittle_5.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 16pt \"Algerian\";")
        self.pedido_tittle_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.pedido_tittle_5, 0, 0, 1, 1)

        self.direccion_label = QLabel(self.frame_cliente)
        self.direccion_label.setObjectName(u"direccion_label")
        self.direccion_label.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"font: 12pt \"impact\";")
        self.direccion_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.direccion_label, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_cliente)

        self.frame_pago = QFrame(self.frame_inferior)
        self.frame_pago.setObjectName(u"frame_pago")
        self.frame_pago.setFrameShape(QFrame.StyledPanel)
        self.frame_pago.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_pago)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.metodo_pago_label = QLabel(self.frame_pago)
        self.metodo_pago_label.setObjectName(u"metodo_pago_label")
        self.metodo_pago_label.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"font: 12pt \"impact\";")
        self.metodo_pago_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.metodo_pago_label, 1, 2, 1, 1)

        self.pedido_tittle_8 = QLabel(self.frame_pago)
        self.pedido_tittle_8.setObjectName(u"pedido_tittle_8")
        self.pedido_tittle_8.setFont(font1)
        self.pedido_tittle_8.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 16pt \"Algerian\";")
        self.pedido_tittle_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.pedido_tittle_8, 0, 0, 1, 1)

        self.pedido_tittle_4 = QLabel(self.frame_pago)
        self.pedido_tittle_4.setObjectName(u"pedido_tittle_4")
        self.pedido_tittle_4.setFont(font1)
        self.pedido_tittle_4.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 16pt \"Algerian\";")
        self.pedido_tittle_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.pedido_tittle_4, 0, 1, 1, 1)

        self.pedido_tittle_9 = QLabel(self.frame_pago)
        self.pedido_tittle_9.setObjectName(u"pedido_tittle_9")
        self.pedido_tittle_9.setFont(font1)
        self.pedido_tittle_9.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 16pt \"Algerian\";")
        self.pedido_tittle_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.pedido_tittle_9, 0, 2, 1, 1)

        self.estado_label = QLabel(self.frame_pago)
        self.estado_label.setObjectName(u"estado_label")
        self.estado_label.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"font: 12pt \"impact\";")
        self.estado_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.estado_label, 1, 0, 1, 1)

        self.monto_label = QLabel(self.frame_pago)
        self.monto_label.setObjectName(u"monto_label")
        self.monto_label.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"font: 12pt \"impact\";")
        self.monto_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.monto_label, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_pago)


        self.verticalLayout_2.addWidget(self.frame_inferior)

        self.frame_img = QFrame(self.content_frame)
        self.frame_img.setObjectName(u"frame_img")
        self.frame_img.setFrameShape(QFrame.StyledPanel)
        self.frame_img.setFrameShadow(QFrame.Raised)
        self.img_label = QLabel(self.frame_img)
        self.img_label.setObjectName(u"img_label")
        self.img_label.setGeometry(QRect(10, 10, 541, 351))
        self.img_label.setMinimumSize(QSize(540, 350))

        self.verticalLayout_2.addWidget(self.frame_img)

        self.add_edit_button_2 = QPushButton(self.content_frame)
        self.add_edit_button_2.setObjectName(u"add_edit_button_2")
        self.add_edit_button_2.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(True)
        self.add_edit_button_2.setFont(font3)
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

        self.verticalLayout_2.addWidget(self.add_edit_button_2)


        self.horizontalLayout.addWidget(self.content_frame)


        self.gridLayout_2.addWidget(self.background_frame, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.central_widget_frame, 0, 0, 1, 1)


        self.retranslateUi(add_edit_menu)

        QMetaObject.connectSlotsByName(add_edit_menu)
    # setupUi

    def retranslateUi(self, add_edit_menu):
        add_edit_menu.setWindowTitle(QCoreApplication.translate("add_edit_menu", u"Form", None))
        self.label_tittle.setText(QCoreApplication.translate("add_edit_menu", u"Cita Detalle", None))
        self.minimize_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.close_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.pedido_tittle_7.setText(QCoreApplication.translate("add_edit_menu", u"FECHA Y HORA", None))
        self.cita_id_label.setText(QCoreApplication.translate("add_edit_menu", u"TextLabel", None))
        self.fechahora_label.setText(QCoreApplication.translate("add_edit_menu", u"TextLabel", None))
        self.pedido_tittle.setText(QCoreApplication.translate("add_edit_menu", u"C\u00d3DIGO CITA", None))
        self.pedido_tittle_2.setText(QCoreApplication.translate("add_edit_menu", u"CLIENTE", None))
        self.pedido_tittle_3.setText(QCoreApplication.translate("add_edit_menu", u"BARBERO", None))
        self.cliente_label.setText(QCoreApplication.translate("add_edit_menu", u"TextLabel", None))
        self.barbero_label.setText(QCoreApplication.translate("add_edit_menu", u"TextLabel", None))
        self.pedido_tittle_6.setText(QCoreApplication.translate("add_edit_menu", u"DIRECCI\u00d3N CLIENTE", None))
        self.telefono_label.setText(QCoreApplication.translate("add_edit_menu", u"TELEFONO CLIENTE", None))
        self.pedido_tittle_5.setText(QCoreApplication.translate("add_edit_menu", u"TELEFONO CLIENTE", None))
        self.direccion_label.setText(QCoreApplication.translate("add_edit_menu", u"Direcci\u00f3n cliente", None))
        self.metodo_pago_label.setText(QCoreApplication.translate("add_edit_menu", u"TextLabel", None))
        self.pedido_tittle_8.setText(QCoreApplication.translate("add_edit_menu", u"ESTADO", None))
        self.pedido_tittle_4.setText(QCoreApplication.translate("add_edit_menu", u"MONTO", None))
        self.pedido_tittle_9.setText(QCoreApplication.translate("add_edit_menu", u"METODO DE PAGO", None))
        self.estado_label.setText(QCoreApplication.translate("add_edit_menu", u"TextLabel", None))
        self.monto_label.setText(QCoreApplication.translate("add_edit_menu", u"TextLabel", None))
        self.img_label.setText(QCoreApplication.translate("add_edit_menu", u"TextLabel", None))
        self.add_edit_button_2.setText(QCoreApplication.translate("add_edit_menu", u"SALIR", None))
    # retranslateUi

