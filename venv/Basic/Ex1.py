#תוכנה המקבלת יום חוד ושנה ומדפיסה אותו כתאריך
day= int (input ("type the day"))
#לא מקבל יום עד שהוא תקין.
while day < 0 or day>31:
    day = int(input("type the  correct day"))
month= int(input("type the month"))
#לא מקבל חודש עד שהוא תקין.
while month < 1 or month >12:
    month = int(input("type the correct month"))
year= int(input("type the year"))
#לא מקבל שנה עד שהיא תקינה.
while year>2020 :
   year=int (input("type the correct year"))
print (day,"/",month,"/",year)
