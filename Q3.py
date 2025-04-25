from datetime import date

d1 = int(input("Enter day of first date: "))
m1 = int(input("Enter month of first date: "))
y1 = int(input("Enter year of first date: "))

d2 = int(input("Enter day of second date: "))
m2 = int(input("Enter month of second date: "))
y2 = int(input("Enter year of second date: "))

date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

days_diff = abs((date2 - date1).days)

print("Number of days between two dates:", days_diff)
