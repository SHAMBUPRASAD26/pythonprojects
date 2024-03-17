import csv
f=open("jsp.csv","a",newline="")
a=csv.writer(f)
a.writerow(["studentid","roll","phn"])
x=int(input("enter id:"))
y=int(input("enter roll:"))
z=int(input("enter phn:"))
a.writerow([x,y,z])