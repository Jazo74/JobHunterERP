import misc
import ui

def menu_options_students():
    while True:
        inputs = input("Please choose a number!")
        option = inputs
        if option == "1":
            pass    
        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "4":
            pass
        elif option == "5":
            pass
        elif option == "6":
            pass
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        break

def init():
    while True:
        ui.print_program_menu(["Create Student", "Show student", "Show all students", "Update student", "Activate/Deactivate student", "Delete student"])
        try:
            menu_options_students()
        except KeyError as err:
            ui.print_message(str(err))