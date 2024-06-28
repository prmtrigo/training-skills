x = list(map(int, input().split()))

vs = x[0]

n = 0

for v in x[1:]:
    if v > 0:
        n = v
        break

total_sum = sum(vs + i for i in range(n))
print(total_sum)
