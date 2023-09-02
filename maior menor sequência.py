def encontrar_maior_menor(sequencia):
    if len(sequencia) == 0:
        return None, None

    maior = menor = sequencia[0]

    for numero in sequencia:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    return maior, menor


try:
    sequencia = []
    while True:
        entrada = input("Digite um número (ou 'fim' para encerrar): ")

        if entrada.lower() == 'fim':
            break

        numero = float(entrada)
        sequencia.append(numero)

    maior, menor = encontrar_maior_menor(sequencia)

    if maior is not None and menor is not None:
        print(f"O maior número é: {maior}")
        print(f"O menor número é: {menor}")
    else:
        print("A sequência está vazia, não é possível encontrar o maior e o menor.")

except ValueError:
    print("Por favor, insira números válidos.")
