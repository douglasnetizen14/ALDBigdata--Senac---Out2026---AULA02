# Cáçculo do valor de uma corrida de taxi

distancia = float(input('digite a distãncia percorrida em km: '))
passageiros = int(input('numero de passageiros:  '))

valor_corrida = 8 +(distancia * 3)
valor_total = valor_corrida + 5
valor_por_pessoa= valor_total / passageiros

#saida
print(f'valor total da corrida:   R$ {valor_total:.2f}')
print(f'valor por pessoa:  R$ {valor_por_pessoa:.2f} ')
                        

