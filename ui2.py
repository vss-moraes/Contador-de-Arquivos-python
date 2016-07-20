# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contadorUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Contador(object):
    def setupUi(self, Contador):
        Contador.setObjectName("Contador")
        Contador.resize(998, 653)
        self.centralwidget = QtWidgets.QWidget(Contador)
        self.centralwidget.setObjectName("centralwidget")
        self.botaoAbrir = QtWidgets.QPushButton(self.centralwidget)
        self.botaoAbrir.setGeometry(QtCore.QRect(760, 30, 87, 29))
        self.botaoAbrir.setObjectName("botaoAbrir")

        self.botaoIniciar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoIniciar.setGeometry(QtCore.QRect(460, 70, 87, 29))
        self.botaoIniciar.setObjectName("botaoIniciar")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 56, 17))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 621, 29))
        self.lineEdit.setObjectName("lineEdit")

        self.tabela = QtWidgets.QTableWidget(self.centralwidget)
        self.tabela.setEnabled(False)
        self.tabela.setGeometry(QtCore.QRect(20, 130, 271, 481))
        self.tabela.setObjectName("tabela")
        self.tabela.setColumnCount(0)
        self.tabela.setRowCount(0)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(310, 130, 651, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(5, -3, 641, 441))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 651, 451))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        Contador.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(Contador)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 23))
        self.menubar.setObjectName("menubar")
        Contador.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Contador)
        self.statusbar.setObjectName("statusbar")
        Contador.setStatusBar(self.statusbar)

        self.retranslateUi(Contador)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Contador)

    def retranslateUi(self, Contador):
        _translate = QtCore.QCoreApplication.translate
        Contador.setWindowTitle(_translate("Contador", "Contador de Arquivos"))
        self.botaoAbrir.setText(_translate("Contador", "Abrir..."))
        self.botaoIniciar.setText(_translate("Contador", "Iniciar"))
        self.label.setText(_translate("Contador", "Diretório"))
        self.label_2.setText(_translate("Contador", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Contador", "Tab 1"))
        self.label_3.setText(_translate("Contador", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Contador", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Contador = QtWidgets.QMainWindow()
    ui = Ui_Contador()
    ui.setupUi(Contador)
    Contador.show()
    sys.exit(app.exec_())
