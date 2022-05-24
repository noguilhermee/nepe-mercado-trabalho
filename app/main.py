"""""""""""""""""""""""""""""""""""
        MERCADO DE TRABALHO
"""""""""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""""""
          IMPORTAÇÕES
"""""""""""""""""""""""""""""""""
import os
import numpy as np
import pandas as pd
import datetime as date
import matplotlib.pyplot as plt

import functions.colnames as fcolname
import functions.cities as fcity


"""""""""""""""""""""""""""""""""
          FUNÇÕES
"""""""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""""""
       PROGRAMA PRINCIPAL
"""""""""""""""""""""""""""""""""

# Selecionando o diretório
os.getcwd()
os.chdir('D:\\Programing\\python\\ufsj\\nepe\\nepe-mercado-trabalho\\data')

# Criando um array para as colunas e importando os dados
colnames = ['uf','code','city']
fcolname.setColNames(colnames)

uri = 'https://github.com/nogueira-guilherme/nepe-mercado-trabalho/blob/master/data/caged-tabela.xlsx?raw=true'
caged = pd.read_excel(uri, sheet_name='Tabela 8.1', usecols='B:EI', nrows=(5577-7), skiprows=6, names=colnames)


# Selecionando os dados de São João del-Rei
sjdr = caged[(caged['code'] == 316250)]
sjdr = sjdr.fillna(0) # substituir dos valores não identificados (nan -> 0)

div = caged[(caged['code'] == 312230)]
div = div.fillna(0)

lavras = caged[(caged['code'] == 313820)]
lavras = lavras.fillna(0)

barbacena = caged[(caged['code'] == 310560)]
barbacena = barbacena.fillna(0)


# Criando um DataFrame para São João del-Rei
df_sjdr = pd.DataFrame(columns=['data', 'estoque', 'admissoes', 'desligamentos', 'saldos', 'variacao'])
df_div = pd.DataFrame(columns=['data', 'estoque', 'admissoes', 'desligamentos', 'saldos', 'variacao'])
df_lavras = pd.DataFrame(columns=['data', 'estoque', 'admissoes', 'desligamentos', 'saldos', 'variacao'])
df_barbacena = pd.DataFrame(columns=['data', 'estoque', 'admissoes', 'desligamentos', 'saldos', 'variacao'])


# Transformando o DataFrame: colunas->linhas
fcity.getCityDataframe(sjdr, df_sjdr)
fcity.getCityDataframe(div, df_div)
fcity.getCityDataframe(lavras, df_lavras)
fcity.getCityDataframe(barbacena, df_barbacena)


# Reiniciar os index das linhas
df_sjdr = df_sjdr.reset_index()
df_div = df_div.reset_index()
df_lavras = df_lavras.reset_index()
df_barbacena = df_barbacena.reset_index()


# Manipulação
estoque_sjdr = df_sjdr['estoque']
estoque_div = df_div['estoque']
estoque_lavras = df_lavras['estoque']
estoque_barbacena = df_barbacena['estoque']

estoque_sjdr.to_excel('estoque-sjdr.xlsx')
estoque_div.to_excel('estoque-div.xlsx')
estoque_lavras.to_excel('estoque-lavras.xlsx')
estoque_barbacena.to_excel('estoque-barbacena.xlsx')
