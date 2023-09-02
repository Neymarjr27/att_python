def contagem_pares(inicio, fim):
    contador_pares = 0

    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            contador_pares += 1

    return contador_pares


# Defina o intervalo desejado aqui
inicio = 1
fim = 100

total_pares = contagem_pares(inicio, fim)
print(f"Total de números pares de {inicio} a {fim}: {total_pares}")
