'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def count(n):
    if(n==0):
        return 0
    return 1+count(n//10)
y=count(133)
print(y)
def sum(n,y):
    if(n==0):
        return 0
    return (n%10)**y+sum(n//10,y)
if(sum(153,y)==153):
    print("armstrong")
else:
    print("not armstrong")
