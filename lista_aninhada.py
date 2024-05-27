import time

#Criando uma lista dentro de outra lista usando o For
lista = [[x for x in range(4)] for i in range(5)]

print(lista)

lista2 = [12, 17, 22, 45, 32]

print(lista2)

lista2.sort()

print(lista2)

print(lista2[3])

lista2.reverse()

print(lista2)

time.sleep(5)