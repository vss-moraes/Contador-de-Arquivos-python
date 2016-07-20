import os
import pylab as plt
import numpy

def conta_extensao(arquivo, histograma):
    lista = arquivo.split(".")
    extensao = lista[-1];
    if (len(lista) == 1):
        extensao = "nenhuma"
    elif (len(lista) > 2 and lista[-2] == "tar"):
        extensao = lista[-2] + "." + lista[-1]

    if (extensao.lower() not in histograma):
        histograma[extensao.lower()] = 1
    else:
        histograma[extensao.lower()] += 1

def cria_grafico(histograma):
    num = 1
    maiores = {'outros': 0}
    if (len(histograma) > 15):
        for chave in sorted(histograma, key=histograma.get, reverse=True):
            if (num < 15):
                maiores[chave] = histograma[chave]
                num += 1
            else:
                maiores['outros'] += histograma[chave]
    else:
        maiores = histograma

    legendas = [chave for chave in sorted(maiores, key=maiores.get, reverse=True)]
    valores = [maiores[chave] for chave in legendas]
    explode = [0.1 if (item in ['java', 'py', 'js', 'nenhuma', 'outros']) else 0 for item in legendas]

    plt.pie(valores, labels=legendas,explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('scaled')

    plt.savefig("pie.svg", transparent=True)
    plt.clf()

    pos = plt.arange(len(maiores))+.5
    plt.barh(pos, valores, align="center")
    plt.yticks(pos, legendas)
    plt.xlabel("Quantidade")
    plt.savefig("barh.svg", transparent=True)
    plt.clf()


def conta_arquivos(caminho, histograma):
    varre_diretorio(caminho, histograma)

def varre_diretorio(caminho, histograma):
    for arquivo in os.listdir(caminho):
        if caminho[-1] != '/':
            caminho = caminho + '/'

        caminho_completo = caminho + arquivo

        if os.path.isdir(caminho_completo):
            varre_diretorio(caminho_completo, histograma)
        else:
            conta_extensao(arquivo, histograma)

if __name__ == "__main__":
    histograma = {}
    conta_arquivos(input('Caminho: '), histograma)
    cria_grafico(histograma)
