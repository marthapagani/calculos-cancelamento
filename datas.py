from datetime import date

#def formatacao(dia, mes, ano):
#    saida = input()

def numeroDeDias(inicio, fim):
    return abs((inicio - fim).days)

# necessário adaptar pra receber input de usuário

dia1 = date(2022, 10, 20)
dia2 = date(2022, 11, 3)

dias = numeroDeDias(dia1, dia2)
print(dias)