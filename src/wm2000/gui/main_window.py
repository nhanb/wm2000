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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon = QIcon(QIcon.fromTheme(u"document-open"))
        self.actionOpen.setIcon(icon)
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionSave_As.setEnabled(False)
        icon1 = QIcon(QIcon.fromTheme(u"document-save-as"))
        self.actionSave_As.setIcon(icon1)
        self.actionSave_As.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon2 = QIcon(QIcon.fromTheme(u"application-exit"))
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setMenuRole(QAction.MenuRole.QuitRole)
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
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon3 = QIcon(QIcon.fromTheme(u"document-new"))
        self.actionNew.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageEmpty = QWidget()
        self.pageEmpty.setObjectName(u"pageEmpty")
        self.verticalLayout_2 = QVBoxLayout(self.pageEmpty)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelNoFileChosen = QLabel(self.pageEmpty)
        self.labelNoFileChosen.setObjectName(u"labelNoFileChosen")
        self.labelNoFileChosen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelNoFileChosen.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_2.addWidget(self.labelNoFileChosen)

        self.stackedWidget.addWidget(self.pageEmpty)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuExport = QMenu(self.menubar)
        self.menuExport.setObjectName(u"menuExport")
        self.menuExport.setEnabled(False)
        self.menuPublish = QMenu(self.menubar)
        self.menuPublish.setObjectName(u"menuPublish")
        self.menuPublish.setEnabled(False)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuPublish.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
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
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"&Open...", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save &As...", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
        self.actionManage_export_targets.setText(QCoreApplication.translate("MainWindow", u"&Export to ~/foo/bar", None))
        self.actionChoose.setText(QCoreApplication.translate("MainWindow", u"&Manage...", None))
        self.actionPublish_to_github_com_nhanb.setText(QCoreApplication.translate("MainWindow", u"&Publish to github.com/nhanb", None))
        self.actionPublish_to_gitlab_com_nhanb.setText(QCoreApplication.translate("MainWindow", u"Publish to &gitlab.com/nhanb", None))
        self.actionManage.setText(QCoreApplication.translate("MainWindow", u"&Manage...", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"&New...", None))
        self.labelNoFileChosen.setText(QCoreApplication.translate("MainWindow", u"No file chosen. Click File/New or File/Open and pick a wm2k file to start.", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuExport.setTitle(QCoreApplication.translate("MainWindow", u"E&xport", None))
        self.menuPublish.setTitle(QCoreApplication.translate("MainWindow", u"P&ublish", None))
    # retranslateUi

