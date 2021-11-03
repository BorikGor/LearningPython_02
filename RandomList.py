import random

def ranlst():
    n = int(input("Enter how many numbers:"))
    intlst = []
    for i in range (0, n):
        intlst.append(random.randint(1, 100))
    print(intlst)
    return intlst
