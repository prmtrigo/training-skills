count = 0

for i in range (5):
    x = float(input())
    if x % 2 == 0:
        count += 1

print(count, 'valores pares')