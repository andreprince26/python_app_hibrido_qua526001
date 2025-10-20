# declaraçao de variavel
nome = input("informe seu nome: ").strip().title() # elimina espaço strip,title coloca as letras maiuscula no incio
idade = int(input("informe sua idade: ").strip())
altura = float(input("informe sua altura: ").strip().replace(",","."))

# saida de dados
print(f"nome do usuario: {nome}. tipo: {type(nome)}")
print(f"idade: {idade}. Tipo:{type(idade)}")
