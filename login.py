'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
 
def login():
    z=1
    while(z):
        user=input("enter user name:")
        passw=input("enter password:")
        if(user==passw):
            z=0
            print("successfull")
            break
        print("login failed")
    return 
login()
        