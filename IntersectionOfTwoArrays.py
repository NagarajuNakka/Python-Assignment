def fibonacci(a,b):
    re = lambda a, b: [a[i] for i in range(len(a)) if a[i] in b]
    print(re(a,b))
a=[1,2,4,3,5,7,8,9,10]
b=[1,2,4,8,9]

fibonacci(a,b)