import math
c=50
h=30
l=[]
l=input("Enter the values in comma separated fprmat: ").split(",")
#l=d.split(",")
x=len(l)
for i in range(0,x,1):
    print(round(math.sqrt((2*c*int(l[i])/h))))