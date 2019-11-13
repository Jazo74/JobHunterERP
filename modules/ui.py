
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
    for row in menus:
        print(chr(9) + "(" + str(index) + ") " + row)
        index += 1
    print(chr(9) + "(0) " + "Back to main menu or Exit program")
    print()

def print_table(table, titles): 
    width_titles = []
    for title in titles:
        width_titles.append(len(title))
    sum_lenght = 0
    for j in range(len(titles)):
        for i in table:
            if len(str(i[j])) > width_titles[j]:
                width_titles[j] = len(str(i[j]))
    for i in range(len(width_titles)):
        width_titles[i] += 2
        sum_lenght += width_titles[i] + 1
    sum_line = "-" * (sum_lenght-1)  
    just_line = ("|" + sum_line + "|")
    end_line = ("\\" + sum_line + "/")
    print()
    print("/" + sum_line + "\\")
    print("|", end ="")
    for index in range(len(titles)):
        print((titles[index]).center(width_titles[index]) + "|",end="")
    print()
    print(just_line)
    for i in range(len(table)):
        print("|",end="")
        for j in range(len(titles)):
            print(((str(table[i][j])).center(width_titles[j])) + "|",end="")
        print()
        if i+1 == len(table):
            print(end_line)
        else:
            print(just_line)
    print()