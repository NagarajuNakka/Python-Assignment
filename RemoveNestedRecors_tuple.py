def remove_nested_rec():
    test_tuple=(1,5,7,(4,6),10)
    li=list(test_tuple)
    for i in li:
        if type(i)==tuple:
            li.remove(i)
    print(tuple(li))
remove_nested_rec()