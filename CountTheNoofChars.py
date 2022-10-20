def CountTheNoofChar(sen):
    dicts={}
    for i in sen:
        count=0
        for j in sen:
            if i==j:
                count=count+1
        dicts[i] = count
    print(dicts)
sen="google.com"
CountTheNoofChar(sen)



