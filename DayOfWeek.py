

m = float(input("Enter the month"))
d = float(input("Enter the day"))
y = float(input("Enter the year"))


y0 = y - (14 - m) // 12
x = y0 + y0//4 - y0//100+ y0//400
m0 = m + 12 * ((14 - m) // 12) - 2
d0= (d + x + (31*m0)//12) % 7


print ("The day of the week is:", d0)
