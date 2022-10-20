def angram(str):
    str_list=str.split(" ")
    myset=set()
    for i in str_list:
        newi=''.join(sorted(i))
        myset.add(newi)
        mylist=list(myset)
    indexlist=[]
    for i in range(len(mylist)):
        count = 0
        for j in range(i,len(str_list)):
            if len(mylist[i])==len(str_list[j]) and all(ele in str_list[j] for ele in mylist[i]):
                count=count+1

                indexlist.append(count)
    print(max(indexlist))

str="ant magenta magnate tan gnamate"
angram(str)







