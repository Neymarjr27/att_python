def calcular_emprestimo():
    valor_casa = float(input("Digite o valor da casa: "))
    salario_comprador = float(input("Digite o salário do comprador: "))
    anos_prazo = int(input("Digite a quantidade de anos para pagar: "))


    prestacao_maxima = salario_comprador * 0.3
    valor_prestacao = valor_casa / (anos_prazo * 12)

    if valor_prestacao <= prestacao_maxima:
        print("Empréstimo aprovado!")
        print(f"Valor da prestação mensal: R${valor_prestacao:.2f}")
        print('Entre em contato com o corretor 61 9 1234-5678')
    else:
        print("Empréstimo negado. Valor da prestação excede 30% do salário.")


calcular_emprestimo()