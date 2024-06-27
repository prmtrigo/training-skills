x = int(input())
y = int(input())

sum = 0
for i in range(min(x,y), max(x,y)+1):
    if i % 13 != 0:
        sum = sum + i

print(sum)

