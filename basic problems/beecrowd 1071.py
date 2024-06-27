x = int(input())
y = int(input())

start = min(x,y)+1
end = max(x,y)

if start % 2 == 0:
    start += 1

sum = 0
for i in range (start, end, 2):
    sum += i
print(sum)

