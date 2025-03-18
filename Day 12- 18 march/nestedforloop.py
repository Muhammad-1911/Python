"""for i in range(5):
    print("*")
"""
"""for i in range(5):
    print("*",end="")
"""
"""for i in range(5):
    print("*"*3)"""

"""row=int(input("enter number for row"))
column=int(input("enter number for column"))
for i in range(row):
    for j in range(column):
        print("*",end="")
    print()    """


"""row=int(input("enter number for row"))
column=int(input("enter number for column"))
for i in range(1,row+1):
    for j in range(1,column+1):
        print(i,end="")
       
    print()  """  


"""
row=int(input("enter number for row"))
column=int(input("enter number for column"))
for i in range(1,row+1):
    for j in range(1,column+1):
        print(j,end="")
       
    print() """ 

"""
row=int(input("enter number for row"))
column=int(input("enter number for column"))
count=0
for i in range(1,row+1):
    for j in range(1,column+1):
        count+=1
        print(count,end="")
       
    print() """



row=int(input("enter number for row"))
column=int(input("enter number for column"))
for i in range(1,row+1):
    for j in range(1,column+1):   
        print(i*j,end=" ") 
    print() 