import pandas as pd
import xlrd
import re

def count_capitulos(cap):
    capitulos = cap.split('\n')

    #pegando o conteúdo sem o cabeçalho
    conteudo_cap=[]
    for x in capitulos[1:]:
        conteudo_cap.append(x.split('\t'))

    j=0
    nomes_cap=[]
    while(j<len(conteudo_cap)-1):
        for nome in conteudo_cap[j][13].split(';'):
            nomes_cap.append(nome.strip())
        j=j+1

    #atribuo a pontuação total para cada autor e guardo em um dicionário
    c=0
    pontuacao_cap1={}
    while(c < len(nomes_cap)):
        pontuacao_cap1.update({nomes_cap[c]:(nomes_cap.count(nomes_cap[c])*40)})
        c=c+1

    pontuacao_cap=0
    for y in pontuacao_cap1:
        pontuacao_cap = pontuacao_cap + pontuacao_cap1[y]

    return pontuacao_cap