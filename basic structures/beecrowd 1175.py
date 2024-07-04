l = []
for i in range(20):
    l.append(int(input()))

r = l[::-1]
for j in range(20):
    print("N[{}] = {}".format(j, r[j]))
