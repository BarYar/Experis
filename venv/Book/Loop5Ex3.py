num = int(input("הקלד את גודל המשולש."))
print ("hey")
for i in range (0,num):
    for j in range (0, num):
        if i > j:
            print(" ", end='')
        elif j==num-1:
            print("*")
        else:
            print ("*",end='')

