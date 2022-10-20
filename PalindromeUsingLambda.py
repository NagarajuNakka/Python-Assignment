def fibonacci(Ls):
    re = lambda Ls: [Ls[i] for i in range(len(Ls)) if Ls[i][::-1]==Ls[i]]
    print(re(Ls))

Ls=['php','w3r','python','abcd','java','aaa']

fibonacci(Ls)