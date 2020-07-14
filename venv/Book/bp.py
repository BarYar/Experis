#guess
import tkinter as tk
class Guess:


    def __init__(self, g,num):

        self.g=g
        self.num=num
        self.b=0
        self.p=0
        self.l=[]
    #פונקציה הבודקת אם המספר בעל 4 ספרות
    def CorNum(self):
        while((self.g<1000)or(self.g>9999)):
          self.g = int(input("The Guess has to be 4 digits,type it again."))
    #פונקציה המוציאה את הספרות של הניחוש והמספר
    def Digits (self):
        Tg=int(self.g/1000)
        Hg=int ((self.g%1000)/100)
        Teg=int (((self.g%1000)%100)/10)
        Ug = int(((self.g % 1000) % 100) % 10)
        Tn = int(self.num / 1000)
        Hn = int((self.num % 1000) / 100)
        Ten = int(((self.num % 1000) % 100) / 10)
        Un = int(((self.num % 1000) % 100) % 10)
        self.l = [Tg, Hg, Teg, Ug, Tn, Hn, Ten, Un]
     #תשובה: פונקציה המחזירה בול ופגיעה
    def BPS(self):
      return ("bool:",self.p,"pgiaa",self.b)
      #  פונקציה המחזירה בול
    def RB(self):
         return (self.b)
     #  פונקציה המחזירה פגיעה
    def RP(self):
        return (self.p)
    #פונקציה המגדירה את הפגיעות
    def SP(self,n):
        self.p=n
     #פונקציה המגדירה את הבולים
    def SB(self, n):
        self.b = n
    #פונקציה המעדכנת את הניחוש
    def UG(self,g1):
        self.g=g1
     #פונקציה הבודקת אם בולים ופגיעות
    def B (self):
        Tg = self.l[0]
        Hg = self.l[1]
        Teg = self.l[2]
        Ug = self.l[3]
        Tn = self.l[4]
        Hn = self.l[5]
        Ten = self.l[6]
        Un = self.l[7]
        T=False
        H=False
        Te=False
        U=False
        C=False
        if(Tn==Tg):
            self.p = self.p + 1
            T=True
            C=True
        if (Tn == Hg):
            if(C==False):
                self.b = self.b+ 1
                H = True
                C=True
        if (Tn == Teg):
            if (C == False):
                self.b = self.b + 1
                Te = True
                C = True
        if (Tn == Ug):
            if (C == False):
                self.b = self.b + 1
                U = True
                C = True
        C=False
        if (Hn == Tg):
            if (C == False):
                if(T==False):
                    self.b = self.b + 1
                    C = True
            T=True
        if (Hn == Hg):
            if (C == False):
                if (H == False):
                    self.p = self.p + 1
                    H = True
            C = True
        if (Hn == Teg):
            if (C == False):
                if (Te == False):
                  self.b = self.b + 1
                  C=True
            Te = True
        if (Hn == Ug):
            if (C == False):
                if (U == False):
                    self.b = self.b + 1
                    C = True
        C = False
        if (Ten == Tg):
            if (C == False):
                if (T == False):
                    self.b = self.b + 1
                    C = True
            T = True
        if (Ten == Hg):
            if (C == False):
                if (H == False):
                    self.b = self.b + 1
                    C = True
            H = True
        if (Ten == Teg):
            if (C == False):
                if (Te == False):
                    self.p = self.p + 1
                    C = True
            Te = True
        if (Ten == Ug):
            if (C == False):
                if (U == False):
                    self.b = self.b + 1
                    C = True
            U = True
        C = False
        if (Un == Tg):
            if (C == False):
                if (T == False):
                     self.b = self.b + 1
                     C = True
            T = True
        if (Un == Hg):
            if (C == False):
                if (H == False):
                    self.b = self.b + 1
                    C = True
            H = True
        if (Un == Teg):
            if (C == False):
                if (Te == False):
                      self.b = self.b + 1
                      C = True
            Te = True
        if (Un == Ug):
            if (C == False):
                if (U == False):
                    self.p = self.p + 1
                    C = True
            U = True



#מספר רנדומלי 4 ספרות
def Ran():
    num=int(random.random()*10000)
    while ((num<1000)or(num>9999)):
     num = int(random.random() * 10000)

    return num



#main
import random
num=Ran()
guess= int(input("Type your  guess."))
G=Guess(guess, num)
#בודק אם המספר תקין
G.CorNum()
G.Digits()
G.B()
p=int(G.RP())
print(G.BPS())
G.SB(0)
G.SP(0)
while (p < 4):
    G.CorNum()
    guess = int(input("Type your  guess."))
    G.UG(guess)
    G.Digits()
    G.B()
    print(G.BPS())
    p = G.RP()
    G.SB(0)
    G.SP(0)
print("Congratulations the number was",num)



