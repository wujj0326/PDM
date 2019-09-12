x=[*range(11)]
print(x)
print(x[:3])
print(x[3:])
print(x[::3]) #from 0-9 jumping from every three
print(x[5:2:-1]) #from 5-2 jump every -1
print(1 in x)
#x.extend([4,5,6]) #extend 4,5,6 to orginal x list (x list would be changed)
print(x+[4,5,6])
x.append([4,5,6]) #adding another item to the list
print(x)
len(x) #the length of the list
z,y=[1,2]
print(y)