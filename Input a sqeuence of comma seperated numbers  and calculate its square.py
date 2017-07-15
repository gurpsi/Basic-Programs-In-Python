l=[]
l=input("Enter the string (comma seperated ','): ").split(",")
x=len(l)
print(x)
for j in range(0,x,1):
    print(int(l[j]),':',int(l[j])*int(l[j]))