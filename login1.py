'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def login():
    us="x"
    pas="y"
    while(us!=pas):
        us=input("enter user:")
        pas=input("enter pas:")
        if(us==pas):
            print("succefull")
            break
        print("login failed")
    return
login()
        
