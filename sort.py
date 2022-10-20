def sort_lower_upper(s):
    s1=''.join(sorted(s))
    str1=''
    str2=''
    for ele in s1:
        if ele.isupper():
            str1=str1+ele
        else:
            str2=str2+ele
    new=""
    if len(str1)<len(str2):
        for i in range(len(str1)):
            new=new+str1[i]+str2[i]

        neww=new+str2[len(str1):]
        print(neww)
    else:
        for i in range(len(str2)):
            new = new + str1[i] + str2[i]
        neww=new+str1[len(str2):]
        print(neww)

s="abbfDDhGFBvdFDGBNDasZVDFjkb"
sort_lower_upper(s)
