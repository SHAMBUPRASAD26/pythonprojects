'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
class F15:
    def __init__(jsp,x,y):
        jsp.x=x
        jsp.y=y
        print("jsp is the highest package of the decade",x)
        print("microsoft")
        print("start:",x,"end:",y)
    def lights(jsp,a):
        jsp.a=a
        print("light colour:",a)
    def fan(jsp,b):
        jsp.b=b
        print("fan speed",b)
    def ac(jsp,c,d):
        jsp.c=c
        jsp.d=d
        print("ac temp:",c,"room temp",d)
    def display(jsp):
        diff=jsp.d-jsp.c
        print("diff",diff)
        print("fan",jsp.b)
        print(jsp.x,"start")
        print(jsp.y,"end")
k=F15(12,1)
k.lights("red")
k.fan(120)
k.ac(15,30)
k.display()
        

