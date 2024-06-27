x = int(input())

sum_in = 0
sum_out = 0

for i in range (x):
    n =  int(input())
    if (0 <= n <= 20):
        sum_in += 1
    else:
        sum_out += 1

print(sum_in, 'in')
print(sum_out, 'out')