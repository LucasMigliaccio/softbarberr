# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

#from ui_files import logo

class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1239, 767)
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(MainWindow)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
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

        self.frame_superior = QFrame(self.content_frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMaximumSize(QSize(16777215, 65))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(212, 172, 13 );\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(154, 125, 10);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.operador_button = QPushButton(self.frame_superior)
        self.operador_button.setObjectName(u"operador_button")
        self.operador_button.setMinimumSize(QSize(220, 0))
        font1 = QFont()
        font1.setFamilies([u"Tw Cen MT Condensed Extra Bold"])
        font1.setPointSize(10)
        self.operador_button.setFont(font1)
        self.operador_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(60, 76, 116 );\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(39, 49, 73 );\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.operador_button)

        self.ceo_button = QPushButton(self.frame_superior)
        self.ceo_button.setObjectName(u"ceo_button")
        self.ceo_button.setMinimumSize(QSize(220, 0))
        self.ceo_button.setFont(font1)
        self.ceo_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(148, 52, 68  );\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(97, 35, 45);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.ceo_button)

        self.horizontalSpacer = QSpacerItem(110, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.recuento_button = QPushButton(self.frame_superior)
        self.recuento_button.setObjectName(u"recuento_button")
        self.recuento_button.setMinimumSize(QSize(35, 0))
        self.recuento_button.setMaximumSize(QSize(16777215, 16777215))
        self.recuento_button.setFont(font1)
        self.recuento_button.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(98, 98, 98);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.recuento_button)


        self.verticalLayout_7.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.content_frame)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_operador = QFrame(self.frame_inferior)
        self.frame_operador.setObjectName(u"frame_operador")
        self.frame_operador.setStyleSheet(u"background-color: rgb(60, 76, 116);")
        self.frame_operador.setFrameShape(QFrame.StyledPanel)
        self.frame_operador.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_operador)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.op_pushButton_cliente = QPushButton(self.frame_operador)
        self.op_pushButton_cliente.setObjectName(u"op_pushButton_cliente")
        self.op_pushButton_cliente.setStyleSheet(u"background-color: rgb(39, 49, 73 );\n"
"color: white;")

        self.verticalLayout_3.addWidget(self.op_pushButton_cliente)

        self.op_pushButton_menu = QPushButton(self.frame_operador)
        self.op_pushButton_menu.setObjectName(u"op_pushButton_menu")
        self.op_pushButton_menu.setMinimumSize(QSize(220, 0))
        self.op_pushButton_menu.setStyleSheet(u"background-color: rgb(39, 49, 73 );\n"
"color: white;")

        self.verticalLayout_3.addWidget(self.op_pushButton_menu)


        self.horizontalLayout.addWidget(self.frame_operador)

        self.frame_cocina = QFrame(self.frame_inferior)
        self.frame_cocina.setObjectName(u"frame_cocina")
        self.frame_cocina.setStyleSheet(u"background-color: rgb(228, 228, 228);")
        self.frame_cocina.setFrameShape(QFrame.StyledPanel)
        self.frame_cocina.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_cocina)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.co_pushButton_menu = QPushButton(self.frame_cocina)
        self.co_pushButton_menu.setObjectName(u"co_pushButton_menu")
        self.co_pushButton_menu.setStyleSheet(u"background-color: rgb(190, 190, 190);\n"
"color: black;")

        self.verticalLayout_4.addWidget(self.co_pushButton_menu)

        self.co_pushButton_menu_2 = QPushButton(self.frame_cocina)
        self.co_pushButton_menu_2.setObjectName(u"co_pushButton_menu_2")
        self.co_pushButton_menu_2.setStyleSheet(u"background-color: rgb(190, 190, 190);\n"
"color: black;")

        self.verticalLayout_4.addWidget(self.co_pushButton_menu_2)

        self.co_pushButton_pedidos = QPushButton(self.frame_cocina)
        self.co_pushButton_pedidos.setObjectName(u"co_pushButton_pedidos")
        self.co_pushButton_pedidos.setMinimumSize(QSize(220, 0))
        self.co_pushButton_pedidos.setStyleSheet(u"background-color: rgb(190, 190, 190);\n"
"color: black;")

        self.verticalLayout_4.addWidget(self.co_pushButton_pedidos)


        self.horizontalLayout.addWidget(self.frame_cocina)

        self.frame_CEO = QFrame(self.frame_inferior)
        self.frame_CEO.setObjectName(u"frame_CEO")
        self.frame_CEO.setStyleSheet(u"background-color: rgb(148, 52, 68);")
        self.frame_CEO.setFrameShape(QFrame.StyledPanel)
        self.frame_CEO.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_CEO)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_8 = QPushButton(self.frame_CEO)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(220, 0))
        self.pushButton_8.setStyleSheet(u"background-color: rgb(97, 35, 45);")

        self.verticalLayout_6.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_CEO)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"background-color: rgb(97, 35, 45);")

        self.verticalLayout_6.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_CEO)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"background-color: rgb(97, 35, 45);")

        self.verticalLayout_6.addWidget(self.pushButton_10)


        self.horizontalLayout.addWidget(self.frame_CEO)

        self.frame_vacio = QFrame(self.frame_inferior)
        self.frame_vacio.setObjectName(u"frame_vacio")
        self.frame_vacio.setStyleSheet(u"background-color: black;")
        self.frame_vacio.setFrameShape(QFrame.StyledPanel)
        self.frame_vacio.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_vacio)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_logo = QLabel(self.frame_vacio)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setStyleSheet(u"QLabel{\n"
"image:url(:/imagess/strip.png);\n"
"}")

        self.verticalLayout_9.addWidget(self.label_logo)


        self.horizontalLayout.addWidget(self.frame_vacio)


        self.verticalLayout_7.addWidget(self.frame_inferior)

        self.frame_action = QFrame(self.content_frame)
        self.frame_action.setObjectName(u"frame_action")
        self.frame_action.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_action.setFrameShape(QFrame.StyledPanel)
        self.frame_action.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_action)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_5 = QFrame(self.frame_action)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.new_request_button = QPushButton(self.frame_5)
        self.new_request_button.setObjectName(u"new_request_button")
        self.new_request_button.setMinimumSize(QSize(150, 30))
        self.new_request_button.setFont(font1)
        self.new_request_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(60, 76, 116);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(30, 38, 57);\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"../../../.designer/assets/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_request_button.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.new_request_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 30))
        self.label.setMaximumSize(QSize(30, 16777215))
        self.label.setStyleSheet(u"background-color: black;\n"
"border-radius: 0px;")
        self.label.setPixmap(QPixmap(u"./assets/icons/search.png"))

        self.horizontalLayout_3.addWidget(self.label)

        self.search_line_edit = QLineEdit(self.frame_5)
        self.search_line_edit.setObjectName(u"search_line_edit")
        self.search_line_edit.setMinimumSize(QSize(0, 30))
        self.search_line_edit.setMaximumSize(QSize(500, 16777215))
        self.search_line_edit.setStyleSheet(u"background-color: white;\n"
"border-radius: 0px;")

        self.horizontalLayout_3.addWidget(self.search_line_edit)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame = QFrame(self.frame_action)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.infopedidos_table = QTableWidget(self.frame)
        self.infopedidos_table.setObjectName(u"infopedidos_table")
        font2 = QFont()
        font2.setPointSize(12)
        self.infopedidos_table.setFont(font2)
        self.infopedidos_table.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.infopedidos_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_8.addWidget(self.infopedidos_table)


        self.verticalLayout_5.addWidget(self.frame)


        self.verticalLayout_7.addWidget(self.frame_action)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.label_tittle.setText(QCoreApplication.translate("MainWindow", u"Barber System", None))
        self.minimize_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.close_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.operador_button.setText(QCoreApplication.translate("MainWindow", u"Operador", None))
        self.ceo_button.setText(QCoreApplication.translate("MainWindow", u"CEO", None))
        self.recuento_button.setText(QCoreApplication.translate("MainWindow", u"RECUENTO", None))
        self.op_pushButton_cliente.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.op_pushButton_menu.setText(QCoreApplication.translate("MainWindow", u"Productos", None))
        self.co_pushButton_menu.setText(QCoreApplication.translate("MainWindow", u"Barberos", None))
        self.co_pushButton_menu_2.setText(QCoreApplication.translate("MainWindow", u"Fichada", None))
        self.co_pushButton_pedidos.setText(QCoreApplication.translate("MainWindow", u"Horarios", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Pr\u00f3ximamente...", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Pr\u00f3ximamente...", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Pr\u00f3ximamente...", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.new_request_button.setText(QCoreApplication.translate("MainWindow", u"Nueva Cita", None))
        self.label.setText("")
        self.search_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Buscar...", None))
    # retranslateUi

