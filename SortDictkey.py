def sort_dict(test_dict):
    empty=[]
    new_test_dict={}
    for k in test_dict.keys():
        empty.append(k)

    for i in sorted(empty):
        new_test_dict[i]=test_dict[i]
    print(new_test_dict)

test_dict={"c":[3],"b":[12,10],"a":[19,14]}
sort_dict(test_dict)



