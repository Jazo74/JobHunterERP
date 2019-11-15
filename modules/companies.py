from modules import misc
from modules import ui
from modules import file_handling

def menu_options_companys():
    file_company = "databases/companies.csv"
    file_positions = "databases/positions.csv"
    while True:
        inputs = input("Please choose a number! ")
        option = inputs
        if option == "1":
            create_company(file_company)
        elif option == "2":
            read_company(file_company, file_positions)  
        elif option == "3":
            read_companies(file_company)  
        elif option == "4":
            update_company(file_company)
        elif option == "5":
            delete_company(file_company)
        elif option == "0":
            return False

def init():
    while True:
        ui.print_program_menu(["Create company", "Show company", "Show all companies", "Update company", "Delete company"])
        try:
            if menu_options_companys() == False:
                break
        except KeyError as err:
            ui.print_message(str(err))           

def create_company(filename):
    table = file_handling.import_data(filename) #import table
    data = ui.user_input("Please give me the datas of the company", ["Name: "]) # user input
    id = misc.generate_random(table)  # generate id
    new_table = misc.append_table(table, misc.build_record(id, data)) # making new table
    file_handling.export_data(new_table, filename, "w") # saving the new table

def update_company(filename):
    table = file_handling.import_data(filename) #import table
    id = ui.user_input("Please give me the ID of the company", ["ID: "]) # user input, ID
    data = ui.user_input("Please give me the datas of the company", ["Name: "]) # user input, rest info
    new_table = misc.update_table(table, id[0], misc.build_record(id[0], data)) # updating the table
    file_handling.export_data(new_table, filename, "w") # saving the new table

def delete_company(filename, pos_table):
    table = file_handling.import_data(filename) #import table
    pos_table = file_handling.import_data(pos_file) # import positions table
    id = ui.user_input("Please give me the ID of the company", ["ID: "]) # user input, ID
    for index in range(len(table)): # deleting an element from the table by index
        if table[index][0] == id[0]:
            del table[index]
            break
    file_handling.export_data(table, filename, "w")

def read_companies(filename):
    table = file_handling.import_data(filename)
    titles = ["ID", "Name"]
    ui.print_table(table, titles)

def read_company(filename, pos_file):
    table = file_handling.import_data(filename) # import table
    pos_table = file_handling.import_data(pos_file) # import positions table
    id = ui.user_input("Please give me the ID of the company",["ID: "]) # user input, ID
    titles = ["ID", "Name"]
    titles_2 = ["Positions ID", "Description", "Seats", "Company ID"]
    filtered_table = []
    pos_filtered_table = []
    for record in table:
        if record[0] == id[0]:
            filtered_table.append(record)
            ui.print_table(filtered_table, titles)
    for record in pos_table:
        if record[3] == filtered_table[0][0]:
            pos_filtered_table.append(record)
    if len(pos_filtered_table) != 0:
        ui.print_table(pos_filtered_table, titles_2)