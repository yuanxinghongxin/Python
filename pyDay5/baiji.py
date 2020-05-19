
lst = []
for x in range(1,21):
    for y in range(1,101):
        for z in range(1,101):
            he = "{} {} {}".format(x,y,z)
            if 5 * int(x) + 3 * int(y) + int(z) / 3 == 100 and int(x + y + z) == 100:
                print(he)
#                lst.append(he)
#print(len(lst))
