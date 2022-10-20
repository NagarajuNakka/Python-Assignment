def cubes(l):
    """this function takes list as arguement and try to convert odd numbers from list as keys and their cubes as their
    values"""
    new_l=[{i:i*i*i} for i in l if i%2==1]
    print(new_l)
l=[1,2,3,4,5,6,7]
cubes(l)



