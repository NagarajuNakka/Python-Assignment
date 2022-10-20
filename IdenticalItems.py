def identical_items(arr1,arr2):
    arr1.extend(arr2)
    new_set=set()
    for i in range(len(arr1)):
        count=0
        for j in range(i+1,len(arr1)):
            if arr1[i]==arr1[j]:
                new_set.add(arr1[i])
    print(new_set)

arr1=[10,20,30,40,50]
arr2=[30,40,50,60,70]
identical_items(arr1,arr2)