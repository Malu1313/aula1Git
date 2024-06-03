import time

# #Biblioteca para retornar um número inteiro aleatório
# from  random import randint as rd
# sorteado = rd(-100, 100) #sorteia um número de -100 a 100

# #Criando uma lista de números inteiros aleatórios
# lista = [rd(1,6) for i in range(1,11)]
# lista2 = [x for x in range (1, 11)]
# lista3 = ["Rolo compressor!!!" for f in range (1, 5)]
# # print(lista)
# # print(lista2)
# # print(lista3)

# #criando lista par
# # par = [i for i in range(10) if i%2 == 0]
# # print(par)

# # #Povoando uma lista com "input"
# # listaUsuario = [input("Digite um número: ") for p in range(5)]
# # print(listaUsuario)

# #Utilizando o método split(cada palavra se torna um elemento da lista)
# nome = "Mickey Mouse"
# # print(nome)
# # print(nome.split())
# # print(nome)

# #aplicando o "split" com o input
# # notas = [n for n in input("Notas: "). split()]
# # print(notas)

# notas2 = [float(n) for n in input("Notas: "). split(",")]
# print(notas2)

#Lista com tipos diferentes de dados
listaMista = [17, 70.5, "Sem Mundial!", True]
#print(listaMista)


#Manipulação / Fatiamento de Listas
veiculos1 = ["carros", "bicicleta", "motor"]
print("Veículos1:", veiculos1)

#Copiando todo o conteúdo de uma lista para outra
veiculos2 = veiculos1[:]
del veiculos1[2]
print("Veículos 1:", veiculos1)
print("Veículos 2:", veiculos2)

#Copiando parte do conteúdo de uma lista
veiculos3 = veiculos2[0:1]
print(veiculos3)

#copiando parte do conteúdo, incluindo o último elemento
veiculos4 = veiculos2[0:-1]
print(veiculos4)

veiculos5 = veiculos2[-1: 1]
print(veiculos5)

#Outra maneira de fatiamento (omissão do star ou do end)
my_list = ["A", "B", "C", "D", "E", "F"]
print(my_list)
new_list = my_list[:3]
print(new_list)
new_list_fim = my_list[5:]
print(new_list_fim)

#Apagando conteúdo de listas
del my_list[1:3]
print(my_list)
del my_list[:] #apaga todo o conteúdo
print(my_list)

del my_list
print(my_list)

#Testando se alfuns itens existem em uma lista ou não
#Para isso, usamos palavras chaves chave in e not in:
naosei = ["A", "B", 18, 15]
print("A" in naosei)

time.sleep(3)