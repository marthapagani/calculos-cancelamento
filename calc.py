import datas

def proporcional (valorPlano, diasUtilizados): # função para calcular valor proporcional
    valorPagar = (valorPlano / 30) * diasUtilizados
    return valorPagar

def vigencia (meses): # função para calcular rescisão contratual
    valorPagar = meses * 25
    return valorPagar

valorFixoPlano = float(input("Valor do plano: R$ "))

boleto = input("Possui boleto em aberto? [S/N] ")

if boleto.upper() == "S": # tem boleto em aberto
    gerarProporcional = input("Vai efetuar pagamento do valor integral? [S/N] ")
    
    if gerarProporcional.upper() == "N":
        diasUtilizados = int(input("Dias de utilização: "))
        valorPlano = proporcional(valorFixoPlano, diasUtilizados)
    else:
        valorPlano = valorFixoPlano

possuiVigencia = input("Possui vigência contratual ativa? [S/N] ")

if possuiVigencia.upper() == "S": # tem meses de vigência contratual ativa
    meses = int(input("Quantos meses? [1-12] "))
    valorVigencia = vigencia(meses)
else:
    valorVigencia = 0

valorPlano += valorVigencia

print(f"Valor a ser pago será R$ {valorPlano}. ")