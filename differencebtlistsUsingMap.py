x=[6,5,3,9]
y=[0,1,7,7]
re=list(map((lambda x,y:(x+y,x-y)),x,y))
print(re)