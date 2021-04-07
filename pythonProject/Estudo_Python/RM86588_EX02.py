#variaveis
contadori = 1
contadorp = 2
mediai = 0
media_totali = 0
mediap = 0
media_totalp = 0
#receber notas de alunos impares
while (contadori <= 50):
    print("Você esta digitando as notas dos alunos ímpares")
    mediai = float(input("Por Favor, insira a nota do aluno numero {}: ".format(contadori)))
    media_totali = media_totali + mediai
    contadori = contadori + 2
#receber notas de alunos pares
while (contadorp <= 50):
    print("Você esta digitando as notas dos alunos pares")
    mediap = float(input("Por Favor, insira a nota do aluno numero {}: ".format(contadorp)))
    media_totalp = media_totalp + mediap
    contadorp = contadorp + 2
#calculo media alunos impares e pares
media_totali = media_totali / 25
media_totalp = media_totalp / 25

#exibir maior media
if (media_totali > media_totalp):
    print("A media dos alunos ímpares foi de: {:.2f}".format(media_totali))
    print("A media dos alunos pares foi de: {:.2f}".format(media_totalp))
    print("A maior media foi dos alunos Impares")
elif (media_totalp > media_totali):
    print("A media dos alunos pares foi de: {:.2f}".format(media_totalp))
    print("A media dos alunos impares foi de: {:.2f}".format(media_totali))
    print("A maior media foi dos alunos pares")
else:
    print("A media entre os alunos impares e pares é igual. Média: {:.2f} ".format(media_totali))