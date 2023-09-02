def tabuada_v2(base, termos):
    print(f"Tabuada do {base} (com {termos} termos):")

    for i in range(1, termos + 1):
        resultado = base * i
        print(f"{base} x {i} = {resultado}")


try:
    base = int(input("Digite a base da tabuada: "))
    termos = int(input("Digite o número de termos desejado: "))

    tabuada_v2(base, termos)
except ValueError:
    print("Por favor, insira valores inteiros válidos para a base e o número de termos.")
