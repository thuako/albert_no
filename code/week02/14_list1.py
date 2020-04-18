mylist = [2, 3, 5]

print(mylist)
print(mylist[0])
print(mylist[2])
print(mylist[0:2])

mylist.append(7)
print(mylist)
mylist2 = [11, 13, 17]
mylist = mylist + mylist2
print(mylist)

print(mylist[4:])
print(mylist[-1])

mylist = mylist + [19]
print(mylist)

a = 5
if a in mylist:
    print("yes, a is in mylist")
else:
    print("yes, a is not in mylist")
