from RandomList import ranlst

intlst = ranlst()

i=0
EvenList = []
OddList = []
for i in range (0, intlst.__len__()): # todo: use items directly. see code below
    if(intlst[i]%2):
        OddList.append(intlst[i])
    else:
        EvenList.append(intlst[i])
        
print(EvenList, "\n", OddList)

even_list = list()
odd_list = list()

for item in intlst:
    if item%2: odd_list.append(item)
    else: even_list.append(item)