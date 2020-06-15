import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np

# passando a url
scope = ['https://spreadsheets.google.com/feeds']

# passando o nome do meu arquivo com as credenciais e a url como parâmetro
credentials = ServiceAccountCredentials.from_json_keyfile_name('credenciais_sheets.json', scope)

gc = gspread.authorize(credentials)

# url da planilha de respostas: 
# https://docs.google.com/spreadsheets/d/1lpRAk_SSG8iJOhMNKV1yVRTK61zkforDL_6Lm2iUZBg/edit?pli=1#gid=1096379494

# abrindo a planilha especificada pelo seu ID/key (fica depois de /d e antes de /edit)
wks = gc.open_by_key('1lpRAk_SSG8iJOhMNKV1yVRTK61zkforDL_6Lm2iUZBg')

# pega o nome da página 1 da planilha
worksheet = wks.get_worksheet(0)

#pega todo o conteúdo de uma planilha e e traz como listas de dicionario
list_of_dicts = worksheet.get_all_records()

# criando um df a partir de todos os registros da sheet salvos em um dict
dataframe = pd.DataFrame(list_of_dicts)

# # modificando para o valor máximo a quantidade de linhas e colunas que devem ser mostradas em um print 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# # lista para renomear as colunas
colunas = ['grupo_no_Diretório_Grupos_CNPq', 'Email', 'alunos_grad_com_bolsa', 'alunos_grad_sem_bolsa','alunos_pos_com_bolsa', 'alunos_pos_sem_bolsa','n_docentes_cred_pos_EACH', 'n_docentes_cred_pos_fora_EACH', 'n_docentes_sem_cred_pos_EACH', 'QtD_docentes_ocupantes', 'QtD_docentes_ocupantes_simultaneamente', 'ex_alunos_com_pos','estagiarios_pos-doc_com_bolsa', 'estagiarios_pos-doc_sem_bolsa','Captacoes_financeiras','n_orientações_doutorado', 'n_orientacoes_IC_Pub', 'n_orientacoes_mestrado', 'orientacoes_TCC', 'n_outras_orientacoes', 'n_profs_colaboradores', 'n_profs_visitantes', 'servidores_técnicos_secretários', 'n_supervisões_pós-doutorado', 'Grupo', 'contiguidade', 'Mais_de_um_Docente', 'Mais_de_um_grupo', 'Cadastro_no_CNPQ', 'xmls', 'n_patentes_grupo','produções_artist_culturais_A', 'produções_artist_culturais_B' , 'produções_artist_culturais_C' ,'Quantidade_Prêmios_Honrarias', 'Qtd_Softwares', 'bolsa_prodt_1A', 'bolsa_prodt_1B', 'bolsa_prodt_1C', 'bolsa_prodt_1D', 'bolsa_prodt_2', 'frequência_uso', 'natureza_do_uso','Timestamp']

# renomeando as colunas do df
dataframe.columns = colunas

# alterando a ordem das colunas do df
dataframe= dataframe[['Grupo','Mais_de_um_Docente','Mais_de_um_grupo', 'natureza_do_uso', 'frequência_uso', 'Cadastro_no_CNPQ', 'grupo_no_Diretório_Grupos_CNPq','QtD_docentes_ocupantes', 'QtD_docentes_ocupantes_simultaneamente','contiguidade', 'n_docentes_cred_pos_EACH', 'n_docentes_cred_pos_fora_EACH', 'n_docentes_sem_cred_pos_EACH', 'n_orientações_doutorado','n_orientacoes_mestrado', 'n_supervisões_pós-doutorado', 'n_orientacoes_IC_Pub', 'orientacoes_TCC','n_outras_orientacoes', 'Captacoes_financeiras', 'alunos_pos_com_bolsa', 'alunos_pos_sem_bolsa','estagiarios_pos-doc_com_bolsa', 'estagiarios_pos-doc_sem_bolsa', 'n_profs_colaboradores', 'n_profs_visitantes', 'alunos_grad_com_bolsa', 'alunos_grad_sem_bolsa', 'ex_alunos_com_pos',   'servidores_técnicos_secretários', 'xmls', 'bolsa_prodt_1A', 'bolsa_prodt_1B', 'bolsa_prodt_1C', 'bolsa_prodt_1D','bolsa_prodt_2','Qtd_Softwares', 'n_patentes_grupo', 'Quantidade_Prêmios_Honrarias', 'produções_artist_culturais_A', 'produções_artist_culturais_B' , 'produções_artist_culturais_C', 'Email', 'Timestamp']
]

#pegando a quantidade de grupos = linhass no df
qtd_linhas = dataframe['Grupo'].count()

soma_pesos = 10 # soma de pesos por sessão
point = {}
for i in range(qtd_linhas):
    pontos_medios = 0
    pontos = []
    if dataframe.loc[i]['Mais_de_um_Docente'] == 'Sim':
            pontos.append(100*2)
    if dataframe.loc[i]['Mais_de_um_grupo'] == 'Sim':
            pontos.append(100*2)
    if dataframe.loc[i]['natureza_do_uso'] == 'Experimentos, análises, reuniões,armazenamento de material e equipamentos':
            pontos.append(100*2)
    if dataframe.loc[i]['natureza_do_uso'] == 'Reuniões,armazenamento de material/equipamentos':
            pontos.append(80*2)
    if dataframe.loc[i]['natureza_do_uso'] == 'Reuniões':
        pontos.append(40*2)
    if dataframe.loc[i]['frequência_uso'] == 'Espaço utilizado esporadicamente':
        pontos.append(20*2)
    if dataframe.loc[i]['frequência_uso'] == 'Espaço utilizado regularmente':
        pontos.append(100*2)
    if dataframe.loc[i]['Cadastro_no_CNPQ'] == 'Sim':
        pontos.append(100*2)
    if dataframe.loc[i]['Cadastro_no_CNPQ'] == 'Não':
        pontos.append(20*2)
    pontos.append(dataframe.loc[i]['QtD_docentes_ocupantes']*100*2)
    pontos.append(dataframe.loc[i]['QtD_docentes_ocupantes_simultaneamente']*20*2)
    if dataframe.loc[i]['contiguidade'] == 'Sim':
        pontos.append(100)
    if dataframe.loc[i]['contiguidade'] == 'Não, o espaço é fracionado em diferentes locais na EACH':
        pontos.append(50)
    pontos.append(dataframe.loc[i]['n_docentes_cred_pos_EACH']*100)
    pontos.append(dataframe.loc[i]['n_docentes_cred_pos_fora_EACH']*50)
    pontos.append(dataframe.loc[i]['n_outras_orientacoes']*10)
    pontos.append(dataframe.loc[i]['Captacoes_financeiras']*100)
    pontos.append(dataframe.loc[i]['alunos_pos_com_bolsa']*60)
    pontos.append(dataframe.loc[i]['alunos_pos_sem_bolsa']*40)
    pontos.append(dataframe.loc[i]['estagiarios_pos-doc_com_bolsa']*40)
    pontos.append(dataframe.loc[i]['estagiarios_pos-doc_sem_bolsa']*20)
    pontos.append(dataframe.loc[i]['n_profs_colaboradores']*30)
    pontos.append(dataframe.loc[i]['n_profs_visitantes']*30)
    pontos.append(dataframe.loc[i]['alunos_grad_com_bolsa']*40)
    pontos.append(dataframe.loc[i]['alunos_grad_sem_bolsa']*20)
    pontos.append(dataframe.loc[i]['ex_alunos_com_pos']*10)
    pontos.append(dataframe.loc[i]['servidores_técnicos_secretários']*10)
    pontos.append(dataframe.loc[i]['bolsa_prodt_1A']*100)
    pontos.append(dataframe.loc[i]['bolsa_prodt_1B']*80)
    pontos.append(dataframe.loc[i]['bolsa_prodt_1C']*60)
    pontos.append(dataframe.loc[i]['bolsa_prodt_1D']*40)
    pontos.append(dataframe.loc[i]['bolsa_prodt_2']*20)
    pontos.append(dataframe.loc[i]['Qtd_Softwares']*60)
    pontos.append(dataframe.loc[i]['n_patentes_grupo']*120)
    pontos.append(dataframe.loc[i]['Quantidade_Prêmios_Honrarias']*50)
    pontos.append(dataframe.loc[i]['produções_artist_culturais_A']*100)
    pontos.append(dataframe.loc[i]['produções_artist_culturais_B']*60)
    pontos.append(dataframe.loc[i]['produções_artist_culturais_C']*20)

    pontos_medios = round(np.sum(pontos)/soma_pesos,2)
    point.update({dataframe.loc[i]["Grupo"]: pontos_medios})

df = pd.DataFrame(data=point, index=['Pontos'])
df