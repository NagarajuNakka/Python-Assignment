def flatten_tuple(test_tuple):

    empty_tuple_list=[]
    for i in test_tuple:

        if type(i) is list:
            for j in i:

                empty_tuple_list.append(j)
    print(empty_tuple_list)
test_tuple=([5],[6],[3],[8])
flatten_tuple(test_tuple)

