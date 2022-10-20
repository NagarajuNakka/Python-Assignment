def SecondMost(arr):
    count = 0
    count1=0
    count2 = 0
    count3 = 0
    l={}
    for i in  arr:
        if i=="aaa":
            count1=count1+1
            #print("aaa",count1)
            l["aaa"]=count1
            #print(l)

        elif i=="bbb":
            count2 = count2 + 1
            #print("bbb",count2)
            l["bbb"] = count2
            #print(l)

        elif i == "ccc":
            count3 = count3 + 1
            #print("ccc",count3)
            l["ccc"] = count3
    value = sorted(l.values(), reverse=True)
    SecondMost=value[1]
    for key, val in l.items():
        if val == SecondMost:
            return key


    return value


arr=["aaa","bbb","ccc","bbb","aaa","aaa"]
result=SecondMost(arr)
print(result)

