"""
The main program
"""
import os
import sys
import ui
from students import students
from companies import companies
from positions import positions
from applications import applications


def menu_options():
    while True:
        inputs = input("Please choose a number (from 0 to 4): ")
        option = inputs
        if option == "1":
            pass    
        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "4":
            pass
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
