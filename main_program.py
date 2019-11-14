"""
The main program
"""
import os
import sys
from modules import ui
from modules import students
from modules import companies
from modules import positions
from modules import applications


def menu_options():
    while True:
        inputs = input("Please choose a number!")
        option = inputs
        if option == "1":
            students.init()    
        elif option == "2":
            companies.init()
        elif option == "3":
            positions.init()
        elif option == "4":
            applications.init()
        elif option == "0":
            sys.exit(0)
        else:
            raise KeyError("There is no such option.")
        break
def main():
    
    while True:
        ui.print_program_menu(["Students", "Companies", "Positions", "Applications"])
        try:
            menu_options()
        except KeyError as err:
            ui.print_message(str(err))
        

if __name__ == '__main__':
    main()
