"""""""""""""""""""""""""""""""""""
        MERCADO DE TRABALHO
"""""""""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""""""
          IMPORTAÇÕES
"""""""""""""""""""""""""""""""""
import datetime as date

"""""""""""""""""""""""""""""""""
       PROGRAMA PRINCIPAL
"""""""""""""""""""""""""""""""""

def setVariables(year, month, colnames):
    estoque = f"estoque-{month}-{year}"
    colnames.append(estoque)

    admissoes = f"admissoes-{month}-{year}"
    colnames.append(admissoes)

    desligamentos = f"desligamentos-{month}-{year}"
    colnames.append(desligamentos)

    saldos = f"saldos-{month}-{year}"
    colnames.append(saldos)

    variacao = f"variacao-{month}-{year}"
    colnames.append(variacao)

def setColNames(colnames):
    # Adicionando aos meses-anos cada variável
    for year in range(2020, 2023):
        for month in range(1, 13):
            currentMonth = 3
            currentYear  = date.datetime.now().year

            if year == currentYear and month == currentMonth+1:
                break
            else:
                setVariables(year, month, colnames)
                month = ""









# if month <= currentMonth:
#     if month == 1:
#         month = "january"
#         setVariables(year, month, sjdr)
#     if month == 2:
#         month = "february"
#         setVariables(year, month, sjdr)
#     if month == 3:
#         month = "march"
#         setVariables(year, month, sjdr)
#     if month == 4:
#         month = "april"
#         setVariables(year, month, sjdr)
#     if month == 5:
#         month = "may"
#         setVariables(year, month, sjdr)
#     if month == 6:
#         month = "june"
#         setVariables(year, month, sjdr)
#     if month == 7:
#         month = "july"
#         setVariables(year, month, sjdr)
#     if month == 8:
#         month = "august"
#         setVariables(year, month, sjdr)
#     if month == 9:
#         month = "september"
#         setVariables(year, month, sjdr)
#     if month == 10:
#         month = "october"
#         setVariables(year, month, sjdr)
#     if month == 11:
#         month = "november"
#         setVariables(year, month, sjdr)
#     if month == 12:
#         month = "december"
#         setVariables(year, month, sjdr)
#     month = ""
# else:
#     if month <= currentMonth:
#         if month == 1 and currentMonth >= cont:
#             month = "january"
#             setVariables(year, month, sjdr)
#         if month == 2 and currentMonth >= cont:
#             month = "february"
#             setVariables(year, month, sjdr)
#         if month == 3 and currentMonth >= cont:
#             month = "march"
#             setVariables(year, month, sjdr)
#         if month == 4 and currentMonth >= cont:
#             month = "april"
#             setVariables(year, month, sjdr)
#         if month == 5 and currentMonth >= cont:
#             month = "may"
#             setVariables(year, month, sjdr)
#         if month == 6 and currentMonth >= cont:
#             month = "june"
#             setVariables(year, month, sjdr)
#         if month == 7 and currentMonth >= cont:
#             month = "july"
#             setVariables(year, month, sjdr)
#         if month == 8 and currentMonth >= cont:
#             month = "august"
#             setVariables(year, month, sjdr)
#         if month == 9 and currentMonth >= cont:
#             month = "september"
#             setVariables(year, month, sjdr)
#         if month == 10 and currentMonth >= cont:
#             month = "october"
#             setVariables(year, month, sjdr)
#         if month == 11 and currentMonth >= cont:
#             month = "november"
#             setVariables(year, month, sjdr)
#         if month == 12 and currentMonth >= cont:
#             month = "december"
#             setVariables(year, month, sjdr)
#         month = ""




