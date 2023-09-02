import time

def contagem_regressiva(numero_inicial):
    for i in range(numero_inicial, -1, -1):
        print(i)
        time.sleep(1)  # Aguarda 1 segundo entre cada contagem

    print("Contagem regressiva concluída!")

# Defina o número inicial da contagem regressiva aqui
numero_inicial = 10

contagem_regressiva(numero_inicial)
