from modules import misc
from modules import ui
from modules import file_handling

def menu_options_students():
    filename = "databases/students.csv"
    message = "Please give me the student's data!"
    while True:
        inputs = input("Please choose a number! ")
        option = inputs
        if option == "1":
            table = file_handling.import_data(filename)
            file_handling.export_data(create_student(table), filename, "w")    
        elif option == "2":
            table = file_handling.import_data(filename)
            id = ui.user_input(message,["ID: "])
            read_student(table, id[0])  
        elif option == "3":
            table = file_handling.import_data(filename)
            read_students(table)  
        elif option == "4":
            table = file_handling.import_data(filename)
            file_handling.export_data(update_student(table), filename, "w")
        elif option == "5":
            table = file_handling.import_data(filename)
            id = ui.user_input(message,["ID: "])
            file_handling.export_data(create_student(table, id[0]), filename, "w")
        elif option == "6":
            questions = ["ID: "]
            id = ui.user_input(message, "ID: ")
            table = file_handling.import_data(filename)
            file_handling.export_data(delete_student(table, id[0]), filename, "w")
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

def create_student(table):
    message = "Please give me the student's datas!"
    questions = ["Name: ", "Age: ", "Active(yes or no): "]
    misc.append_record(table, ui.user_input(message, questions))
    return table

def update_student(table, id, data):
    message = "Please give me the student's ID!"
    questions = ["ID: "]
    id = ui.user_input(message, questions)
    new_table = []
    for record in table:
        if record[0] != id[0]:
            new_table.append(record)
        else:
            message = "Please give me the student's datas!"
            questions = ["Name: ", "Age: ", "Active(yes or no): "]
            answers = ui.user_input(message, questions)
            new_table.append([id[0], answers[0], answers[1], answers[2]])
    return new_table

def delete_student(table, id):
    new_table = []
    for record in table:
        if record[0] != id:
            new_table.append(record)
    return new_table

def read_students(table):
    titles = ["ID", "Name", "Age", "Status"]
    ui.print_table(table, titles)

def read_student(table, id):
    titles = ["ID", "Name", "Age", "Status"]
    filtered_table = []
    for record in table:
        if record[0] == id:
            filtered_table.append(record)
            ui.print_table(filtered_table, titles)