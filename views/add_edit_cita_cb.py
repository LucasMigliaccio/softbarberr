# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_edit_cita_cb.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class AddEditMenu(object):
    def setupUi(self, add_edit_menu):
        if not add_edit_menu.objectName():
            add_edit_menu.setObjectName(u"add_edit_menu")
        add_edit_menu.resize(600, 974)
        add_edit_menu.setMinimumSize(QSize(600, 0))
        add_edit_menu.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(add_edit_menu)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(add_edit_menu)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setMaximumSize(QSize(600, 16777215))
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.central_widget_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
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


        self.verticalLayout.addWidget(self.frame_nav)

        self.frame_inferior = QFrame(self.content_frame)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setMaximumSize(QSize(16777215, 16777215))
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_inferior)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.fecha_tittle = QLabel(self.frame_inferior)
        self.fecha_tittle.setObjectName(u"fecha_tittle")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(False)
        self.fecha_tittle.setFont(font1)
        self.fecha_tittle.setStyleSheet(u"color: rgb(230, 230, 230);")
        self.fecha_tittle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.fecha_tittle)

        self.frame_2 = QFrame(self.frame_inferior)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fechahora_dateTimeEdit = QDateTimeEdit(self.frame_2)
        self.fechahora_dateTimeEdit.setObjectName(u"fechahora_dateTimeEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fechahora_dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.fechahora_dateTimeEdit.setSizePolicy(sizePolicy)
        self.fechahora_dateTimeEdit.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.fechahora_dateTimeEdit.setFont(font2)
        self.fechahora_dateTimeEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #cbcbcb;")
        self.fechahora_dateTimeEdit.setAlignment(Qt.AlignCenter)
        self.fechahora_dateTimeEdit.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))

        self.horizontalLayout_2.addWidget(self.fechahora_dateTimeEdit)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.barbero_tittle = QLabel(self.frame_inferior)
        self.barbero_tittle.setObjectName(u"barbero_tittle")
        self.barbero_tittle.setFont(font1)
        self.barbero_tittle.setStyleSheet(u"color: rgb(230, 230, 230);")
        self.barbero_tittle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.barbero_tittle)

        self.frame_4 = QFrame(self.frame_inferior)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(70, 40))
        self.comboBox.setStyleSheet(u"background-color: white;\n"
"border: 1px solid grey;")

        self.horizontalLayout_7.addWidget(self.comboBox)

        self.pushButton_img_3 = QPushButton(self.frame_4)
        self.pushButton_img_3.setObjectName(u"pushButton_img_3")
        self.pushButton_img_3.setMinimumSize(QSize(40, 40))
        self.pushButton_img_3.setMaximumSize(QSize(40, 40))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(True)
        self.pushButton_img_3.setFont(font3)
        self.pushButton_img_3.setStyleSheet(u"QPushButton {\n"
"background-color: #7c7c7c;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 195, 0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../assets/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_img_3.setIcon(icon4)
        self.pushButton_img_3.setIconSize(QSize(35, 35))

        self.horizontalLayout_7.addWidget(self.pushButton_img_3)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.cliente_tittle = QLabel(self.frame_inferior)
        self.cliente_tittle.setObjectName(u"cliente_tittle")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Black"])
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setItalic(True)
        self.cliente_tittle.setFont(font4)
        self.cliente_tittle.setStyleSheet(u"color: rgb(230, 230, 230);")
        self.cliente_tittle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.cliente_tittle)

        self.frame_3 = QFrame(self.frame_inferior)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.imagen_lineEdit_2 = QLineEdit(self.frame_3)
        self.imagen_lineEdit_2.setObjectName(u"imagen_lineEdit_2")
        self.imagen_lineEdit_2.setMinimumSize(QSize(70, 40))
        self.imagen_lineEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.imagen_lineEdit_2.setStyleSheet(u"background-color: white;\n"
"border: 1px solid grey;")

        self.horizontalLayout_5.addWidget(self.imagen_lineEdit_2)

        self.pushButton_img_2 = QPushButton(self.frame_3)
        self.pushButton_img_2.setObjectName(u"pushButton_img_2")
        self.pushButton_img_2.setMinimumSize(QSize(40, 40))
        self.pushButton_img_2.setMaximumSize(QSize(40, 40))
        self.pushButton_img_2.setFont(font3)
        self.pushButton_img_2.setStyleSheet(u"QPushButton {\n"
"background-color: #7c7c7c;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 195, 0);\n"
"}")
        self.pushButton_img_2.setIcon(icon4)
        self.pushButton_img_2.setIconSize(QSize(35, 35))

        self.horizontalLayout_5.addWidget(self.pushButton_img_2)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.servicio_tittle = QLabel(self.frame_inferior)
        self.servicio_tittle.setObjectName(u"servicio_tittle")
        self.servicio_tittle.setFont(font4)
        self.servicio_tittle.setStyleSheet(u"color: rgb(230, 230, 230);")
        self.servicio_tittle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.servicio_tittle)

        self.servicio_lineEdit = QLineEdit(self.frame_inferior)
        self.servicio_lineEdit.setObjectName(u"servicio_lineEdit")
        self.servicio_lineEdit.setMinimumSize(QSize(400, 40))
        self.servicio_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.servicio_lineEdit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid grey;")

        self.verticalLayout_3.addWidget(self.servicio_lineEdit)

        self.monto_tittle = QLabel(self.frame_inferior)
        self.monto_tittle.setObjectName(u"monto_tittle")
        self.monto_tittle.setFont(font1)
        self.monto_tittle.setStyleSheet(u"color: rgb(230, 230, 230);")
        self.monto_tittle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.monto_tittle)

        self.monto_lineEdit = QLineEdit(self.frame_inferior)
        self.monto_lineEdit.setObjectName(u"monto_lineEdit")
        self.monto_lineEdit.setMinimumSize(QSize(0, 40))
        self.monto_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #cbcbcb;")

        self.verticalLayout_3.addWidget(self.monto_lineEdit)

        self.pago_tittle = QLabel(self.frame_inferior)
        self.pago_tittle.setObjectName(u"pago_tittle")
        self.pago_tittle.setFont(font1)
        self.pago_tittle.setStyleSheet(u"color: rgb(230, 230, 230);")
        self.pago_tittle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.pago_tittle)

        self.pago_comboBox = QComboBox(self.frame_inferior)
        self.pago_comboBox.setObjectName(u"pago_comboBox")
        self.pago_comboBox.setMinimumSize(QSize(0, 40))
        self.pago_comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.pago_comboBox)

        self.estado_tittle = QLabel(self.frame_inferior)
        self.estado_tittle.setObjectName(u"estado_tittle")
        self.estado_tittle.setFont(font1)
        self.estado_tittle.setStyleSheet(u"color: rgb(230, 230, 230);")
        self.estado_tittle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.estado_tittle)

        self.estado_comboBox = QComboBox(self.frame_inferior)
        self.estado_comboBox.setObjectName(u"estado_comboBox")
        self.estado_comboBox.setMinimumSize(QSize(0, 40))
        self.estado_comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.estado_comboBox)

        self.imagen_tittle = QLabel(self.frame_inferior)
        self.imagen_tittle.setObjectName(u"imagen_tittle")
        self.imagen_tittle.setFont(font1)
        self.imagen_tittle.setStyleSheet(u"color: rgb(230, 230, 230);")
        self.imagen_tittle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.imagen_tittle)


        self.verticalLayout.addWidget(self.frame_inferior)

        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.imagen_lineEdit = QLineEdit(self.frame)
        self.imagen_lineEdit.setObjectName(u"imagen_lineEdit")
        self.imagen_lineEdit.setMinimumSize(QSize(70, 40))
        self.imagen_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.imagen_lineEdit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid grey;")

        self.horizontalLayout_4.addWidget(self.imagen_lineEdit)

        self.pushButton_img = QPushButton(self.frame)
        self.pushButton_img.setObjectName(u"pushButton_img")
        self.pushButton_img.setMinimumSize(QSize(40, 40))
        self.pushButton_img.setMaximumSize(QSize(40, 40))
        self.pushButton_img.setFont(font3)
        self.pushButton_img.setStyleSheet(u"QPushButton {\n"
"background-color: #7c7c7c;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 195, 0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../assets/icons/open-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_img.setIcon(icon5)
        self.pushButton_img.setIconSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.pushButton_img)


        self.verticalLayout.addWidget(self.frame)

        self.add_edit_button = QPushButton(self.content_frame)
        self.add_edit_button.setObjectName(u"add_edit_button")
        self.add_edit_button.setMinimumSize(QSize(0, 50))
        self.add_edit_button.setFont(font3)
        self.add_edit_button.setStyleSheet(u"QPushButton {\n"
"background-color: #7c7c7c;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 195, 0);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout.addWidget(self.add_edit_button)

        self.cancel_button = QPushButton(self.content_frame)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(0, 50))
        self.cancel_button.setFont(font3)
        self.cancel_button.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.cancel_button)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.horizontalLayout_3.addWidget(self.background_frame)


        self.horizontalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(add_edit_menu)

        QMetaObject.connectSlotsByName(add_edit_menu)
    # setupUi

    def retranslateUi(self, add_edit_menu):
        add_edit_menu.setWindowTitle(QCoreApplication.translate("add_edit_menu", u"Form", None))
        self.label_tittle.setText(QCoreApplication.translate("add_edit_menu", u"Cita Agregar", None))
        self.minimize_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.close_button.setText(QCoreApplication.translate("add_edit_menu", u"...", None))
        self.fecha_tittle.setText(QCoreApplication.translate("add_edit_menu", u"FECHA Y HORA", None))
        self.barbero_tittle.setText(QCoreApplication.translate("add_edit_menu", u"BARBERO", None))
        self.pushButton_img_3.setText("")
        self.cliente_tittle.setText(QCoreApplication.translate("add_edit_menu", u"CLIENTE", None))
        self.pushButton_img_2.setText("")
        self.servicio_tittle.setText(QCoreApplication.translate("add_edit_menu", u"SERVICIOS PROGRAMADOS", None))
        self.monto_tittle.setText(QCoreApplication.translate("add_edit_menu", u"MONTO", None))
        self.pago_tittle.setText(QCoreApplication.translate("add_edit_menu", u"METODO DE PAGO", None))
        self.estado_tittle.setText(QCoreApplication.translate("add_edit_menu", u"ESTADO", None))
        self.imagen_tittle.setText(QCoreApplication.translate("add_edit_menu", u"IMAGEN", None))
        self.pushButton_img.setText("")
        self.add_edit_button.setText(QCoreApplication.translate("add_edit_menu", u"AGREGAR/ACTUALIZAR", None))
        self.cancel_button.setText(QCoreApplication.translate("add_edit_menu", u"CANCELAR", None))
    # retranslateUi

