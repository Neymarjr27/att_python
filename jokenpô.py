import random


def get_user_choice():
    user_choice = input("Escolha pedra, papel ou tesoura: ")
    return user_choice.lower()


def get_computer_choice():
    choices = ['pedra', 'papel', 'tesoura']
    computer_choice = random.choice(choices)
    return computer_choice


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate!"
    elif user_choice == 'pedra':
        return "Você ganhou!" if computer_choice == 'tesoura' else "Você perdeu!"
    elif user_choice == 'papel':
        return "Você ganhou!" if computer_choice == 'pedra' else "Você perdeu!"
    elif user_choice == 'tesoura':
        return "Você ganhou!" if computer_choice == 'papel' else "Você perdeu!"
    else:
        return "Escolha inválida!"


def main():
    print("Bem-vindo ao Jokenpô!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Você escolheu: {user_choice}")
    print(f"O computador escolheu: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)


if __name__ == "__main__":
    main()
