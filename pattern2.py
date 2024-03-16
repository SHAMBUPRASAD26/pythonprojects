'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
for i in range(1,5):
    for s in range(1,4-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("x",end=" ")
    print()
for i in range(1,4):
     for s in range(1,i+1):
         print(" ",end=" ")
     for j in range(1,2*(4-i)):
         print("x",end=" ")
     print()