
def print_message(message):
    print()
    print(message)
    print()

def print_program_menu(menus):
    
    print()
    index = 1
    for row in menus:
        print(chr(9) + "(" + str(index) + ") " + row)
        index += 1
    print(chr(9) + "(0) " + "Back to main menu or Exit program")
    print()
