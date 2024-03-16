'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

x=[12,42,23,96,7,18,10,133]
y=0
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if(x[i]>x[j]):
            temp=x[i]
            x[i]=x[j]
            x[j]=temp
print(x[0])
max1=x[-1]
min1=x[0]
x[-1]=max1+min1
x[0]=max1-min1
print(x)