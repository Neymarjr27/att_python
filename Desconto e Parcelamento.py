def calcular_valor_produto(preco, forma_pagamento, parcelas=1):
    if forma_pagamento == "avista-dinheiro" or forma_pagamento == "avista-cheque":
        valor_pago = preco * 0.9  # 10% de desconto
    elif forma_pagamento == "avista-cartao":
        valor_pago = preco * 0.95  # 5% de desconto
    elif forma_pagamento == "2x-cartao":
        valor_pago = preco  # Preço normal
    elif forma_pagamento == "3x-cartao" or parcelas >= 3:
        valor_pago = preco * 1.2  # 20% de juros
    else:
        return None  # Forma de pagamento inválida

    return valor_pago


# Exemplo de uso
preco_produto = float(input("Digite o preço do produto: "))
forma_pagamento = input(
    "Digite a forma de pagamento (avista-dinheiro, avista-cheque, avista-cartao, 2x-cartao, 3x-cartao): ")
parcelas_cartao = 1
if forma_pagamento == "2x-cartao" or forma_pagamento == "3x-cartao":
    parcelas_cartao = int(input("Digite o número de parcelas: "))

valor_final = calcular_valor_produto(preco_produto, forma_pagamento, parcelas_cartao)

if valor_final is not None:
    print(f"Valor a ser pago: R$ {valor_final:.2f}")
else:
    print("Forma de pagamento inválida.")
