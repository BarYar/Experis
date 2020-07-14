#תוכנה המדפיסה את הגיל של הבן אדם בשנה העתידית שהבן אדם מקבל.
name=input("type your name.")
Tyear=int(input("type this year."))
age=int(input("type your age."))
Fyear=int(input("type a year in the future."))
dif=Fyear-Tyear
age=age+dif
print(name,"will be",age,"in",Fyear)