import os
from time import sleep

def main():
    text = '北京奥运会圆满成功.....'
    while True:
        os.system('clear')
        print(text)
        sleep(0.2)
        text = text[1:] + text[0]

main()
