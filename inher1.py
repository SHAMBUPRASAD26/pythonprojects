'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Faculty:
    def __init__(self,f_name,department,f_id):
        self.f_name=f_name
        self.department=department
        self.f_id=f_id
    def printinfo(self):
        print("faculty information",self.f_name,self.department,self.f_id)
obj=Faculty("Jsp","IT","60")
obj.printinfo()
class cse(Faculty):
    pass
obj=cse("joogindra","cse","23")
obj.printinfo()