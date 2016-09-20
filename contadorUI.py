# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contadorUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import contador
import os


class Ui_Contador(object):

    def setupUi(self, Contador):
        Contador.setObjectName("Contador")
        Contador.resize(800, 120)
        self.centralwidget = QtWidgets.QWidget(Contador)
        self.centralwidget.setObjectName("centralwidget")

        self.botaoAbrir = QtWidgets.QPushButton(self.centralwidget)
        self.botaoAbrir.setGeometry(QtCore.QRect(660, 30, 87, 29))
        self.botaoAbrir.setObjectName("botaoAbrir")
        self.botaoAbrir.clicked.connect(self.escolhe_arquivo)

        self.botaoIniciar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoIniciar.setGeometry(QtCore.QRect(360, 70, 87, 29))
        self.botaoIniciar.setObjectName("botaoIniciar")
        self.botaoIniciar.clicked.connect(self.iniciar)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 56, 17))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 621, 29))
        self.lineEdit.setObjectName("lineEdit")

        self.tabela = QtWidgets.QTableWidget(self.centralwidget)
        self.tabela.setGeometry(QtCore.QRect(20, 115, 202, 481))
        self.tabela.setObjectName("tabela")
        self.tabela.setColumnCount(2)
        self.tabela.setRowCount(0)
        self.tabela.setHorizontalHeaderLabels(["Extensão", "Quantidade"])
        self.tabela.setVisible(False)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(240, 115, 550, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setVisible(False)

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.grafico_pizza = QtWidgets.QLabel(self.tab)
        self.grafico_pizza.setGeometry(QtCore.QRect(0, 0, 550, 481))
        self.grafico_pizza.setObjectName("grafico_pizza")
        self.tabWidget.addTab(self.tab, "Pizza")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.grafico_barrash = QtWidgets.QLabel(self.tab_2)
        self.grafico_barrash.setGeometry(QtCore.QRect(0, 0, 550, 481))
        self.grafico_barrash.setObjectName("grafico_barrash")
        self.tabWidget.addTab(self.tab_2, "Barras")

        Contador.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Contador)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 23))
        self.menubar.setObjectName("menubar")
        Contador.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Contador)
        self.statusbar.setObjectName("statusbar")
        Contador.setStatusBar(self.statusbar)

        self.retranslateUi(Contador)
        QtCore.QMetaObject.connectSlotsByName(Contador)

    def retranslateUi(self, Contador):
        _translate = QtCore.QCoreApplication.translate
        Contador.setWindowTitle(_translate("Contador", "Contador de Arquivos"))
        self.botaoAbrir.setText(_translate("Contador", "Abrir..."))
        self.botaoIniciar.setText(_translate("Contador", "Iniciar"))
        self.label.setText(_translate("Contador", "Diretório"))

    def escolhe_arquivo(self):
        fname = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select a folder:', '', QtWidgets.QFileDialog.ShowDirsOnly)
        self.lineEdit.setText(fname)

    def mostra_tabela(self, histograma):
        tabela = self.tabela
        tabela.setRowCount(len(histograma))

        for linha, chave in enumerate(sorted(histograma, key=histograma.get, reverse=True)):
            novoItem = QtWidgets.QTableWidgetItem(chave)
            tabela.setItem(linha, 0, novoItem)
            novoItem = QtWidgets.QTableWidgetItem(str(histograma[chave]))
            tabela.setItem(linha, 1, novoItem)

        tabela.verticalHeader().hide()
        tabela.setVisible(True)

    def reseta_tela(self):
        self.tabela.setVisible(False)
        self.tabWidget.setVisible(False)
        Contador.resize(800, 120)

    def iniciar(self):
        self.reseta_tela()
        histograma = {}
        caminho = self.lineEdit.text()
        self.grafico_pizza.setPixmap(QtGui.QPixmap(""))
        print(caminho)
        if (caminho != '' and os.path.isdir(caminho)):
            contador.varre_diretorio(caminho, histograma)
            contador.cria_grafico(histograma)
            pizza = QtGui.QPixmap("pie.svg").scaledToWidth(550, mode=QtCore.Qt.SmoothTransformation)
            barras_h = QtGui.QPixmap("barh.svg").scaledToWidth(550, mode=QtCore.Qt.SmoothTransformation)
            self.grafico_pizza.setPixmap(pizza)
            self.grafico_barrash.setPixmap(barras_h)
            Contador.resize(800, 630)
            self.mostra_tabela(histograma)
            self.tabWidget.setVisible(True)
        else:
            self.reseta_tela()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Contador = QtWidgets.QMainWindow()
    ui = Ui_Contador()
    ui.setupUi(Contador)
    Contador.show()
    sys.exit(app.exec_())
