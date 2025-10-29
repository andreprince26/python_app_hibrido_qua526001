#  [] declaraçao de lista
nomes = ["Andre", "Luiz", "Souza", "Moreira"]

# exibi o primeiro nome ///for e um laço de repeçao
for nome in nomes:
    print(nome)

# ordena a lista em ordem alfabetica
nomes.sort()

# re-exibir a lista em ordem alfabetica\\\.\n e quebra de linha
print("\nOrdem Alfabetica:\n")
for nome in nomes:
    print(nome)

#reverte a ordem da lista
nomes.sort(reverse=True)

print("\nOrdem Alfabetica reversa:\n")
for nome in nomes:
    print(nome)

