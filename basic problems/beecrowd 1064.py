positive = 0
sum = 0

for i in range (6):
    x = float(input())
    if x > 0:
        positive = positive + 1
        sum = sum + x
        average = sum/positive

print(positive, 'valores positivos')
print('%.1f' % average)