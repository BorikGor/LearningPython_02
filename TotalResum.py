from RandomList import ranlst
intlst = ranlst()
rslt = 0

for i in range (0, intlst.__len__()):
    rslt += intlst[i]
print("The sum of the above numbers is:", rslt)