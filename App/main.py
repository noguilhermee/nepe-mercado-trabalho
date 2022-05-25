"""""""""""""""""""""""""""""""""""
    NEPE - MERCADO DE TRABALHO
"""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""
          IMPORTAÇÕES
"""""""""""""""""""""""""""""""""
import os
import numpy as np
import pandas as pd
import datetime as date
import matplotlib.pyplot as plt

import Functions.caged as caged


"""""""""""""""""""""""""""""""""
       PROGRAMA PRINCIPAL
"""""""""""""""""""""""""""""""""

# Selecionando o diretório
os.getcwd()
os.chdir('D:\\Programing\\python\\ufsj\\nepe\\mercado-trabalho\\Data')

# Cidade e retornar um DataFrame
df_sjdr = caged.get_city_by_code(316250)


# Manipulação
estoque_sjdr = df_sjdr['estoque']
estoque_div = df_div['estoque']
estoque_lavras = df_lavras['estoque']
estoque_barbacena = df_barbacena['estoque']

estoque_sjdr.to_excel('estoque-sjdr.xlsx')
estoque_div.to_excel('estoque-div.xlsx')
estoque_lavras.to_excel('estoque-lavras.xlsx')
estoque_barbacena.to_excel('estoque-barbacena.xlsx')


