import re
import pandas as pd
import xlrd

# abrindo o arquivo orientações1 q está na pasta dados
orientacoes = open("dados/orientacoes1.txt",'r', encoding="ISO-8859-1")
lido = orientacoes.read()

# encontrando a expressão doutourado no arquivo orientações1
numero_de_doutorados = re.findall("doutorado",lido)
numero_de_doutorados2 = re.findall("Tese de doutorado",lido)
print(len(numero_de_doutorados))

# atribuindo 100 pontos a cada pesquisador co m título de doutor
pontuacao = len(numero_de_doutorados) * 100
pontuacao = len(numero_de_doutorados2) * 100

numero_de_mestrados = re.findall("mestrado",lido)
numero_de_mestrados1 = re.findall("Disserta��o de mestrado",lido)
print(len(numero_de_mestrados))
pontuacao = pontuacao + len(numero_de_mestrados) * 80
pontuacao = pontuacao + len(numero_de_mestrados1)

numero_de_pos_doc = re.findall("pós-doutorado",lido)
print(len(numero_de_pos_doc))
pontuacao = pontuacao + len(numero_de_pos_doc) * 80

#Foi necessario implementar dois contadores para iniciação cientifica e tcc, pois eles aparecem de duas maneiras diferentes
#nos arquivos a serem lidos pelo programa
numero_de_ini_cient = re.findall("INICIACAO_CIENTIFICA",lido)
print(len(numero_de_ini_cient))
pontuacao = pontuacao + len(numero_de_ini_cient) * 40

numero_de_ini_cient_2 = re.findall("Iniciação Científica",lido)
numero_de_ini_cient_3 = re.findall("Inicia��o Cient�fica",lido)
print(len(numero_de_ini_cient_2))
pontuacao = pontuacao + len(numero_de_ini_cient_2) * 40
pontuacao = pontuacao + len(numero_de_ini_cient_3) * 40

numero_de_tcc_1 = re.findall("TRABALHO_DE_CONCLUSAO_DE_CURSO_GRADUACAO",lido)
print(len(numero_de_tcc_1))
pontuacao = pontuacao + len(numero_de_tcc_1) * 10

numero_de_tcc_2 = re.findall("Trabalho de conclusão de curso de graduação",lido)
numero_de_tcc_3 = re.findall("Trabalho de conclus�o de curso de gradua��o",lido)
print(len(numero_de_tcc_2))
pontuacao = pontuacao + len(numero_de_tcc_2) * 10
pontuacao = pontuacao + len(numero_de_tcc_3) * 10

print("Debug orientações: {}".format(pontuacao))

# a partir daqui estamos lidando com os periódicos
periodicos = open("dados/periodicos1.txt", 'r', encoding="ISO-8859-1")
lido = periodicos.read()

#procurando a sequencia de oito numeros
resultados = re.findall("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", lido)
print(resultados)

qualisframe = open("qualis.xls", 'r', encoding="ISO-8859-1")
openqualis = qualisframe.read()

#como alguns numeros inuteis são encontrados pelo programa, aqui realizo a filtragem deles.
only_artigos = []
for x in resultados:
    if x != '16891473' and x != '40536405':
        only_artigos.append(x)

print(len(only_artigos))

tudocerto = []

for x in only_artigos:
    subs = x[0:4]
    subs = subs + '-'
    subs = subs + x[4:8]
    tudocerto.append(subs)


print(pontuacao)
print(len(numero_de_mestrados))
print(len(numero_de_doutorados))
print(len(numero_de_pos_doc))
print(len(numero_de_ini_cient))
print(len(numero_de_ini_cient_2))
print(len(numero_de_tcc_1))
print(len(numero_de_tcc_2))

print(tudocerto)

dataframe = pd.read_csv('qualis.csv')

print(type(tudocerto[0]))
print(type(dataframe['ISSN'][0]))

tamanho = len(dataframe['ISSN'])

print(pontuacao)

dataframe = dataframe.sort_values(by=['Estrato'])
print(dataframe.head())
print(dataframe.count())

# atribuindo pontuações para os srtigos com extrato A, B OU C
for x in tudocerto:
    print(x)
    for y in range(tamanho):
        if x == dataframe['ISSN'][y]:
            print(dataframe['ISSN'][y])
            result = dataframe['Estrato'][y]
            print(result)
            if result == 'A1' or result == 'A2':
                pontuacao = pontuacao + 100
                break
            elif result == 'B1' or result == 'B2' or 'B3' or 'B4' or 'B5':
                pontuacao = pontuacao + 60
                break
            elif result == 'C':
                pontuacao = pontuacao + 20
                break
                
#abrindo o arquivo capitulos
with open("dados/capit",encoding="ISO-8859-1") as c:
    cap = c.read()

#cada linha do arquivo vira a posição de uma lista
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
pontuacao_cap

#abro o arquivo livros'
with open("dados/livros1.txt",encoding="ISO-8859-1") as li:
    livros = li.read()

#cada linha do arquivo vira uma posição de book
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


pontuacao_total_grupo = pontuacao + pontuacao_autores + pontuacao_editores + pontuacao_cap

print(pontuacao_total_grupo)