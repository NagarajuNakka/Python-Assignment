def fibonacci(fib_up_to):


    fibo = lambda n: [ab.append(sum(ab)) or ab.pop(0)
                      for ab in [[0,1]] for _ in range(n)]
    print(fibo(fib_up_to))

fib_up_to=5
fibonacci(fib_up_to)