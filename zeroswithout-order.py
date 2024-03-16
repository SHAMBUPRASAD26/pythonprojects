'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
x=[2,0,1024,0,40,230,0]
y=[]
z=0
for i in x:
    if(i==0):
        z=z+1
    else:
        y=y+[i]
for j in range(z):
    y=y+[0]
print(y)
        