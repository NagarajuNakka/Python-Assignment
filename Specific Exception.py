try:
    a=input("enter numerator:")
    b= input("enter denominator:")
    a=int(a)
    b=int(b)
    c=a/b
    print(c)

except (ValueError,TypeError, ZeroDivisionError) as e:
   print(e)