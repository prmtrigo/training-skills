count_even = 0
count_odd = 0
positive  = 0
negative = 0

for i in range (5):
    x = float(input())
    if x % 2 == 0:
        count_even += 1
    if x % 2 !=0:
        count_odd += 1
    if x > 0:
        positive += 1
    if x < 0:
        negative += 1

print(count_even, 'valor(es) par(es)')
print(count_odd, 'valor(es) impar(es)')
print(positive, 'valor(es) positivo(s)')
print(negative, 'valor(es) negativo(s)')