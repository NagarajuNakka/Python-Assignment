def remove_nested_rec(test_list):
    len_test_list=[]
    final_list=[]
    for i in range(len(test_list)):
        length_value=len(test_list[i])
        len_test_list.append(length_value)
    len_test_list.sort()
    for j in range(len(len_test_list)):
        for n in range(len(test_list)):
            if len(test_list[n])==len_test_list[j]:
                final_list.append(test_list[n])
    print(final_list)
test_list=[(3,4,6,723),(1,2),(134,234,34)]
remove_nested_rec(test_list)