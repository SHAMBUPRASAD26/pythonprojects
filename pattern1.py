'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

for i in range(1,4):
    for s in range(1,4-i+1):
        print(" ",end=" ")
    for j in range(0,1):
        print("X",end=" ")
    for s1 in range(1,i):
        print(" ",end=" ")
    for j1 in range(1,i):
        if(i==3 and j1==1):
            print(" ",end=" ")
            continue
        print("X",end=" ")
    print()
for x in range(1,8):
    print("X",end=" ")
print()