def import_data(filename):
    
    with open(filename, "r") as file:
        lines = file.readlines()
    table = []
    for word in lines:
        table.append(word.replace("\n","").split(";"))
    return table
        
def export_data(table, filename, mode='a'):
    with open(filename, mode) as file:
        if mode != "a" and mode != "w":
            raise ValueError("Wrong file opening mode")
        else:
            for word in table:
                file.write(";".join(word) + "\n")
