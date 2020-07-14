import random
from b
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