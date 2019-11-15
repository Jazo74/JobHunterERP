from modules import misc
from modules import ui
from modules import file_handling

def menu_options_applications():
    file_application = "databases/applications.csv"
    file_students = "databases/students.csv"
    file_positions = "databases/positions.csv"
    while True:
        inputs = input("Please choose a number! ")
        option = inputs
        if option == "1":
            create_application(file_application, file_students, file_positions) 
        elif option == "2":
            update_application(file_application)
        elif option == "3":
            delete_application(file_application)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        break

def init():
    while True:
        ui.print_program_menu(["Create application", "Update application", "Delete application"])
        try:
            menu_options_applications()
        except KeyError as err:
            ui.print_message(str(err))

def create_application(filename, filename_2, filename_3):
    table = file_handling.import_data(filename) #import position table
    table_2 = file_handling.import_data(filename_2) #import company table
    table_3 = file_handling.import_data(filename_3) #import company table
    students_list = []
    for record in table_2:
        students_list.append(record[0])
    positions_list = []
    for record in table_3:
        positions_list.append(record[0])
    data = ui.user_input("Please give me the position's data", ["Accepted: "]) # user input
    while True:
        temp_student_id = ui.user_input("", ["Student ID: "])
        if temp_student_id[0] in students_list:
            break
        ui.print_message("Wrong Student ID")
    while True:
        temp_position_id = ui.user_input("", ["Postition ID: "])
        if temp_position_id[0] in positions_list:
            break
        ui.print_message("Wrong Position_ID")
    data.append(temp_student_id[0])
    data.append(temp_position_id[0])
    id = misc.generate_random(table)  # generate id
    new_table = misc.append_table(table, misc.build_record(id, data)) # making new table
    file_handling.export_data(new_table, filename, "w") # saving the new table


def delete_application(filename):
    table = file_handling.import_data(filename) #import table
    id = ui.user_input("Please give me the application's ID", ["ID: "]) # user input, ID
    for index in range(len(table)): # deleting an element from the table by index
        if table[index][0] != id[0]:
            del table[index]
            break
    file_handling.export_data(table, filename, "w")

def update_application(filename):
    table = file_handling.import_data(filename) #import table
    id = ui.user_input("Please give me the application's ID", ["ID: "]) # user input, ID
    data = ui.user_input("Please give me the application's data", ["Accepted: "]) # user input, Active?
    new_table = []
    for record in table:
        if record[0] != id[0]:
            new_table.append(record)
        else:
            record[1] = data[0]
            new_table.append(record)
    file_handling.export_data(new_table, filename, "w") # saving the new table