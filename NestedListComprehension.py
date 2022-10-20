
"""this nested list comprehension return the numbers from 1-1000 which are divisible by numbers from
2-9"""
l=[i for i in range(1,1000) for j in range(2,9) if i%j==0]
print(list(set(l)))