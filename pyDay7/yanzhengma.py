import random
import time
all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def main():
    a = 1
    while a <= 4:
        x = int(random.randint(1,len(all_chars)))
        print(all_chars[x],end='')
        a += 1

main()
