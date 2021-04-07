#variavél semaforo é do tipo string
semaforo = input("Qual o estado do semarofo? ").upper()
if semaforo == "verde":
    passos = int(input("Quantos Passos? "))
    tempo = float(input("Em quanto tempo? "))
    print("Como o semáforo estava {} eu caminhei {} passos".format(semaforo,passos))
    print("Utilizei {} segundos para caminhar {} passos".format(tempo,passos))
    velocidade = passos / tempo
    print("Velocidade que eu caminhei foi de {:.2f} passos por segundo".format(velocidade))
else:
    print("O semaforo não esta verde, Aguarde!")




#print ("Tipo de dado na variável semáforo: {}".format(type(semaforo)))
#print ("Tipo de dado na variável passos: {}".format(type(passos)))
#print ("Tipo de dado na variável tempo: {}".format(type(tempo)))




