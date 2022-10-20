def elements_ends_with_b(test_list):

    l=[i for i in test_list if i[len(i)-1]=='b' and len(i)>2]
    print(l)

test_list=['ch','dh','eh','cb','tb','td','chb','tdb']
elements_ends_with_b(test_list)