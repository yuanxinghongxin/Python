"""
右半边三角
"""
#for i in range(1,10):
#    for j in range(1,i+1):
#        print("*",end="")
#    print()

"""
左半边
三角
"""
for i in range(1,10):
    for j in range(1,10):
        if j < 10 - i:
        #if j < 10 - i:
            print(' ', end='')
        else:
            print('*', end='')
    print()

"""
全三角
"""
row = int(input('lai'))
for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
