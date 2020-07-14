#תוכנה המדפיסה מספר תלת ספרתי בסדר הפוך.
num=int(input("type 3 digits number."))
while (num>999 or num<100):
        num=int(input("type 3 digits number."))
hundreds= int (num/100)
tens=int ((num%100)/10)
units=(num%100)%10
print(units*100+tens*10+hundreds)