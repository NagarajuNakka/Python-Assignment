def CountTheNoofChar(sen):
    dicts={}
    for i in sen:
        count=0
        for j in sen:
            if i==j:
                count=count+1
        dicts[i] = count
    emptylist=[]
    for key,val in dicts.items():
        if val%2==1:
            emptylist.append(key)
    print(emptylist)


sen="geekforgeeks is best for geeks"
CountTheNoofChar(sen)