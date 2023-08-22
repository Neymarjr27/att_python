def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def verificar_aprovacao(media):
    if media >= 7.0:
        return "APROVADO"
    elif 5.0 <= media < 7.0:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"


# Entrada das notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = calcular_media(nota1, nota2)

# Verificação da situação do aluno
situacao = verificar_aprovacao(media)

# Exibição da mensagem final
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
