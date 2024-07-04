T = int(input())

fib = [0]*61
fib[0] = 0
fib[1] = 1

for i in range(2, 61):
    fib[i] = fib[i-1] + fib[i-2]

for _ in range(T):
    n = int(input())
    print("Fib({}) = {}".format(n, fib[n]))