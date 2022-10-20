def tranpose_matrix(l):
    a=l[0]
    b=l[1]
    new_list= [[a[i],b[i]] for i in range(len(a))]
    print(new_list)

l=[[1,2,3,4],[4,5,6,8]]
tranpose_matrix(l)