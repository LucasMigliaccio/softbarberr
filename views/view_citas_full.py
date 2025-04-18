# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_citas_full.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableView,
    QToolButton, QVBoxLayout, QWidget)
from ui_files import icons

class ViewCitasFull(object):
    def setupUi(self, ViewEmpleado):
        if not ViewEmpleado.objectName():
            ViewEmpleado.setObjectName(u"ViewEmpleado")
        ViewEmpleado.resize(947, 574)
        self.verticalLayout = QVBoxLayout(ViewEmpleado)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(ViewEmpleado)
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
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
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
        icon.addFile(u":/newPrefix/assets/icons/minimize-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_button.setIcon(icon)
        self.restore_button = QToolButton(self.butttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(30, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/icons/restore-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restore_button.setIcon(icon1)
        self.maximize_button = QToolButton(self.butttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(30, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/assets/icons/maximize-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximize_button.setIcon(icon2)
        self.close_button = QToolButton(self.butttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(60, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/assets/icons/close-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_button.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.butttons_holder_frame)


        self.verticalLayout_7.addWidget(self.frame_nav)

        self.frame_action = QFrame(self.content_frame)
        self.frame_action.setObjectName(u"frame_action")
        self.frame_action.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_action.setFrameShape(QFrame.StyledPanel)
        self.frame_action.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_action)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.frame_action)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.marcas_table = QTableView(self.frame)
        self.marcas_table.setObjectName(u"marcas_table")
        self.marcas_table.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;")

        self.horizontalLayout.addWidget(self.marcas_table)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(24, 24, 24);\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.edit_pushButton = QPushButton(self.frame_3)
        self.edit_pushButton.setObjectName(u"edit_pushButton")
        self.edit_pushButton.setMinimumSize(QSize(0, 175))
        self.edit_pushButton.setStyleSheet(u"background-color: rgb(34, 34, 34);\n"
"border-radius: 10px;")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/assets/icons/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.edit_pushButton.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.edit_pushButton)

        self.delete_pushButton = QPushButton(self.frame_3)
        self.delete_pushButton.setObjectName(u"delete_pushButton")
        self.delete_pushButton.setMinimumSize(QSize(0, 175))
        self.delete_pushButton.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(34, 34, 34);")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/assets/icons/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_pushButton.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.delete_pushButton)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_action)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 11, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color:white;")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_7.addWidget(self.frame_action)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(ViewEmpleado)

        QMetaObject.connectSlotsByName(ViewEmpleado)
    # setupUi

    def retranslateUi(self, ViewEmpleado):
        ViewEmpleado.setWindowTitle(QCoreApplication.translate("ViewEmpleado", u"Form", None))
        self.label_tittle.setText(QCoreApplication.translate("ViewEmpleado", u"Ver m\u00e1s Citas", None))
        self.minimize_button.setText(QCoreApplication.translate("ViewEmpleado", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("ViewEmpleado", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("ViewEmpleado", u"...", None))
        self.close_button.setText(QCoreApplication.translate("ViewEmpleado", u"...", None))
        self.edit_pushButton.setText("")
        self.delete_pushButton.setText("")
        self.label.setText(QCoreApplication.translate("ViewEmpleado", u"lucasmigliaccio10@gmail.com", None))
    # retranslateUi

