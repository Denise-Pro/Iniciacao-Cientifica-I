import re
import pandas as pd
import os 
import pathlib
import xlrd
import orientações as ori
import periodicos as per
import capitulos as cap
import livros as lv
import forms
import matplotlib.pyplot as plt

pontos_forms = pontos_forms = forms.forms_points()

grupos = os.listdir("dados/") 
grupos = pd.Series(grupos)
grupos = grupos[grupos != '.DS_Store']
print("Grupos que terão seus pontos computados:")
print(grupos)

resultado_final = pd.DataFrame(columns=["Grupo","Pontuação"])

for grupo in grupos:

    arquivo_de_orientacoes = "dados/"+grupo+"/orientacoes1.txt"
    orientacoes = open(arquivo_de_orientacoes,'r', encoding="ISO-8859-1")
    orientacoes = orientacoes.read()
    pontuacao = ori.count_orientacoes(orientacoes)

    arquivo_de_periodicos = "dados/"+grupo+"/periodicos1.txt"
    periodicos = open(arquivo_de_periodicos, 'r', encoding="ISO-8859-1")
    periodicos = periodicos.read()
    pontuacao = per.count_periodicos(periodicos)

    arquivo_de_capitulos = "dados/"+grupo+"/capit"
    with open(arquivo_de_capitulos,encoding="ISO-8859-1") as c:
        capitulos = c.read()
    pontuacao = pontuacao + cap.count_capitulos(capitulos)

    arquivo_de_capitulos = "dados/"+grupo+"/livros1.txt"
    with open(arquivo_de_capitulos,encoding="ISO-8859-1") as li:
        livros = li.read()
    pontuacao = pontuacao + lv.count_livros(livros)

    linha = pd.DataFrame({"Grupo":grupo,"Pontuação":pontuacao+ pontos_forms[grupo].values})
    resultado_final = resultado_final.append(linha)
    print("Grupo: "+grupo+" -> Pontuação Final: {}".format(pontuacao+pontos_forms[grupo]['Pontos']))

resultado_final = resultado_final.reset_index()
resultado_final.to_csv("pontuacao_final.csv")

pontuacao = pd.read_csv('pontuacao_final.csv', sep = ',')
pontuacao = pontuacao.drop(columns=['Unnamed: 0','index'])


pontuacao.boxplot()
plt.savefig("Box_Plot_Grupos_Pesquisa_EACH.jpeg", dpi=300) #salva imagem como jpeg e com tamnho 300
plt.show()