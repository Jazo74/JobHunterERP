from modules import misc
from modules import ui
from modules import file_handling

def menu_options_students():
    file_student = "databases/students.csv"
    while True:
        inputs = input("Please choose a number! ")
        option = inputs
        if option == "1":
            create_student(file_student)
        elif option == "2":
            read_student(file_student)  
        elif option == "3":
            read_students(file_student)  
        elif option == "4":
            update_student(file_student)
        elif option == "5":
            state_student(file_student)
        elif option == "6":
            delete_student(file_student)
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

def create_student(filename):
    table = file_handling.import_data(filename) #import table
    data = ui.user_input("Please give me the student's data", ["Name: ", "Age: ", "Active?: "]) # user input
    id = misc.generate_random(table)  # generate id
    new_table = misc.append_table(table, misc.build_record(id, data)) # making new table
    file_handling.export_data(new_table, filename, "w") # saving the new table

def update_student(filename):
    table = file_handling.import_data(filename) #import table
    id = ui.user_input("Please give me the student's ID", ["ID: "]) # user input, ID
    data = ui.user_input("Please give me the student's data", ["Name: ", "Age: ", "Active?: "]) # user input, rest info
    new_table = misc.update_table(table, id[0], misc.build_record(id[0], data)) # updating the table
    file_handling.export_data(new_table, filename, "w") # saving the new table

def delete_student(filename):
    table = file_handling.import_data(filename) #import table
    id = ui.user_input("Please give me the student's ID", ["ID: "]) # user input, ID
    for index in range(len(table)): # deleting an element from the table by index
        if table[index][0] != id[0]:
            del table[index]
            break
    file_handling.export_data(table, filename, "w")

def read_students(filename):
    table = file_handling.import_data(filename)
    titles = ["ID", "Name", "Age", "Status"]
    ui.print_table(table, titles)


def read_student(filename):
    table = file_handling.import_data(filename) # import table
    id = ui.user_input("Please give me the student's ID",["ID: "]) # user input, ID
    titles = ["ID", "Name", "Age", "Status"]
    filtered_table = []
    for record in table:
        if record[0] == id[0]:
            filtered_table.append(record)
            ui.print_table(filtered_table, titles)

def state_student(filename):
    table = file_handling.import_data(filename) #import table
    id = ui.user_input("Please give me the student's ID", ["ID: "]) # user input, ID
    data = ui.user_input("Please give me the student's data", ["Active?: "]) # user input, Active?
    new_table = []
    for record in table:
        if record[0] != id[0]:
            new_table.append(record)
        else:
            record[3] = data[0]
            new_table.append(record)
    file_handling.export_data(new_table, filename, "w") # saving the new table