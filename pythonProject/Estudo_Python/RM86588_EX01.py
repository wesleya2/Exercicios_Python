# Programa calculadora calorias
# Solicita a quantidade de alimentos consumidos no dia
qtd_alimentos = float(input("Informe a quantidade de alimentos consumidos no dia: "))
# defini que o valor inicial do total é 0
total_calorias = 0
#contador alimentos
cont_alimentos = 1
# Sequencia para calculo do total de calorias
while (qtd_alimentos > 0):
    qtd_calorias = float(input("Informe a qtd de calorias do alimento {}: ".format(cont_alimentos)))
    total_calorias = total_calorias + qtd_calorias
    cont_alimentos = cont_alimentos + 1
    qtd_alimentos = qtd_alimentos - 1
# Imprime a quantidade total de alimentos consumidos
print("A quantidade de calorias consumidas foi de: {:.2f}".format(total_calorias))
