# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'horarios.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)

class ViewHorarios(object):
    def setupUi(self, ViewCliente):
        if not ViewCliente.objectName():
            ViewCliente.setObjectName(u"ViewCliente")
        ViewCliente.resize(917, 499)
        self.verticalLayout = QVBoxLayout(ViewCliente)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(ViewCliente)
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
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.guardar_button = QPushButton(self.frame_5)
        self.guardar_button.setObjectName(u"guardar_button")
        self.guardar_button.setMinimumSize(QSize(150, 30))
        font1 = QFont()
        font1.setFamilies([u"Tw Cen MT Condensed Extra Bold"])
        font1.setPointSize(10)
        self.guardar_button.setFont(font1)
        self.guardar_button.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(30, 38, 57);\n"
"	color: white;\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"L:/OneDrive/Escritorio/AngelCuk/assets/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.guardar_button.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.guardar_button)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame = QFrame(self.frame_action)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horarios_table = QTableWidget(self.frame)
        self.horarios_table.setObjectName(u"horarios_table")
        self.horarios_table.setStyleSheet(u"background-color: rgb(235, 235, 235);")

        self.verticalLayout_8.addWidget(self.horarios_table)


        self.verticalLayout_5.addWidget(self.frame)


        self.verticalLayout_7.addWidget(self.frame_action)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(ViewCliente)

        QMetaObject.connectSlotsByName(ViewCliente)
    # setupUi

    def retranslateUi(self, ViewCliente):
        ViewCliente.setWindowTitle(QCoreApplication.translate("ViewCliente", u"Form", None))
        self.label_tittle.setText(QCoreApplication.translate("ViewCliente", u"Barberos Horarios", None))
        self.minimize_button.setText(QCoreApplication.translate("ViewCliente", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("ViewCliente", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("ViewCliente", u"...", None))
        self.close_button.setText(QCoreApplication.translate("ViewCliente", u"...", None))
        self.guardar_button.setText(QCoreApplication.translate("ViewCliente", u"GUARDAR HORARIOS", None))
    # retranslateUi

