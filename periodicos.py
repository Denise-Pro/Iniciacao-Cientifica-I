import pandas as pd
import re 
import xlrd

def count_periodicos(lido):
    resultados = re.findall(r'\t\d\d\d\d\d\d\d\w\t', lido)

    pontuacao = 0
    #como alguns numeros inuteis são encontrados pelo programa, aqui realizo a filtragem deles.
    

    tudocerto = []

    for x in resultados:
        subs = x[1:5]
        subs = subs + '-'
        subs = subs + x[5:9]
        tudocerto.append(subs)

    artigos_validados = pd.Series(tudocerto)

    dataframe = pd.read_csv('qualis.csv')

    tamanho = len(dataframe['ISSN'])

    dataframe = dataframe.sort_values(by=['Estrato'])

    for x in artigos_validados:
        for y in range(tamanho):
            if x == dataframe['ISSN'][y]:
                result = dataframe['Estrato'][y]
                if result == 'A1' or result == 'A2':
                    pontuacao = pontuacao + 100
                    break
                elif result == 'B1' or result == 'B2' or 'B3' or 'B4' or 'B5':
                    pontuacao = pontuacao + 60
                    break
                elif result == 'C':
                    pontuacao = pontuacao + 20
                    break

    return pontuacao