# -*- coding: UTF-8 -*-

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np

def forms_points():
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

    # # lista para renomear as colunas
    colunas = {
                'Em caso positivo, inclua nome, sigla e link do grupo no Diretório de Grupos do CNPq.':'grupo_no_Diretório_Grupos_CNPq',
                'Email Address':'Email',
                'Indique o número de alunos de graduação com bolsa utilizando o espaço de pesquisa: (40 pontos cada)':'alunos_grad_com_bolsa', 
                'Indique o número de alunos de graduação sem bolsa utilizando o espaço de pesquisa: (20 pontos cada)':'alunos_grad_sem_bolsa',
                'Indique o número de alunos de pós-graduação com bolsa utilizando o espaço de pesquisa: (60 pontos cada)':'alunos_pos_com_bolsa',
                'Indique o número de alunos de pós-graduação sem bolsa utilizando o espaço de pesquisa: (40 pontos cada)':'alunos_pos_sem_bolsa',
                'Indique o número de docentes da EACH no grupo que estão credenciados em programas de pós-graduação da EACH: (100 pontos cada)':'n_docentes_cred_pos_EACH',
                'Indique o número de docentes da EACH no grupo que estão credenciados em programas de pós-graduação fora da EACH: (50 pontos cada)':'n_docentes_cred_pos_fora_EACH',
                'Indique o número de docentes da EACH no grupo que não tem credenciamento em programas de pós-graduação: (10 pontos cada)':'n_docentes_sem_cred_pos_EACH', 
                'Indique o número de docentes da EACH que ocupam exclusivamente o espaço do presente grupo: (100 pontos cada)':'QtD_docentes_ocupantes',
                'Indique o número de docentes da EACH que ocupam simultaneamente o espaço do presente grupo e outros espaços de pesquisa: (20 pontos cada)':'QtD_docentes_ocupantes_simultaneamente',
                'Indique o número de egressos (ex-alunos) postulantes a vaga na pós-graduação utilizando o espaço de pesquisa: (10 pontos cada)':'ex_alunos_com_pos',
                'Indique o número de estagiários de pós-doutorado com bolsa utilizando o espaço de pesquisa: (40 pontos cada)':'estagiarios_pos-doc_com_bolsa',
                'Indique o número de estagiários de pós-doutorado sem bolsa utilizando o espaço de pesquisa: (20 pontos cada)':'estagiarios_pos-doc_sem_bolsa',
                'Indique o número de fomentos a pesquisa (em andamento e concluídas) obtidos pelos docentes da EACH no grupo: (100 pontos cada)':'Captacoes_financeiras',
                'Indique o número de orientações de doutorado (finalizadas ou vigentes) dos docentes da EACH no grupo: (100 pontos cada)':'n_orientações_doutorado',
                'Indique o número de orientações de iniciação científica, PUB ou IC voluntária (finalizadas ou vigentes) dos docentes da EACH no grupo: (40 pontos cada)':'n_orientacoes_IC_Pub', 
                'Indique o número de orientações de mestrado (finalizadas ou vigentes) dos docentes da EACH no grupo: (80 pontos cada)':'n_orientacoes_mestrado', 
                'Indique o número de orientações de trabalhos de conclusão de curso (finalizadas ou vigentes) dos docentes da EACH no grupo: (10 pontos cada)':'orientacoes_TCC',
                'Indique o número de outras modalidades de orientações de graduação (finalizadas ou vigentes) dos docentes da EACH no grupo: (10 pontos cada)':'n_outras_orientacoes', 
                'Indique o número de professores colaboradores utilizando o espaço de pesquisa: (30 pontos cada)':'n_profs_colaboradores', 
                'Indique o número de professores visitantes utilizando o espaço de pesquisa: (30 pontos cada)':'n_profs_visitantes', 
                'Indique o número de servidores técnicos(as) ou secretários(as) utilizando o espaço de pesquisa: (10 pontos cada)':'servidores_técnicos_secretários', 
                'Indique o número de supervisões de pós-doutorado (finalizadas ou vigentes) dos docentes da EACH no grupo: (70 pontos cada)':'n_supervisões_pós-doutorado', 
                'Nome do Grupo de Pesquisa':'Grupo', 
                'O espaço de pesquisa utilizado é contínuo, ou seja, há contiguidade nos ambientes ocupados pelo grupo para atividades de pesquisa?':'contiguidade',
                'O espaço utilizado é ocupado por mais de um docente da EACH?':'Mais_de_um_Docente', 
                'O espaço utilizado é ocupado por mais de um grupo de pesquisa?':'Mais_de_um_grupo', 
                'O grupo está cadastrado no diretório de Grupos do CNPq?':'Cadastro_no_CNPQ', 
                'Por favor, inclua os currículos Lattes atualizados dos docentes da EACH pertencentes ao grupo para cômputo da produção docente (formato de arquivo xml, extraído diretamente da Plataforma Lattes):':'xmls', 
                'Quantas patentes os membros possuem?':'n_patentes_grupo',
                'Quantas produções artísticas, culturais e/ou técnica do Extrato A os membros do grupo possuem?':'produções_artist_culturais_A', 
                'Quantas produções artísticas, culturais e/ou técnica do Extrato B os membros do grupo possuem?':'produções_artist_culturais_B', 
                'Quantas produções artísticas, culturais e/ou técnica do Extrato C os membros do grupo possuem?':'produções_artist_culturais_C',
                'Quantos prêmios e honrarias os membros do grupo possuem?':'Quantidade_Prêmios_Honrarias', 
                'Quantos softwares os membros do grupo já desenvolveram?':'Qtd_Softwares', 
                'Quantos são os bolsistas de produtividade acadêmica de extrato 1A?':'bolsa_prodt_1A', 
                'Quantos são os bolsistas de produtividade acadêmica de extrato 1B?':'bolsa_prodt_1B', 
                'Quantos são os bolsistas de produtividade acadêmica de extrato 1C?':'bolsa_prodt_1C', 
                'Quantos são os bolsistas de produtividade acadêmica de extrato 1D?':'bolsa_prodt_1D', 
                'Quantos são os bolsistas de produtividade acadêmica de extrato 2?':'bolsa_prodt_2', 
                'Selecione a opção que melhor descreve a frequência de uso do espaço de pesquisa:':'frequência_uso', 
                'Selecione a opção que melhor descreve a natureza do uso do espaço de pesquisa:':'natureza_do_uso',
                'Timestamp':'Timestamp',
                'Indique o número de alunos de pós-graduação com bolsa utilizando o espaço de pesquisa: (60 pontos cada)':'alunos_pos_com_bolsa',
                'Indique o número de alunos de pós-graduação sem bolsa utilizando o espaço de pesquisa: (40 pontos cada)':'alunos_pos_sem_bolsa',
            }



    # renomeando as colunas do df
    dataframe = dataframe.rename(colunas,axis=1)
    # alterando a ordem das colunas do df

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

        #umatodos os campos que precisam ser contabilizados pelo programa 
        
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
    return(df)