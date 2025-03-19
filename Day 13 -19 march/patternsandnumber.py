"""row=int(input("enter rows"))
for i in range(1,row+1):
    for k in range(row-i):
        print(end="  ")
    for j in range(i):
        print("*",end=" ")
    print()  """  

"""row=int(input("enter rows"))
for i in range(row,0,-1):
    for k in range(row-i):
        print(end="  ")
    for j in range(i):
        print("*",end=" ")   
    print()"""
"""
row=int(input("enter rows"))
for i in range(1,row+1):
    for k in range(row-i):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
"""

"""
"""


"""row=int(input("enter rows"))
for i in range(row,0,-1):
    for k in range(row-i):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()"""

#Diamond
"""row=int(input("enter rows"))
for i in range(1,row+1):
    for k in range(row-i):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(row-1,0,-1):
    for k in range(row-i):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
"""

"""row=int(input("enter rows"))
for i in range(1,row+1):
    for k in range(row-i):
        print(end="  ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
"""
"""row=int(input("enter number"))
for i in range(row):
    for j in range(row):
        if i==j:
            print("1",end=" ")
        else:
            print("0",end=" ")    
    print() """   

count=1
for i in range(1,7):
    for j in range(1,6):
        if i%2==0:
            if j%2==0:
                print(count,end=" ")
                count+=1
            else:
                print("*",end=" ")    
        else:
            if j%2==0:
                print("*",end=" ")
                count+=1
            else:
                print(count,end=" ")
                count+=1
    print()               

