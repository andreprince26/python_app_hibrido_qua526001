#loop
while True:
    try:
        # menu
        print("1 - Soma")
        print("2 - Subtraçao")
        print("3 - Multiplicaçao")
        print("4 - Divisao")
        print("5 - Sair do programa")
        opcao = input("informe a opcao desejada: ").strip()

        if opcao != "5":
            n1 = int(input("informe o 1° numero: ").strip())
            n2 = int(input("informe o 2º numero: ").strip())

            match opcao:
                case "1":
                    result = n1+n2
                    print(f"o resultado da soma é {result}")
                    continue
                case "2":
                    result = n1-n2
                    print(f"o resultado da subtraçao é: {result}")
                    continue
                case "3":
                    result = n1*n2
                    print(f"o resultado da multiplicaçao é: {result}")
                    continue
                case "4":
                    result = n1/n2
                    print(f"o resultado da divisao é: {result}")    
                    continue
                case _:
                    print("opcao invalido.")
                    continue
            
        else:
            print("programa encerrado.")
            break
    except:
        print("valores invalidos.")