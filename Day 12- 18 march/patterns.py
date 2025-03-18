"""row=int(input("enter row number"))
for i in range(1,row+1):
    for j in range(i):
        print("*", end="")
    print() """
"""
row=int(input("enter row number"))
for i in range(row,0,-1):
    for j in range(i):
        print("*", end="")
    print()       """


"""row=int(input("enter row number"))
for i in range(1,row+1):
    for j in range(i):
        print(i, end="")
    print()   """    
"""enter row number3
1"""
22
333
"""
row=int(input("enter row number"))
count=0
for i in range(1,row+1):
    for j in range(i):
        count+=1
        print(count, end="")
    print()"""


row=int(input("enter row number"))
for i in range(1,row+1):
    for j in range(i):
        print(j+1, end="")
    print() 


row=int(input("enter row number"))
count=1
for i in range(1,row+1):
    i=count
    for j in range(i):
         print(i, end="")