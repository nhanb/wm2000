# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionManage_export_targets = QAction(MainWindow)
        self.actionManage_export_targets.setObjectName(u"actionManage_export_targets")
        self.actionChoose = QAction(MainWindow)
        self.actionChoose.setObjectName(u"actionChoose")
        self.actionPublish_to_github_com_nhanb = QAction(MainWindow)
        self.actionPublish_to_github_com_nhanb.setObjectName(u"actionPublish_to_github_com_nhanb")
        self.actionPublish_to_gitlab_com_nhanb = QAction(MainWindow)
        self.actionPublish_to_gitlab_com_nhanb.setObjectName(u"actionPublish_to_gitlab_com_nhanb")
        self.actionManage = QAction(MainWindow)
        self.actionManage.setObjectName(u"actionManage")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuExport = QMenu(self.menubar)
        self.menuExport.setObjectName(u"menuExport")
        self.menuPublish = QMenu(self.menubar)
        self.menuPublish.setObjectName(u"menuPublish")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuPublish.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuExport.addAction(self.actionManage_export_targets)
        self.menuExport.addAction(self.actionChoose)
        self.menuPublish.addAction(self.actionPublish_to_github_com_nhanb)
        self.menuPublish.addAction(self.actionPublish_to_gitlab_com_nhanb)
        self.menuPublish.addSeparator()
        self.menuPublish.addAction(self.actionManage)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionManage_export_targets.setText(QCoreApplication.translate("MainWindow", u"Export to ~/foo/bar", None))
        self.actionChoose.setText(QCoreApplication.translate("MainWindow", u"Manage...", None))
        self.actionPublish_to_github_com_nhanb.setText(QCoreApplication.translate("MainWindow", u"Publish to github.com/nhanb", None))
        self.actionPublish_to_gitlab_com_nhanb.setText(QCoreApplication.translate("MainWindow", u"Publish to gitlab.com/nhanb", None))
        self.actionManage.setText(QCoreApplication.translate("MainWindow", u"Manage...", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuExport.setTitle(QCoreApplication.translate("MainWindow", u"Export", None))
        self.menuPublish.setTitle(QCoreApplication.translate("MainWindow", u"Publish", None))
    # retranslateUi

