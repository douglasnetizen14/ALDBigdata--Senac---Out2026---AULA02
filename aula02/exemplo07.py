#Valor d\ compra Mesmo Valor

preço = float(input('informe o preço:  '))
quantidade =int(input('digite a quantidade:   '))


#processamento
subtotal = preço * quantidade
desconto = subtotal *0.1
total = subtotal - desconto


10
# saida
print(f'valor sem desconto R$ {subtotal}')
print(f'desconto de R$ {desconto}')
print(f'total a pagar: R$ {total}')