# biblioteca
import os
  
# declaraçao de lista
nomes = []

#limpa o console
os.system("cls")

#loop
while True:
    #menu
    print("1 - Inserir novo nome")
    print("2 - Exibir lista de nome")
    print("3 - Excluir nome na lista")
    print("4 - Sair do programa")
    opcao = input("informe a opçao desejada: ").strip()
    match opcao:
        case "1":
            os.system("cls")
            novo_nome = input("informe o novo nome: ").strip().title()
            nomes.append(novo_nome)  # insere novo nome na lista
            os.system("cls")
            print(f"{novo_nome} cadastrado com sucesso.")
            continue
        case "2":
            os.system("cls")
            print("lista de nomes:\n")
            for i in range(len(nomes)):  # fixme
                print(f"{i} - {nomes[i]}")   #lista o nome na lista
            print(f"\n{'-'*40}\n")    
            continue    
        case "3":
            os.system("cls")
            try:
                posicao = int(input("informe a posiçao a ser excluida: ").strip())
                if posicao >= 0 and posicao < len(nomes):
                    del(nomes[posicao])
                    print("nome excluido com sucesso.")
                else:
                    print("posiçao inexistente.")
            except Exception as e:
                print(f"posiçao invalida. {e}.")
                continue
        case "4":
            print("programa encerrado.")
            break
        case _:
            print("opçao invalida.")
            continue
