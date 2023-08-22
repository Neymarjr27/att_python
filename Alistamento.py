from datetime import datetime


def verificar_alistamento(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento

    if idade < 18:
        tempo_falta = 18 - idade
        print(f"Você ainda vai se alistar ao serviço militar. Faltam {tempo_falta} anos.")
    elif idade == 18:
        print("É hora de se alistar ao serviço militar!")
    else:
        tempo_passou = idade - 18
        print(f"Você já passou do tempo de alistamento. Passaram-se {tempo_passou} anos.")


# Lê o ano de nascimento do usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))
verificar_alistamento(ano_nascimento)
