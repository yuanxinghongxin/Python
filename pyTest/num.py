lst = [1,1,3,4,4,5,1]
lst2 = []
x = len(lst)
for i in range(x):
    if i == 0:
        lst2.append(lst[i])
    else:
        if lst[i-1] != lst[i]:
            lst2.append(lst[i])
print(lst2)
