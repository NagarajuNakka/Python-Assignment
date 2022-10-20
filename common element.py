def common_element(arr1,arr2):
    arr1.extend(arr2)
    print(arr1)
    print(set(arr1))
    if len(set(arr1))<len(arr1):
        print('TRUE')
    else:
        print('FALSE')


arr1=[1,2,3,4,5]
arr2=[5,6,7,8,9]
common_element(arr1,arr2)