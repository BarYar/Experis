day= int (input ("type the day"))
while day < 0 or day>31:
    day = int(input("type the  correct day"))
month= int(input("type the month"))
while month < 0 or month >12:
    month = int(input("type the correct month"))
year= int(input("type the year"))
while year>2020 :
   year=int (input("type the year"))
print (day,"/",month,"/",year)
