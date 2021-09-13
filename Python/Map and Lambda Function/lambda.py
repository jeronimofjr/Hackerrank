cube = lambda x: x*x*x

def fib(n):
    return fib(n-1) + fib(n-2) if n > 2 else n-1

def fibonacci(n):
    return [fib(i) for i in range(1, n+1)]
