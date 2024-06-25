n = int(input())
fibonacci = [0, 1]
while len(fibonacci) < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

for i in range(n):
    if i == n - 1:
        print(fibonacci[i])
    else:
        print(fibonacci[i], end=" ")