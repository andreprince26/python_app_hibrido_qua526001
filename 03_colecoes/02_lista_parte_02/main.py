# declaraçao de lista
nomes = []

try: 
    while True:
     print("1 - inserir nome na lista")
     print("2 - exibir lista")
     print("3 - sair domprograma")
     opcao = input("informe opçao desejada:").strip()
     match opcao:
         case "1":
           novo_nome = input("informe o novo nome:").strip().title()
           nomes.append(novo_nome)
           print(f"{novo_nome} inserido com sucesso:")
         case "2":
           print("\nlista de nomes:\n")
           for nome in nomes:
              print(nome)
         case "3":
           break
         case _:
           print("opçao invalida.")
           continue

except Exception as e:
    print(f"erro ao exibir a lista. {e}.")
finally:
    print("programa encerrado.") 