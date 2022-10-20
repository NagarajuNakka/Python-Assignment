def CountTheNoofChar(sen):
    dicts={}
    for i in sen:
        count=0
        for j in sen:
            if i==j or i==j.upper() or i==j.lower():
                count=count+1
        dicts[i] = count
    emptystr=''
    for key,val in dicts.items():
        if val==1:
            emptystr = emptystr+key
    newstr="".join(sorted(emptystr))
    print(newstr[0])
sen="iNeuron.com"
CountTheNoofChar(sen)