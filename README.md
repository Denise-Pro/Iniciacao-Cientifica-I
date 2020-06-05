# Título 
<h1 align="center"> Iniciação Científica </h1>

# Descrição do Projeto
<p align="justify"> Projeto de Web Scraping e análise de dados (currículos lattes cadastrados no CNPQ) desenvolvido em Python 
 </p>

# Objetivo principal

Através desse código analisamos vários currículos lattes de pesquisadores que compõem os grupos de pesquisa da usp-leste, atribuímos pontuações a esses grupos com base em critérios pré-estabelecidos pela comissão de pesquisa e, essas pontuações servem para redistribuir de maneira mais justa os espaços disponíveis, na USP-leste, entre grupos de pesquisa, sendo que grupos com mais pontos tem prioridades em detrimento dos outros.

# Status do Projeto: 
Em desenvolvimento :warning:

# Sequência do Desenvolvimento

:heavy_check_mark: A princípio ja havia um programa em perl que extraía os lattes com formato xml (feito por um professor), do site do cnpq e os transformava para csv. Assim, a primeira etapa desse projeto foi pegar os dados dos pesquisadores em formato csv, fazer as devidas análises, atribuir as pontuações aos grupos de pesquisa e construir visualizações gráficas para apresentá-las.   

:heavy_check_mark: Na segunda etapa, percebemos que não seriam possíveis concluir determinadas análises, pois alguns dados não estavam disponíveis nos lattes dos pesquisadores. Diante desse fato, contruímos um formulário no Google forms e distribuímos entre os grupos com perguntas que não podiam ser respondidas analisando apenas os currículos dos mesmos.
Após obter as respostas via forms, eu construí um programa que extrai os dados via api deste forms. Usei a api do google Sheets para extrair os dados com formato xls.

:warning: A terceira etapa será refatorar o código, calcular medias as ponderadas e os outliers

:warning: A quarta e última etapa será extrair os currículos lattes diretamente da plataforma cnpq e analisá-los com o formato xml, sem precisar usar o programa secundário perl citado na primeira etapa. Toda a esrutura será mudada para atender o formato xml.

# Resumo das Funcionalidades

:trophy: Extrai dados com formato csv de arquivos que estão em diretórios locais 

:trophy: Extrai dados xls de Planilhas do Google (Google sheetes) via api 

:warning: Calcula Outliers (em breve) 

:warning: web scraping e parser de dados com formato xml (em breve) 

:warning: Resume as análises em visualizações gráficas (em breve)

# Desenvolvedores
[<img src="https://avatars2.githubusercontent.com/u/66394744?s=400&u=e5a0cd3c7d94c95ba5926502a2f80720ff814ff7&v=4" width=115 > <br> <sub> Denise Proença </sub>](https://github.com/Denise-Pro) 


[<img src="https://avatars3.githubusercontent.com/u/57142259?s=400&u=9ded641ffbfe9140fe8f2792bab86ac851716788&v=4" width=115 > <br> <sub> Ruanitto Docine </sub>](https://github.com/ruandocini)
