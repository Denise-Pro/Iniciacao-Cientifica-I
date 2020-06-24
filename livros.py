import pandas as pd 
import xlrd
import re 

def count_livros(livros):

    book = livros.split('\n')

    conteudo_book=[]
    for x in book[1:]:
        conteudo_book.append(x.split('\t'))

    LIVROS_PUBLICADOS = []
    LIVROS_ORGANIZADOS =[]

    for i in range(0, len(conteudo_book)-1):
        if(conteudo_book[i][5] == 'LIVRO_ORGANIZADO_OU_EDICAO'):
            LIVROS_ORGANIZADOS.append(conteudo_book[i])
        elif(conteudo_book[i][5] == 'LIVRO_PUBLICADO'):
            LIVROS_PUBLICADOS.append(conteudo_book[i])
        i =i+1

    j=0
    editores = []
    #pegando os editores q organizaram/editaram
    while(j<len(LIVROS_ORGANIZADOS)):
        for nome in LIVROS_ORGANIZADOS[j][13].split(';'):
            editores.append(nome)
        j=j+1
    editores


    c=0
    pontuacao_editores1={}
    while(c < len(editores)):
        pontuacao_editores1.update({editores[c]:(editores.count(editores[c])*80)})
        c=c+1

    pontuacao_editores = 0    
    for e in pontuacao_editores1:
        pontuacao_editores = pontuacao_editores + pontuacao_editores1[e]
    pontuacao_editores

    #livros autoria propria
    #pegando os autores
    k=0
    autores= []
    while(k<len(LIVROS_PUBLICADOS)):
        for nome in LIVROS_PUBLICADOS[k][13].split(';'):
            autores.append(nome.strip())
        k=k+1

    p=0
    pontuacao_autores1={}
    while(p < len(autores)):
        pontuacao_autores1.update({autores[p]:(autores.count(autores[p])*120)})
        p=p+1

    pontuacao_autores=0
    for a in pontuacao_autores1:
        pontuacao_autores = pontuacao_autores + pontuacao_autores1[a]
    pontuacao_autores

    return pontuacao_autores + pontuacao_editores
