def SumofalltheEle(arr,i,j):
    sum=0
    for iter in range(i,j+1):
        sum=sum+arr[iter]
    print(sum)

arr=[2,4,5,10]
i=1
j=3
SumofalltheEle(arr,i,j)
