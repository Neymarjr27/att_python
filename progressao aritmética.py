def progressao_aritmetica(termo_inicial, diferenca_comum, numero_de_termos):
    pa = [termo_inicial + i * diferenca_comum for i in range(numero_de_termos)]
    return pa


try:
    termo_inicial = float(input("Digite o primeiro termo da PA: "))
    diferenca_comum = float(input("Digite a diferença comum da PA: "))
    numero_de_termos = int(input("Digite o número de termos desejado: "))

    pa = progressao_aritmetica(termo_inicial, diferenca_comum, numero_de_termos)

    print("Progressão Aritmética:")
    for termo in pa:
        print(termo, end=" ")

except ValueError:
    print("Por favor, insira valores numéricos válidos para o primeiro termo, diferença comum e número de termos.")
