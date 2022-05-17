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


"""""""""""""""""""""""""""""""""
       PROGRAMA PRINCIPAL
"""""""""""""""""""""""""""""""""

os.getcwd()
os.chdir('D:\\Programing\\python\\nepe\\nepe-mercado-trabalho\\Data')

df_caged = pd.read_table('202203\\CAGEDFOR202203.txt', sep=";")
df_caged.to_excel('dados-caged.xlsx')



df_sjdr = df_caged[(df_caged['município']==316250)]
df_sjdr.to_excel('dados-sjdr.xlsx')




conditionList = [
    (df_caged['município'] == 316250),
]
choiceList = ['competênciamov']

df_sjdr = np.select(conditionList, choiceList)










