print("Please enter a number to show you numbers less than twelve.")
A =int(input("enter your number 1 :"))
B =int(input("enter your number 2 :"))
C =int(input("enter your number 3 :"))
D =int(input("enter your number 4 :"))
E =int(input("enter your number 5 :"))
F =int(input("enter your number 6 :"))
G =int(input("enter your number 7 :"))
print([A,B,C,D,E,F,G])
score = [A,B,C,D,E,F,G]

def sco(a):
    if a < 12 :
        return True
    else:
        return False


val = list(filter(sco,score))
print(val)