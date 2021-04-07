#Modulos
import math
import random
import emoji
from playsound import playsound
#Entrada de dados - Num_Exercicio
ex = int(input("digite o numero do exercicio: "))
#Exercicios
if 16 == ex:
    num = float(input("digite um numero: "))
    real = math.floor(num)
    print(emoji.emojize(":arrow_right:{}".format(real),use_aliases=True))
elif 17 == ex:
    b = float(input("Digite o valor da Base: "))
    a = float(input("Digite o valor da Altura: "))
    hipotenusa = math.hypot(a, b)
    print("{:.2f}".format(hipotenusa))
elif 18 == ex:
    a = float(input("Digite o Angulo: "))
    cos = math.cos(a)
    sen = math.sin(a)
    tan = math.tan(a)
    print("Seno: {},Cosseno: {}, Tangente: {:.2f}".format(sen, cos, tan))
elif 19 == ex:
    alunos = []
    aluno = 1
    for x in range(0,4):
        alunos.append(input("Digite o aluno numero {}: ".format(aluno)))
        aluno = aluno + 1
    print(alunos)
elif 20 == ex:
    alunos = []
    aluno = 1
    for x in range(0, 4):
        alunos.append(input("Digite o aluno numero {}: ".format(aluno)))
        aluno = aluno + 1
    print(random.choices(alunos))
elif 21 == ex:
    playsound("C:/Users/wgeraldo/PycharmProjects/pythonProject/Estudo_Python/alicia.mp3")
#Saida
else:
    print("Exercicio Incorreto")
