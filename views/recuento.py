# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recuento.ui'
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
    QLabel, QLineEdit, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)
#import logo_rc

class RecuentoDetailWindow(object):
    def setupUi(self, DetailWindow):
        if not DetailWindow.objectName():
            DetailWindow.setObjectName(u"DetailWindow")
        DetailWindow.resize(984, 655)
        self.gridLayout = QGridLayout(DetailWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(DetailWindow)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(21, 21, 21);")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.background_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_nav = QFrame(self.background_frame)
        self.frame_nav.setObjectName(u"frame_nav")
        self.frame_nav.setMinimumSize(QSize(0, 40))
        self.frame_nav.setMaximumSize(QSize(16777215, 40))
        self.frame_nav.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_nav.setFrameShape(QFrame.StyledPanel)
        self.frame_nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_nav)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_tittle = QLabel(self.frame_nav)
        self.label_tittle.setObjectName(u"label_tittle")
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        self.label_tittle.setFont(font)
        self.label_tittle.setStyleSheet(u"color: rgb(255, 255, 0);")

        self.horizontalLayout_7.addWidget(self.label_tittle)

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

        self.horizontalLayout_7.addWidget(self.butttons_holder_frame)


        self.verticalLayout_6.addWidget(self.frame_nav)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content_frame)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 125))
        self.frame.setStyleSheet(u"background-color: rgb(21, 21, 21);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"\n"
"color: rgb(255, 255, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.fecha_lineEdit = QLineEdit(self.frame)
        self.fecha_lineEdit.setObjectName(u"fecha_lineEdit")
        self.fecha_lineEdit.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Black"])
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setItalic(True)
        self.fecha_lineEdit.setFont(font2)
        self.fecha_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #cbcbcb;\n"
"font: 87 italic 18pt \"Segoe UI Black\";")
        self.fecha_lineEdit.setMaxLength(32764)
        self.fecha_lineEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.verticalLayout_3.addWidget(self.fecha_lineEdit)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.content_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 15px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mp_ico_label = QLabel(self.frame_3)
        self.mp_ico_label.setObjectName(u"mp_ico_label")
        self.mp_ico_label.setStyleSheet(u"image: url(:/imagess/mercadopago.png);")

        self.horizontalLayout_2.addWidget(self.mp_ico_label)

        self.mp_namelabel = QLabel(self.frame_3)
        self.mp_namelabel.setObjectName(u"mp_namelabel")
        self.mp_namelabel.setStyleSheet(u"\n"
"color: rgb(255, 255, 0);\n"
"font: 87 16pt \"Segoe UI Black\";")

        self.horizontalLayout_2.addWidget(self.mp_namelabel)

        self.mp_label = QLabel(self.frame_3)
        self.mp_label.setObjectName(u"mp_label")
        self.mp_label.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 87 16pt \"Segoe UI Black\";")

        self.horizontalLayout_2.addWidget(self.mp_label)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 15px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.efec_ico_label = QLabel(self.frame_4)
        self.efec_ico_label.setObjectName(u"efec_ico_label")
        self.efec_ico_label.setStyleSheet(u"image: url(:/imagess/efectivo.png);")

        self.horizontalLayout.addWidget(self.efec_ico_label)

        self.efec_namelabel = QLabel(self.frame_4)
        self.efec_namelabel.setObjectName(u"efec_namelabel")
        self.efec_namelabel.setStyleSheet(u"\n"
"color: rgb(255, 255, 0);\n"
"font: 87 16pt \"Segoe UI Black\";")

        self.horizontalLayout.addWidget(self.efec_namelabel)

        self.efec_label = QLabel(self.frame_4)
        self.efec_label.setObjectName(u"efec_label")
        self.efec_label.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 87 16pt \"Segoe UI Black\";")

        self.horizontalLayout.addWidget(self.efec_label)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 15px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gastos_namelabel = QLabel(self.frame_7)
        self.gastos_namelabel.setObjectName(u"gastos_namelabel")
        self.gastos_namelabel.setStyleSheet(u"\n"
"color: rgb(255, 255, 0);\n"
"font: 87 16pt \"Segoe UI Black\";")
        self.gastos_namelabel.setScaledContents(False)
        self.gastos_namelabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.gastos_namelabel)

        self.gastos_lineEdit = QLineEdit(self.frame_7)
        self.gastos_lineEdit.setObjectName(u"gastos_lineEdit")
        self.gastos_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #cbcbcb;\n"
"font: 87 italic 18pt \"Segoe UI Black\";")

        self.verticalLayout.addWidget(self.gastos_lineEdit)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 15px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.total_namelabel = QLabel(self.frame_8)
        self.total_namelabel.setObjectName(u"total_namelabel")
        self.total_namelabel.setStyleSheet(u"color: rgb(255, 255, 0);\n"
"font: 87 16pt \"Segoe UI Black\";")
        self.total_namelabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.total_namelabel)

        self.total_label = QLabel(self.frame_8)
        self.total_label.setObjectName(u"total_label")
        self.total_label.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 87 16pt \"Segoe UI Black\";")

        self.horizontalLayout_3.addWidget(self.total_label)


        self.verticalLayout_4.addWidget(self.frame_8)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout_6.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.gridLayout.addWidget(self.central_widget_frame, 0, 0, 1, 1)


        self.retranslateUi(DetailWindow)

        QMetaObject.connectSlotsByName(DetailWindow)
    # setupUi

    def retranslateUi(self, DetailWindow):
        DetailWindow.setWindowTitle(QCoreApplication.translate("DetailWindow", u"Form", None))
        self.label_tittle.setText(QCoreApplication.translate("DetailWindow", u"Cierre Caja", None))
        self.minimize_button.setText(QCoreApplication.translate("DetailWindow", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("DetailWindow", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("DetailWindow", u"...", None))
        self.close_button.setText(QCoreApplication.translate("DetailWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("DetailWindow", u"INGRESA UNA FECHA V\u00c1LIDA", None))
        self.fecha_lineEdit.setText("")
        self.fecha_lineEdit.setPlaceholderText(QCoreApplication.translate("DetailWindow", u"(DD-MM-AAAA)", None))
        self.mp_ico_label.setText("")
        self.mp_namelabel.setText(QCoreApplication.translate("DetailWindow", u"MERCADO PAGO :", None))
        self.mp_label.setText("")
        self.efec_ico_label.setText("")
        self.efec_namelabel.setText(QCoreApplication.translate("DetailWindow", u"EFECTIVO :", None))
        self.efec_label.setText("")
        self.gastos_namelabel.setText(QCoreApplication.translate("DetailWindow", u"GASTOS DEL DIA:", None))
        self.total_namelabel.setText(QCoreApplication.translate("DetailWindow", u"TOTAL:", None))
        self.total_label.setText("")
    # retranslateUi

