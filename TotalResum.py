from RandomList import ranlst
intlst = ranlst()
rslt = 0

for i in range (0, intlst.__len__()): #todo: it is not needed to use indexes - items can be used directly
    rslt += intlst[i]
    
"""
result = 0
for item in intlist:
    result += item
print(result)
"""
print("The sum of the above numbers is:", rslt)