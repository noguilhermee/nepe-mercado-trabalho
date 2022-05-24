"""""""""""""""""""""""""""""""""""
        MERCADO DE TRABALHO
"""""""""""""""""""""""""""""""""""
# 316250 = São João del-Rei
# 312230 = Divinópolis
# 310560 = Barbacena
# 313820 = Lavras


"""""""""""""""""""""""""""""""""
          IMPORTAÇÕES
"""""""""""""""""""""""""""""""""
import pandas as pd
import datetime as date

"""""""""""""""""""""""""""""""""
       PROGRAMA PRINCIPAL
"""""""""""""""""""""""""""""""""

def getCityDataframe(sjdr, df_sjdr):
    for year in range(2020, 2022 + 1):
        for month in range(1, 12 + 1):
            currentMonth = 3
            currentYear = date.datetime.now().year

            if year == currentYear and month == currentMonth + 1:
                break
            else:
                data = f"{month}-{year}"
                estoque = f"estoque-{month}-{year}"
                admissoes = f"admissoes-{month}-{year}"
                desligamentos = f"desligamentos-{month}-{year}"
                saldos = f"saldos-{month}-{year}"
                variacao = f"variacao-{month}-{year}"
                line = {
                    'data': data,
                    'estoque': sjdr[f"{estoque}"].values[0],
                    'admissoes': sjdr[f"{admissoes}"].values[0],
                    'desligamentos': sjdr[f"{desligamentos}"].values[0],
                    'saldos': sjdr[f"{saldos}"].values[0],
                    'variacao': sjdr[f"{variacao}"].values[0],
                }
                df_sjdr.loc[data] = line

