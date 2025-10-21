# declaraçao de variaveis
x = float(input("informe o 1º numero: ").strip().replace(",","."))
y = float(input("informe o 2º numero: ").strip().replace(",","."))

# menu
print("1 - soma")
print("2 - subtraçao")
print("3 - multiplicaçao")
print("4 - divisao")
operador = input("informe a operaçao desejada: ").strip()

# decisao
match operador:
    case "1":
        print(f"A soma e {x+y}")
    case "2":
        print(f"A subtraçao e {x-y}")
    case "3":
        print(f"A multiplicaçao e {x*y}")
    case "4":
        print(f"A divisao e {x/y}")
    case _:
        print("operaçao ivalida.") 


    