l = []
for i in range(100):
    l.append(float(input()))
    if l[i] <= 10:
        print("A[{}] = {:.1f}".format(i, l[i]))
