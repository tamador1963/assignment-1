L=["Network" , "Math" , "Programming", "Physics" , "Music"]
l = [len(i) for i in L]
x=max(l)
x_i=l.index(x)
print ("longest item: "+str(L[x_i]))


