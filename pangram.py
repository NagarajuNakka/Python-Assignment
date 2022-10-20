def pangram(sen):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for ele in alphabets:
        if ele not in sen:
            print(ele)

sen="welcome to geeks for geeks"
pangram(sen)
