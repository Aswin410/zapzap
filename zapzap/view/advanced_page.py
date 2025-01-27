from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/ui/advanced_page.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Advanced(object):
    def setupUi(self, Advanced):
        Advanced.setObjectName("Advanced")
        Advanced.resize(321, 216)
        Advanced.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Advanced)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Advanced)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=Advanced)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.hideBarUsers = QtWidgets.QCheckBox(parent=Advanced)
        self.hideBarUsers.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.hideBarUsers.setObjectName("hideBarUsers")
        self.gridLayout.addWidget(self.hideBarUsers, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=Advanced)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=Advanced)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.donationMessage = QtWidgets.QCheckBox(parent=Advanced)
        self.donationMessage.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.donationMessage.setChecked(True)
        self.donationMessage.setObjectName("donationMessage")
        self.gridLayout_2.addWidget(self.donationMessage, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Advanced)
        QtCore.QMetaObject.connectSlotsByName(Advanced)

    def retranslateUi(self, Advanced):
        
        self.label.setText(_("Advanced"))
        self.label_2.setText(_("Hide setting bar with only one user"))
        self.hideBarUsers.setText(_("Off"))
        self.label_3.setText(_("To access the settings use the menu in the tray or the shortcut Ctrl+P"))
        self.label_4.setText(_("Donation message"))
        self.donationMessage.setText(_("On"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Advanced = QtWidgets.QWidget()
    ui = Ui_Advanced()
    ui.setupUi(Advanced)
    Advanced.show()
    sys.exit(app.exec())
