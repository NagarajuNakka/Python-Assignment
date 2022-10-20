def identical_items(s1,s2):
    arr1=list(s1)
    arr2=list(s2)


    new_set=set()
    for i in range(len(arr1)):

        if arr1[i] not in arr2:
            new_set.add(arr1[i])
    print(new_set)


s1={1,2,3,4,5}
s2={4,5,6,7,8}
identical_items(s1,s2)