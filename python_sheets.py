import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# passando a url
scope = ['https://spreadsheets.google.com/feeds']

# passando o nome do meu arquivo com as credenciais e a url como parâmetro
credentials = ServiceAccountCredentials.from_json_keyfile_name('credenciais_sheets.json', scope)

gc = gspread.authorize(credentials)

# url da planilha de respostas: 
# https://docs.google.com/spreadsheets/d/1VafiXcnpEEBIZAt1e6Fj0p7ptP8J3ym-1-prIi9ZidM/edit#gid=368129378

# abrindo a planilha especificada pelo seu ID/key (fica depois de /d e antes de /edit)
wks = gc.open_by_key('1VafiXcnpEEBIZAt1e6Fj0p7ptP8J3ym-1-prIi9ZidM')

# pega o nome da página 1 da planilha
worksheet = wks.get_worksheet(0)

#pega o conteúdo de uma única linha
values_line = worksheet.row_values(2)

#pega o conteúdo de uma única coluna
values_col = worksheet.col_values(3)

#pega todo o conteúdo de uma planilha e e traz como listas de listas 
list_of_lists = worksheet.get_all_values()

#pega todo o conteúdo de uma planilha e e traz como listas de dicionario
list_of_dicts = worksheet.get_all_records()

dados = list_of_lists[1:]
#list_of_dicts

# lista para renomear as colunas
colunas = ['grupo_no_Diretório_Grupos_CNPq', 'Email', 'alunos_grad_com_bolsa', 'alunos_grad_sem_bolsa','alunos_pos_com_bolsa', 'alunos_pos_sem_bolsa', 'n_docentes_cred_pos_EACH', 'n_docentes_cred_pos_fora_EACH', 'n_docentes_sem_cred_pos_EACH', 'QtD_docentes_ocupantes', 'QtD_docentes_ocupantes_simultaneamente', 'ex_alunos_com_pos', 'estagiarios_pos-doc_com_bolsa', 'estagiarios_pos-doc_sem_bolsa', 'Captacoes_financeiras', 'n_orientações_doutorado', 'n_orientacoes_IC_Pub', 'n_orientacoes_mestrado', 'orientacoes_TCC', 'n_outras_orientacoes', 'n_profs_colaboradores', 'n_profs_visitantes', 'servidores_técnicos_secretários', 'n_supervisões_pós-doutorado', 'Grupo', 'contiguidade', 'Mais_de_um_Docente', 'Mais_de_um_gurpo', 'Cadastro_no_CNPQ', 'xmls', 'n_patentes_grupo', 'produções_artíst_culturais', 'Quantidade_Prêmios_Honrarias', 'Qtd_Softwares', 'bolsa_prodt_A', 'bolsa_prodt_B', 'bolsa_prodt_C', 'frequência_uso', 'natureza_do_uso', 'Timestamp']   

# criando um df a partir de todos os registros da sheet salvos em um dict
dataframe = pd.DataFrame(list_of_dicts)

# renomeando as colunas do df
dataframe.columns = colunas

# modificando para o valor máximo a quantidade de linhas e colunas que devem ser mostradas em um print 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# alterando a ordem das colunas do df
dataframe= dataframe[['Grupo', 'Cadastro_no_CNPQ', 'grupo_no_Diretório_Grupos_CNPq','Mais_de_um_Docente', 'Mais_de_um_gurpo', 'xmls', 'n_patentes_grupo', 'produções_artíst_culturais', 'Quantidade_Prêmios_Honrarias', 'Qtd_Softwares', 'bolsa_prodt_A', 'bolsa_prodt_B', 'bolsa_prodt_C','frequência_uso', 'natureza_do_uso', 'contiguidade', 'alunos_grad_com_bolsa', 'alunos_grad_sem_bolsa','alunos_pos_com_bolsa', 'alunos_pos_sem_bolsa', 'n_docentes_cred_pos_EACH', 'n_docentes_cred_pos_fora_EACH', 'n_docentes_sem_cred_pos_EACH', 'QtD_docentes_ocupantes', 'QtD_docentes_ocupantes_simultaneamente', 'ex_alunos_com_pos', 'estagiarios_pos-doc_com_bolsa', 'estagiarios_pos-doc_sem_bolsa', 'Captacoes_financeiras', 'n_orientações_doutorado', 'n_orientacoes_IC_Pub', 'n_orientacoes_mestrado', 'orientacoes_TCC', 'n_outras_orientacoes', 'n_profs_colaboradores', 'n_profs_visitantes', 'servidores_técnicos_secretários', 'n_supervisões_pós-doutorado',  'Email', 'Timestamp']]

# ordenando pela coluna 'Grupo'
df = dataframe.sort_values(by = 'Grupo')
