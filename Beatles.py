import time

# Etapa 1: Criar uma lista vazia chamada beatles
beatles = []

# Etapa 2: Adicionar os membros iniciais à lista
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Etapa 3: Solicitar ao usuário para adicionar mais membros
for _ in range(2):  # Solicitar duas vezes, uma vez para Stu Sutcliffe e outra para Pete Best
    new_member = input("Digite o nome do próximo membro da banda: ")
    beatles.append(new_member)

# Etapa 4: Remover Stu Sutcliffe e Pete Best da lista
del beatles[-2:]  # Remove os dois últimos membros adicionados (Sutcliffe e Best)

# Etapa 5: Adicionar Ringo Starr ao início da lista
beatles.insert(0, "Ringo Starr")

# Exibir a lista final
print("Lista final dos membros dos Beatles:", beatles)


time.sleep(5)