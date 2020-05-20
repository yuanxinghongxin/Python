lst = [1,1]
a = 20
while a > 2:
    num = int(len(lst))
    yi = num - 1
    er = num - 2
    mo = lst[yi] + lst[er]
    lst.append(mo)
    a -= 1
print(lst)
print(len(lst))
