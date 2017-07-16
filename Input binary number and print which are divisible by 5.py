binary=[]
#out_list=[]
binary=(x for x in input("Enter the binary numbers seperated by commas").split(","))
for i in binary:
    if int(i,2)%5==0:
        print(i)