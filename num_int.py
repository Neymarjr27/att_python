def decimal_to_binary(n):
    return bin(n)[2:]


def decimal_to_octal(n):
    return oct(n)[2:]


def decimal_to_hexadecimal(n):
    return hex(n)[2:]


def main():
    num = int(input("Digite um número inteiro: "))
    base = int(input("Escolha a base de conversão:\n1 para binário\n2 para octal\n3 para hexadecimal\n"))

    if base == 1:
        result = decimal_to_binary(num)
        print(f"O número {num} em binário é: {result}")
    elif base == 2:
        result = decimal_to_octal(num)
        print(f"O número {num} em octal é: {result}")
    elif base == 3:
        result = decimal_to_hexadecimal(num)
        print(f"O número {num} em hexadecimal é: {result}")
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()
