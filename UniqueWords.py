def unique_words():
    a="red,white,black,red,green,black"
    l=a.split(',')
    convert_set = set(l)
    new_list=list( convert_set)
    new_list.sort()
    print(new_list)

unique_words()