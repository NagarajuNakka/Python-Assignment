import numpy as np
def triplet_arr(arr,sum):
    while True:
        new_list = np.random.choice(arr,3)
        count=0
        new_arr=set(new_list)
        if len(new_arr)==3:
            for ele in new_arr:
                count=count+ele
            if count==sum:
                for i in new_arr:
                    print(i)
                break

arr=[12,3,4,1,6,9]
arr1=[1,2,3,4,5]
sum=9
triplet_arr(arr1,sum)

