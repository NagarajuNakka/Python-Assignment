def fibonacci(Ls):

    re_max = lambda Ls: [(len(Ls[i]),Ls[i] )for i in range(len(Ls)) if Ls[i]==max(Ls)]
    re_min= lambda Ls: [(len(Ls[i]), Ls[i]) for i in range(len(Ls)) if Ls[i] == min(Ls)]
    print("List with maximum lenght:")
    print(re_max(Ls)[0])
    print("List with minimum lenght:")
    print(re_min(Ls)[0])


Ls=[[0],[1,3],[5,7],[9,11],[13,15,17]]

fibonacci(Ls)
# l=[[0],[1,2],[1,2,3,4]]
# print(min(l))