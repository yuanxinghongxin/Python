prices = {'aaa':123,'sdr':396,'qwe':96,'zxce':'22'}

prices2 = {key:value for key,value in prices.items() if int(value) > 100}
print(prices2)
