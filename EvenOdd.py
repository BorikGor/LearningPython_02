from RandomList import ranlst

intlst = ranlst()

i=0
EvenList = []
OddList = []
for i in range (0, intlst.__len__()):
    if(intlst[i]%2):
        OddList.append(intlst[i])
    else:
        EvenList.append(intlst[i])
print(EvenList, "\n", OddList)