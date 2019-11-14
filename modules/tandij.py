reszlet = 89222
lst = [2900000,reszlet*18,1450000,1295000,]
lst2 = []
for i in lst:
    lst2.append(round(i * 0.8 * 1.27))

print(lst2)
print(lst2[0]-lst2[1])
print(lst2[1]-lst2[2])
print(lst2[2]-lst2[3])
print(lst2[1]-lst2[3])
print(round((lst2[1]-lst2[3])/18))
print(17554*18)