def RotateArray(arr,d):
    newarr=[]
    for i in range(d):
        newarr.append(arr[i])
        arr.append(arr[i])
    for i,v in enumerate(newarr):
        if v in arr:
            arr.remove(v)

    print(arr)
arr=[3,4,5,6,7,1,2]
d=2
RotateArray(arr,d)