import random

def generate_random(table):
    generated = ''
    while True:
        letters = "abcdefghijklmnopqrstvuxywz"
        capitals = "ABCDEFGHIJKLMNOPQRSTVUXYWZ"
        symbols = "#&@$ß%đĐŁ€"
        for count in range(2):
            generated += letters[random.randint(0, 25)]
        for count in range(2):
            generated += str(random.randint(0,9))
        for count in range(2):
            generated += capitals[random.randint(0, 25)]
        for count in range(2):
            generated += symbols[random.randint(0,9)]
        if generated not in table:
            return generated

def build_record(id, data):
    new_list = []
    new_list.append(id)
    for elem in data:
        new_list.append(elem)
    return new_list

def update_table(table, id, data):
    new_table = []
    for record in table:
        if record[0] != id:
            new_table.append(record)
        else:
            new_table.append(data)
    return new_table

def append_table(table, record):
    table.append(record)
    return table



    