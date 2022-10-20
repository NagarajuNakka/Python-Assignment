def max_min(s):
    new_set=set(s)
    print("set:",new_set)
    new_set_list=list(new_set)
    print(new_set_list)
    min=new_set_list[0]
    print("min is ",min)
    max=new_set_list[len(new_set_list)-1]
    print("max is ",max)
#s=[10,12,10,9,4,13]
s=[8,16,24,1,25,3,10,6555,8]
max_min(s)
