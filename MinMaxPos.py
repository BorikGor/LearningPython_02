from RandomList import ranlst

intlist = ranlst()
min = intlist[0]
max = intlist[0]
MinPos = 1
MaxPos = 1
print("I'll find the first positions of min and max:")
for i in range (1, intlist.__len__()): # todo: it is better to write len(intlist)
    if intlist[i] >= max:
        max = intlist[i]
        MaxPos = (i+1)
    elif intlist[i] <= min:
        min = intlist[i]
        MinPos = (i+1)
    else:
        print("*Blip*")
print("Min = ", min, "at position", MinPos, "\nMax = ", max, "at position", MaxPos)
