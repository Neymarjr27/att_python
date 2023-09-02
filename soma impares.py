def soma_impares(inicio, fim):
    soma = 0

    for numero in range(inicio, fim + 1):
        if numero % 2 != 0:
            soma += numero

    return soma


# Defina o intervalo desejado aqui
inicio = 1
fim = 10

total_soma_impares = soma_impares(inicio, fim)
print(f"Soma dos números ímpares de {inicio} a {fim}: {total_soma_impares}")
