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
    return [id + data]

def build_record(table, id, data):
    for record in table:
        if record[0] != id:
            new_table.append(record)
        else:
            new_table.append([id + data])
    return new_table


    