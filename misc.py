def generate_random(table):
    generated = ''
    while True:
        letters = "abcdefghijklmnopqrstvuxywz"
        capitals = "ABCDEFGHIJKLMNOPQRSTVUXYWZ"
        symbols = "#&@$ß%đĐŁ€"
        for i in range(2):
            generated += letters[random.randint(0, 25)]
        for i in range(2):
            generated += str(random.randint(0,9))
        for i in range(2):
            generated += capitals[random.randint(0, 25)]
        for i in range(2):
            generated += symbols[random.randint(0,9)]
        if generated not in table:
            return generated