import re 
import pandas as pd 
import xlrd

def count_orientacoes(lido):

    numero_de_doutorados = re.findall("doutorado",lido)
    numero_de_doutorados2 = re.findall("Tese de doutorado",lido)

    pontuacao = len(numero_de_doutorados) * 100
    pontuacao = len(numero_de_doutorados2) * 100

    numero_de_mestrados = re.findall("mestrado",lido)
    numero_de_mestrados1 = re.findall("Disserta��o de mestrado",lido)
    pontuacao = pontuacao + len(numero_de_mestrados) * 80
    pontuacao = pontuacao + len(numero_de_mestrados1)

    numero_de_pos_doc = re.findall("pós-doutorado",lido)
    pontuacao = pontuacao + len(numero_de_pos_doc) * 80

    #Foi necessario implementar dois contadores para iniciação cientifica e tcc, pois eles aparecem de duas maneiras diferentes
    #nos arquivos a serem lidos pelo programa
    numero_de_ini_cient = re.findall("INICIACAO_CIENTIFICA",lido)
    pontuacao = pontuacao + len(numero_de_ini_cient) * 40

    numero_de_ini_cient_2 = re.findall("Iniciação Científica",lido)
    numero_de_ini_cient_3 = re.findall("Inicia��o Cient�fica",lido)
    pontuacao = pontuacao + len(numero_de_ini_cient_2) * 40
    pontuacao = pontuacao + len(numero_de_ini_cient_3) * 40

    numero_de_tcc_1 = re.findall("TRABALHO_DE_CONCLUSAO_DE_CURSO_GRADUACAO",lido)
    pontuacao = pontuacao + len(numero_de_tcc_1) * 10

    numero_de_tcc_2 = re.findall("Trabalho de conclusão de curso de graduação",lido)
    numero_de_tcc_3 = re.findall("Trabalho de conclus�o de curso de gradua��o",lido)
    pontuacao = pontuacao + len(numero_de_tcc_2) * 10
    pontuacao = pontuacao + len(numero_de_tcc_3) * 10

    return pontuacao
