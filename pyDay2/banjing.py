"""
输入半径求圆的周长和面积
"""

r = int(input("请输入半径:"))
pai = 3.14
mianji = pai * (r * r)
zhouchang = 2 * pai * r
print("周长为{}".format(zhouchang))
print("面积为{}".format(mianji))
