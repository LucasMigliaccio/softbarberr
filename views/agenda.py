# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agenda.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QSizePolicy,
    QSpacerItem, QTableView, QToolButton, QVBoxLayout,
    QWidget)

class Agenda(object):
    def setupUi(self, DetailWindow):
        if not DetailWindow.objectName():
            DetailWindow.setObjectName(u"DetailWindow")
        DetailWindow.resize(1054, 728)
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
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pendientes_tableView = QTableView(self.frame_8)
        self.pendientes_tableView.setObjectName(u"pendientes_tableView")
        self.pendientes_tableView.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.pendientes_tableView)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_table = QFrame(self.frame_5)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setMinimumSize(QSize(0, 75))
        self.frame_table.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 15px;")
        self.frame_table.setFrameShape(QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_table)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(458, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_second_frame = QLabel(self.frame_table)
        self.label_second_frame.setObjectName(u"label_second_frame")
        self.label_second_frame.setStyleSheet(u"color: rgb(230, 230, 230);")

        self.horizontalLayout_3.addWidget(self.label_second_frame)

        self.horizontalSpacer_4 = QSpacerItem(458, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


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
        self.label_tittle.setText(QCoreApplication.translate("DetailWindow", u"Agenda", None))
        self.minimize_button.setText(QCoreApplication.translate("DetailWindow", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("DetailWindow", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("DetailWindow", u"...", None))
        self.close_button.setText(QCoreApplication.translate("DetailWindow", u"...", None))
        self.label_second_frame.setText("")
    # retranslateUi

