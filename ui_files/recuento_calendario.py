# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recuento_calendario.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QToolButton, QVBoxLayout, QWidget)
from ui_files import icons

class RecuentoDetailWindow(object):
    def setupUi(self, DetailWindow):
        if not DetailWindow.objectName():
            DetailWindow.setObjectName(u"DetailWindow")
        DetailWindow.resize(923, 862)
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
        self.frame.setMinimumSize(QSize(0, 25))
        self.frame.setMaximumSize(QSize(16777215, 15))
        self.frame.setStyleSheet(u"background-color: rgb(21, 21, 21);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 4)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"\n"
"color: rgb(255, 255, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame)

        self.calendarWidget = QCalendarWidget(self.content_frame)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMaximumSize(QSize(16777215, 300))
        self.calendarWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #cbcbcb;\n"
"color: rgb(0,0,0)\n"
"")

        self.verticalLayout_2.addWidget(self.calendarWidget)

        self.frame_2 = QFrame(self.content_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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
        self.mp_ico_label.setStyleSheet(u"image: url(:/prefijoNuevo/assets/icons/mercadopago.png);")

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

        self.mp_segna_namelabel = QLabel(self.frame_3)
        self.mp_segna_namelabel.setObjectName(u"mp_segna_namelabel")
        self.mp_segna_namelabel.setStyleSheet(u"\n"
"color: rgb(255, 255, 0);\n"
"font: 87 16pt \"Segoe UI Black\";")

        self.horizontalLayout_2.addWidget(self.mp_segna_namelabel)

        self.mp_segna_label = QLabel(self.frame_3)
        self.mp_segna_label.setObjectName(u"mp_segna_label")
        self.mp_segna_label.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 87 16pt \"Segoe UI Black\";")

        self.horizontalLayout_2.addWidget(self.mp_segna_label)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 15px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.efec_ico_label = QLabel(self.frame_4)
        self.efec_ico_label.setObjectName(u"efec_ico_label")
        self.efec_ico_label.setStyleSheet(u"image: url(:/prefijoNuevo/assets/icons/efectivo.png);")

        self.horizontalLayout_4.addWidget(self.efec_ico_label)

        self.efec_namelabel = QLabel(self.frame_4)
        self.efec_namelabel.setObjectName(u"efec_namelabel")
        self.efec_namelabel.setStyleSheet(u"\n"
"color: rgb(255, 255, 0);\n"
"font: 87 16pt \"Segoe UI Black\";")

        self.horizontalLayout_4.addWidget(self.efec_namelabel)

        self.efec_label = QLabel(self.frame_4)
        self.efec_label.setObjectName(u"efec_label")
        self.efec_label.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 87 16pt \"Segoe UI Black\";")

        self.horizontalLayout_4.addWidget(self.efec_label)

        self.efec_segna_namelabel = QLabel(self.frame_4)
        self.efec_segna_namelabel.setObjectName(u"efec_segna_namelabel")
        self.efec_segna_namelabel.setStyleSheet(u"\n"
"color: rgb(255, 255, 0);\n"
"font: 87 16pt \"Segoe UI Black\";")

        self.horizontalLayout_4.addWidget(self.efec_segna_namelabel)

        self.efec_segna_label_ = QLabel(self.frame_4)
        self.efec_segna_label_.setObjectName(u"efec_segna_label_")
        self.efec_segna_label_.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 87 16pt \"Segoe UI Black\";")

        self.horizontalLayout_4.addWidget(self.efec_segna_label_)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 15px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.transfe_ico_label = QLabel(self.frame_6)
        self.transfe_ico_label.setObjectName(u"transfe_ico_label")
        self.transfe_ico_label.setStyleSheet(u"image: url(:/prefijoNuevo/assets/icons/banco.png);")

        self.horizontalLayout_5.addWidget(self.transfe_ico_label)

        self.transfe_namelabel = QLabel(self.frame_6)
        self.transfe_namelabel.setObjectName(u"transfe_namelabel")
        self.transfe_namelabel.setStyleSheet(u"\n"
"color: rgb(255, 255, 0);\n"
"font: 87 16pt \"Segoe UI Black\";")

        self.horizontalLayout_5.addWidget(self.transfe_namelabel)

        self.transfe_label = QLabel(self.frame_6)
        self.transfe_label.setObjectName(u"transfe_label")
        self.transfe_label.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 87 16pt \"Segoe UI Black\";")

        self.horizontalLayout_5.addWidget(self.transfe_label)

        self.transfe_segna_namelabel = QLabel(self.frame_6)
        self.transfe_segna_namelabel.setObjectName(u"transfe_segna_namelabel")
        self.transfe_segna_namelabel.setStyleSheet(u"\n"
"color: rgb(255, 255, 0);\n"
"font: 87 16pt \"Segoe UI Black\";")

        self.horizontalLayout_5.addWidget(self.transfe_segna_namelabel)

        self.transfe_segna_label = QLabel(self.frame_6)
        self.transfe_segna_label.setObjectName(u"transfe_segna_label")
        self.transfe_segna_label.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 87 16pt \"Segoe UI Black\";")

        self.horizontalLayout_5.addWidget(self.transfe_segna_label)


        self.verticalLayout_4.addWidget(self.frame_6)

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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
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

        self.frame_table = QFrame(self.frame_5)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setMinimumSize(QSize(0, 75))
        self.frame_table.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 15px;")
        self.frame_table.setFrameShape(QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_table)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.total_monto_pendiente_edit = QLabel(self.frame_table)
        self.total_monto_pendiente_edit.setObjectName(u"total_monto_pendiente_edit")
        self.total_monto_pendiente_edit.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font:  9pt \"Segoe UI Black\";")

        self.gridLayout_2.addWidget(self.total_monto_pendiente_edit, 0, 3, 1, 1)

        self.total_pendiente_cobro_edit = QLabel(self.frame_table)
        self.total_pendiente_cobro_edit.setObjectName(u"total_pendiente_cobro_edit")
        self.total_pendiente_cobro_edit.setStyleSheet(u"color: rgb(170, 0, 0);\n"
"font: 87 9pt \"Segoe UI Black\";")

        self.gridLayout_2.addWidget(self.total_pendiente_cobro_edit, 0, 5, 1, 1)

        self.total_pendiente_cobro_label = QLabel(self.frame_table)
        self.total_pendiente_cobro_label.setObjectName(u"total_pendiente_cobro_label")
        self.total_pendiente_cobro_label.setStyleSheet(u"color: rgb(255, 255, 0);\n"
"font: 87 9pt \"Segoe UI Black\";")

        self.gridLayout_2.addWidget(self.total_pendiente_cobro_label, 0, 4, 1, 1)

        self.total_monto_segna_label = QLabel(self.frame_table)
        self.total_monto_segna_label.setObjectName(u"total_monto_segna_label")
        self.total_monto_segna_label.setStyleSheet(u"color: rgb(255, 255, 0);\n"
"font: 87 9pt \"Segoe UI Black\";")

        self.gridLayout_2.addWidget(self.total_monto_segna_label, 0, 2, 1, 1)

        self.total_monto_label = QLabel(self.frame_table)
        self.total_monto_label.setObjectName(u"total_monto_label")
        self.total_monto_label.setStyleSheet(u"color: rgb(255, 255, 0);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")

        self.gridLayout_2.addWidget(self.total_monto_label, 0, 7, 1, 1)

        self.total_monto_edit = QLabel(self.frame_table)
        self.total_monto_edit.setObjectName(u"total_monto_edit")
        self.total_monto_edit.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 87 9pt \"Segoe UI Black\";")

        self.gridLayout_2.addWidget(self.total_monto_edit, 0, 8, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_table)


        self.horizontalLayout.addWidget(self.frame_5)


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
        self.mp_ico_label.setText("")
        self.mp_namelabel.setText(QCoreApplication.translate("DetailWindow", u"MERCADO PAGO :", None))
        self.mp_label.setText("")
        self.mp_segna_namelabel.setText(QCoreApplication.translate("DetailWindow", u"SE\u00d1AS M.PAGO :", None))
        self.mp_segna_label.setText("")
        self.efec_ico_label.setText("")
        self.efec_namelabel.setText(QCoreApplication.translate("DetailWindow", u"EFECTIVO :", None))
        self.efec_label.setText("")
        self.efec_segna_namelabel.setText(QCoreApplication.translate("DetailWindow", u"SE\u00d1AS EFECTIVO :", None))
        self.efec_segna_label_.setText("")
        self.transfe_ico_label.setText("")
        self.transfe_namelabel.setText(QCoreApplication.translate("DetailWindow", u"T.BANCARIA:", None))
        self.transfe_label.setText("")
        self.transfe_segna_namelabel.setText(QCoreApplication.translate("DetailWindow", u"SE\u00d1AS T.BANCARIA :", None))
        self.transfe_segna_label.setText("")
        self.gastos_namelabel.setText(QCoreApplication.translate("DetailWindow", u"GASTOS DEL DIA:", None))
        self.total_namelabel.setText(QCoreApplication.translate("DetailWindow", u"TOTAL sin Se\u00f1as:", None))
        self.total_label.setText("")
        self.total_monto_pendiente_edit.setText("")
        self.total_pendiente_cobro_edit.setText("")
        self.total_pendiente_cobro_label.setText(QCoreApplication.translate("DetailWindow", u"Total Pendiente de Cobro:", None))
        self.total_monto_segna_label.setText(QCoreApplication.translate("DetailWindow", u"Total Monto de Se\u00f1as:", None))
        self.total_monto_label.setText(QCoreApplication.translate("DetailWindow", u"Total Monto:", None))
        self.total_monto_edit.setText("")
    # retranslateUi

