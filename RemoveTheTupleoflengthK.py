def remove_tuple(tu,k):
    for i in tu:
        if len(i)==2:
            tu.remove(i)
    print(tu)
tu=[(4,5),(4,),(8,6,7),(1,),(3,4,6,7)]
k=2
remove_tuple(tu,k)