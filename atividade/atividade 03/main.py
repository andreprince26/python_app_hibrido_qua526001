
try:        #  todo vez q coloca try tem q coloca except

    nome = input("nome do usuario: ").strip().title()
    peso = float(input("informe o peso e, Kg: ").strip().replace(",","."))
    altura = float(input("informe o altura em metros: ").strip().replace(",","."))

    # calcular IMC
    imc = peso/(altura**2)

    # exibi o IMC do usuario
    print(f"{nome}, seu {imc:.2f}")

    # diagnostico do imc
    if imc < 18.5:
        print(f"{nome} esta abaixo do peso.")
    elif imc < 25:
        print(f"{nome} esta no peso ideal.")
    elif imc < 30:
        print(f"{nome} esta acima do peso.")
    elif imc < 35:
        print(f"{nome} esta obeso.")
    elif imc < 40:
        print(f"{nome} esta com obsesidade mórbida.")
except Exception as e:       #pra mostra o tipo de erro
    print(f"deu ruim!!! {e}")



