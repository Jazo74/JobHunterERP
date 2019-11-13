import os

def user_input(message, questions):
    print(message)
    answers = []
    for ask in questions:
        answers.append(input(ask))
    return answers


def print_message(message):
    print()
    print(message)
    print()

def print_program_menu(menus):
    
    print()
    index = 1
    os.system("clear")
    for row in menus:
        print("(" + str(index) + ")" + row + "  ", end="")
        index += 1
    print("(0)" + "Exit program")
    print()
