num = int(input("enter decimal: "))
binary = []
while num!=0:
    y= num %2
    binary.append(y)
    num=num//2
binary.reverse()
x=[]
for i in binary:
    i=str(i)
    x.append(i)
z="".join(x)
print ("the binary is: "+str(z))    
