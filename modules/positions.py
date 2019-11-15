from modules import misc
from modules import ui
from modules import file_handling

def menu_options_positions():
    file_position = "databases/positions.csv"
    file_companies = "databases/companies.csv"
    while True:
        inputs = input("Please choose a number! ")
        option = inputs
        if option == "1":
            create_position(file_position, file_companies)
        elif option == "2":
            read_position(file_position)  
        elif option == "3":
            read_positions(file_position)  
        elif option == "4":
            update_position(file_position)
        elif option == "5":
            state_position(file_position)
        elif option == "6":
            delete_position(file_position)
        elif option == "0":
            return False

def init():
    while True:
        ui.print_program_menu(["Create position", "Show position", "Show all positions", "Update position", "Activate/Deactivate position", "Delete position"])
        try:
            if menu_options_positions() == False:
                break
        except KeyError as err:
            ui.print_message(str(err))

def create_position(filename, filename_2):
    table = file_handling.import_data(filename) #import position table
    table_2 = file_handling.import_data(filename_2) #import company table
    comp_list = []
    for record in table_2:
        comp_list.append(record[0])
    data = ui.user_input("Please give me the position's data", ["Description: ", "Number of seats: "]) # user input
    while True:
        temp_company_id = ui.user_input("", ["Company ID: "])
        if temp_company_id[0] in comp_list:
            break
        ui.print_message("Wrong ID")
    data.append(temp_company_id[0])
    id = misc.generate_random(table)  # generate id
    new_table = misc.append_table(table, misc.build_record(id, data)) # making new table
    file_handling.export_data(new_table, filename, "w") # saving the new table

def delete_position(filename):
    table = file_handling.import_data(filename) #import table
    id = ui.user_input("Please give me the position's ID", ["ID: "]) # user input, ID
    for index in range(len(table)): # deleting an element from the table by index
        if table[index][0] != id[0]:
            del table[index]
            break
    file_handling.export_data(table, filename, "w")

def read_positions(filename):
    table = file_handling.import_data(filename)
    titles = ["ID", "Name", "Age", "Status"]
    ui.print_table(table, titles)

def read_position(filename):
    table = file_handling.import_data(filename) # import table
    id = ui.user_input("Please give me the position's ID",["ID: "]) # user input, ID
    titles = ["ID", "Description", "Number of seats", "Company ID"]
    filtered_table = []
    for record in table:
        if record[0] == id[0]:
            filtered_table.append(record)
            ui.print_table(filtered_table, titles)

def update_position(filename):
    table = file_handling.import_data(filename) #import table
    id = ui.user_input("Please give me the position's ID", ["ID: "]) # user input, ID
    data = ui.user_input("Please give me the position's data", ["Description: "]) # user input, Active?
    new_table = []
    for record in table:
        if record[0] != id[0]:
            new_table.append(record)
        else:
            record[1] = data[0]
            new_table.append(record)
    file_handling.export_data(new_table, filename, "w") # saving the new table