def subset(is_subset,of):
    li=list(is_subset)
    new_list=[]
    for i in li:
        if i in of:
            re='true'
        else:
            re='false'
        new_list.append(re)
    print(new_list)
    if any(ele =='false' for ele in new_list):
        for i in range(len(of)):
            print('false')
    else:
        for i in range(len(of)):
            print('true')

x={'mango','apple'}
of={'mango','orange'}
is_subset={'mango'}
subset(is_subset,of)