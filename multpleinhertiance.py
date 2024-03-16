'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class placements:
    def info(self):
        print("We have secured a count of 625 placemnts and still counting")
class department:
    def display(self):
        print("The departments present in college are:cse,IT,Cse-Aiml,Cse-ds,ECE,MECH,CIVIL")
class pragati(placements,department):
    def welcome(self):
        print("Welcome to pragati engineering college we are gald to have onboard")
        self.display()
        self.info()
y=pragati()
y.welcome()


