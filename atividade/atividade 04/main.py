try:
    nome = input ("informe seu nome: ").strip().title()
    idade = int(input("informe sua idade: ").strip())

    #lista de filme
    sala_1 = "A Roda Quadrada"
    sala_2 = "A Volta dos que nao foram"
    sala_3 = "A Poeira em Alto Mar"
    sala_4 = "As Trancas do Rei Careca"
    sala_5 = "A Vingança do Frago Assado"

    #loop
    while True:
        # menu de filmes
        print(f"sala 1 - {sala_1} - Livre")
        print(f"sala 2 - {sala_2} - 12 anos")
        print(f"sala 3 - {sala_3} - 14 anos")
        print(f"sala 4 - {sala_4} - 16 anos")
        print(f"sala 5 - {sala_5} - 18 anos")
        sala = input("informe a sala desejada: ").strip()

        # verifica a sala selecionada
        match sala:
            case "1": 
                filme = sala_1
                idade_minima = 0 
                pass
            case "2":
                filme = sala_2
                idade_minima = 12
                pass
            case "3":
                fime = sala_3
                idade_minima = 14
                pass
            case "4":
                filme = sala_4
                idade_minima = 16
                pass
            case "5":
                filme = sala_5
                idade_minima = 5
            case _: 
                print(" sala inexistente.")
        if idade >= idade_minima:
            print (f"{nome} escolheu {filme}. tenha um bom filme!")
            break
        else:
            print(f"{nome} nao foi autorixado a ver {filme}.")
        continue
except Exception as e:
    print(f"erro no programa. {e}")

