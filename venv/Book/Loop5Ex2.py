#תוכנית שמדפיסה משולש בגודל של המספר שנקלט
num = int(input("הקלד את גודל המשולש."))
j =0
for i in range (0,num):
    for j in range (0,i+1):
        if (j==i):
            print ("*")
        else:
            print("*",end='')