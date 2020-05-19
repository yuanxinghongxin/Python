#x = 1
#y = 5
#z = 3
#he = "{}{}{}".format(x,y,z)
for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            he = "{}{}{}".format(x,y,z)
            if (int(x) ** 3) + (int(y) ** 3) + (int(z) ** 3) == int(he):
                print(he)
