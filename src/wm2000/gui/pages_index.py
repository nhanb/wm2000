# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pages_index.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_pagesIndex(object):
    def setupUi(self, pagesIndex):
        if not pagesIndex.objectName():
            pagesIndex.setObjectName(u"pagesIndex")
        pagesIndex.resize(512, 354)
        self.verticalLayout = QVBoxLayout(pagesIndex)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pagesTable = QTableView(pagesIndex)
        self.pagesTable.setObjectName(u"pagesTable")

        self.verticalLayout.addWidget(self.pagesTable)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addPageBtn = QPushButton(pagesIndex)
        self.addPageBtn.setObjectName(u"addPageBtn")

        self.horizontalLayout.addWidget(self.addPageBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(pagesIndex)

        QMetaObject.connectSlotsByName(pagesIndex)
    # setupUi

    def retranslateUi(self, pagesIndex):
        pagesIndex.setWindowTitle(QCoreApplication.translate("pagesIndex", u"Form", None))
        self.addPageBtn.setText(QCoreApplication.translate("pagesIndex", u"Add page...", None))
    # retranslateUi

