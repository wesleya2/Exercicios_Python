valorCompra = float(input("Valor da compra R$ "))
numParcelas = int(input("Numero de Parcelas: "))
valorFinal = valorCompra
if numParcelas == 1:
    valorFinal = valorCompra * 0.9
    print("Valor a ser pago R${:.2f}".format(valorFinal))
elif numParcelas == 4:
    valorFinal = valorCompra * 1.05
    print("Valor a ser pago R${:.2f}".format(valorFinal))
elif numParcelas == 5:
    valorFinal = valorCompra * 1.06
    print("Valor a ser pago R${:.2f}".format(valorFinal))
elif numParcelas == 6:
    valorFinal = valorCompra * 1.08
    print("Valor a ser pago R${:.2f}".format(valorFinal))
elif numParcelas == 2:
    valorFinal = valorCompra
    print("Valor a ser pago R${:.2f}".format(valorFinal))
elif numParcelas == 3:
    valorFinal = valorCompra
    print("Valor a ser pago R${:.2f}".format(valorFinal))
else:
    print("Numero de parcelas não pode ser maior que 6")

