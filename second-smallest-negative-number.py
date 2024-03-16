'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

x=[22,-1,42,65,1,-4,6]
min1=0
min2=0
for i in x:
    if(min1>i):
        min2=min1
        min1=i
    elif(min2>i and min2>min1):
        min2=i
print(min2)


