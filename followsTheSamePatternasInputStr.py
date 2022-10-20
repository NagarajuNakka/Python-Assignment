def same_pattern_asinput(inpu):
    stri="engineers rock"
    EmptList=[]
    for ele in range(-1,-(len(inpu)+1),-1):
        print(inpu[ele])
        for i in range(len(stri)):
            if stri[i]==inpu[ele]:
                EmptList.append(i)
    print(EmptList)
    First_index=EmptList[0]
    for ele in range(2,len(EmptList)):
        if EmptList[ele]<First_index:
            print('TRUE')


        else:
            print('FALSE')
            break

inpu="er"
same_pattern_asinput(inpu)



