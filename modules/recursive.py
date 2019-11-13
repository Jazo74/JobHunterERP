lst = ["a","e",["u","o",["q"]],"i"]

def rec_walk(list):
    new_list = []
    for i in list:
        if len(i) == 1:
            new_list.append(i[0])
        else:
            new_list.append(rec_walk(i))
    return new_list

print(rec_walk(lst))

lst2 = [5,6,7,8,9]
for i in reversed(lst2):
    print(i,end="")
print()
for i in range(len(lst2)-1,-1,-1):
    print(lst2[i], end="")
print()
for i in lst2[len(lst2)::-1]:
    print(i,end="")