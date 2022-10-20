arr=[0,10,[20,30],40,50,[60,70,80],[90,100,110,120]]
newarr=[]
for ele in arr:
    if type(ele)==int:
        newarr.append(ele)
    elif type(ele)==list:
        for i in ele:
            newarr.append(i)
print(newarr)