def Removealltheduplicates(sen):
    li=sen.split(" ")
    print(len(li))

    for i in range(len(li)):
        count=0
        for j in range(i+1,len(li)-1):
            if li[i]==li[j]:
                count=count+1
                count==2
                print("===",li[i])
                li.remove(li[i])
    print(" ".join(li))

sen="Python is great and java is also great"
Removealltheduplicates(sen)