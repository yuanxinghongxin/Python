def bubble_sort(items,comp=lambda x,y:x>y):
    items = items[:]  #fu zhi lie biao
    for i in range(len(items)-1):  #range(0,6) 012345
        swapped = True
        for j in range(i,len(items)-1-i):
            if comp(items[j],items[j+1]):
                items[j],items[j+1] = items[j+1],items[j]
                swapped = False
        if swapped:
            break
    return items

a = [1,23,123,52,32,151]
print(bubble_sort(a))
