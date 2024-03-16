'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
from abc import ABC,abstractmethod
class ticket(ABC):
    @abstractmethod
    def bookticket(self):
        pass
class makemytrip(ticket):
    def bookticket(self):
        a=input("enter your name:")
        b=int(input("enter your phone no:"))
        c=input("enter your emailid:")
        d=input("enter journey date:")
        print("Thank you for choosing makemytrip")
class irctc(ticket):
    def bookticket(self):
        a=input("enter your name:")
        b=int(input("enter your phone no:"))
        c=input("enter your emailid:")
        d=input("enter journey date:")
        e=input("enter whether is 1.one way or 2.round trip")
        if(e in ["round trip","2"]):
            f=input("enter your return date")
        print("Thank you for choosing irctc")
class indigo(ticket):
    def bookticket(self):
        a=input("enter your name:")
        b=int(input("enter your phone no:"))
        c=input("enter your emailid:")
        d=input("enter journey date:")
        e=input("enter whether is 1.one way or 2.round trip")
        x=input("which mode transport from the following bus,train,flight")
        print("Thank yopu for chossing indigo")
x1=makemytrip()
x2=irctc()
x3=indigo()
x1.bookticket()
x2.bookticket()
x3.bookticket()

        
            
        
