'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class showroom:
    def __init__(self):
        x=input("please enter the company name from the following:1.Toyota,2.Mahindra,3.Mercendeez:")
        while(x!="Toyota" and x!="Mahindra" and x!="Mercendeez" and x!="1" and x!="2" and x!="3"):
            print("please select within the companies")
            x=input("please enter the company name from the following:1.Toyota,2.Mahindra,3.Mercendeez:")
        self.x=x
        
    def modelname(self):
        if(self.x=="Toyota" or self.x=="1"):
            print("Welcome to Toyota Company!")
            y=input("enter the model name from the following:1.Urban,2.Innova,3.Rumion:")
            while(y!="Urban" and y!="Innova" and y!="Rumion" and y!="1" and y!="2" and y!="3"):
                print("enter within model names:")
                y=input("enter the model name from the following:1.Urban,2.Innova,3.Rumion:")
        if(self.x=="Mahindra" or self.x=="2"):
            print("Welcome to Mahindra Company!")
            y=input("enter the model name from the following:1.suv,2.xuv,3.scoripio:")
            while(y!="suv" and y!="xuv" and y!="scoripio" and y!="1" and y!="2" and y!="3"):
                print("enter within model names:")
                y=input("enter the model name from the following:1.suv,2.xuv,3.scoripio:")
        if(self.x=="Mercendeez" or self.x=="3"):
            print("Welcome to Mercendeez Company!")
            y=input("enter the model name from the following:1.XM,2.X3,3.X7:")
            while(y!="XM" and y!="X3" and y!="X7" and y!="1" and y!="2" and y!="3"):
                print("enter within model names:")
                y=input("enter the model name from the following:1.XM,2.X3,3.X7:")
        self.y=y
    def varian(self):
        z=input("choose the varaint from 1.Petrol and 2.Disel:")
        while(z!="Petrol" and z!="Disel" and z!="1" and z!="2"):
            print("invalid enter again please within options")
            z=input("choose the varaint from 1.Petrol and 2.Disel:")
        self.z=z
    def display(self):
        obp=0
        xsr=0
        if(self.x=="Toyota" or self.x=="1"):
            self.x="Toyota"
            if((self.y=="Urban" or self.y=="1") and (self.z=="Petrol" or self.z=="1")):
                xsr=1300000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="Urban"
                self.z="Petrol"
            elif((self.y=="Urban" or self.y=="1") and (self.z=="Disel" or self.z=="2")):
                xsr=1200000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="Urban"
                self.z="Disel"
            elif((self.y=="Innova" or self.y=="2") and (self.z=="Petrol" or self.z=="1")):
                xsr=1000000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="Innova"
                self.z="Petrol"
            elif((self.y=="Innova" or self.y=="2") and (self.z=="Disel" or self.z=="2")):
                xsr=900000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="Innova"
                self.z="Disel"
            elif((self.y=="Rumion" or self.y=="3") and (self.z=="Petrol" or self.z=="1")):
                xsr=1400000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="Innova"
                self.z="Petrol"
            elif( (self.y=="Rumion" or self.y=="3") and (self.z=="Disel" or self.z=="2")):
                xsr=1300000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="Rumion"
                self.z="Disel"
        if(self.x=="Mahindra" or self.x=="2"):
            self.x="Mahindra"
            if((self.y=="suv" or self.y=="1") and (self.z=="Petrol" or self.z=="1")):
                xsr=1100000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="suv"
                self.z="Petrol"
            elif((self.y=="suv" or self.y=="1") and (self.z=="Disel" or self.z=="2")):
                xsr=900000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="suv"
                self.z="Disel"
            elif((self.y=="xuv" or self.y=="2") and (self.z=="Petrol" or self.z=="1")):
                xsr=1600000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="xuv"
                self.z="Petrol"
            elif((self.y=="xuv" or self.y=="2") and (self.z=="Disel" or self.z=="2")):
                xsr=1500000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="xuv"
                self.z="Disel"
            elif((self.y=="scoripio" or self.y=="3") and (self.z=="Petrol" or self.z=="1")):
                xsr=2000000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="scoripio"
                self.z="Petrol"
            elif((self.y=="scoripio" or self.y=="3") and (self.z=="Disel" or self.z=="2")):
                xsr=1900000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="scoripio"
                self.z="Disel"
        if(self.x=="Mercendeez" or self.x=="3"):
            self.x="Mercendeez"
            if((self.y=="XM" or self.y=="1") and (self.z=="Petrol" or self.z=="1")):
                xsr=2100000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="XM"
                self.z="Petrol"
            elif((self.y=="XM" or self.y=="1") and (self.z=="Disel" or self.z=="2")):
                xsr=2000000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="XM"
                self.z="Disel"
            elif((self.y=="X3" or self.y=="2") and (self.z=="Petrol" or self.z=="1")):
                xsr=1800000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="X3"
                self.z="Petrol"
            elif((self.y=="X3" or self.y=="2") and (self.z=="Disel" or self.z=="2")):
                xsr=1700000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="X3"
                self.z="Disel"
            elif((self.y=="X7" or self.y=="3") and (self.z=="Petrol" or self.z=="1")):
                xsr=2200000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="X7"
                self.z="Petrol"
            elif((self.y=="X7" or self.y=="3") and (self.z=="Disel" or self.z=="2")):
                xsr=2100000
                obp=xsr+(8*xsr)//100+(10*xsr)//100+10000
                self.y="X7"
                self.z="Disel"
        print("exshowroom price for",self.x,"company for",self.y,"model in",self.z,"variant is",xsr)
        print("Onboard price for",self.x,"Company for",self.y,"model in",self.z,"varaint is",obp)

x=showroom()
x.modelname()
x.varian()
x.display()
            
             
            
            
        
        
            
    
        

