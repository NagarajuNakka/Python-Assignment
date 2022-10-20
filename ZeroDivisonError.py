def divide_two_numbers():
    try:
        a = input("Enter an integer: ")
        b = input("Enter another integer: ")
        if b=='0':
            raise Exception("The numbe shouldn't be a zero")
        c = int(a)/int(b)
    except Exception as e:
        print(e)
divide_two_numbers()