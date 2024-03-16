'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)
x=fact(5)
print(x)

def fib(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    return fib(n-1)+fib(n-2)
y=fib(5)
print(y)