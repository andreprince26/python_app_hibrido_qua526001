 # import as funçoes
import modulo as m

m.limpar()
while True:
    print("1 - calcular quadrado")
    print("2 - calcular retamgulo")
    print("3 - calcular triangulo")
    print("4 - calcular circulo")
    print("5 - calcular trapezio")
    print("6 - sair do programa")
    opcao = input("opçao desejada: ").strip()
    m.limpar()
    match opcao:
        case "1":
            l = float(input("informe o lado do quadrado: ").strip().replace(",","."))
            m. limpar()
            area = m.quadrado(l)
            print(f"area do quadrado {area}")
            continue
        case "2":
            b = float(input("informe a base do triangulo: ").strip().replace(",","."))
            h = float(input("informe a altura do triangulo: ").strip().replace(",","."))
            continue
        case "3":
            b = float(input("informe a base do retangulo: ").strip().replace(",","."))
            b = float(input("informe a base do retangulo: ").strip().replace(",","."))
            m.limpar()
            area = m.triangulo(b, h)
            print(f"area do triangulo {area}")
            continue
            
        case "4":
            r = float(input("informe o raio do circulo: ").strip().replace(",","."))
            m.limpar()
            area = m.circulo(r)
            print(f"area do circulo {area}")
            continue
        case "5":
            b = float(input("informe a base menor do trapezio:").strip().replace(",","."))
            B = float(input("informe a base maior do trapezio:").strip().replace(",","."))
            h = float(input("informe a altura do trapezio:").strip().replace(",","."))
            m.limpar()
            area = m.trapezio(b, B, h)
            print(f"area do trapezio: {area}")
            continue
        case "6":
            break
        case _:
            print("opçao invalida.")
            continue
