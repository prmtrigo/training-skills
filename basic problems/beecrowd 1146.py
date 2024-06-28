while True:
    i = int(input())
    if i == 0:
        break
    else:
        for j in range(1, i):
            print(j, end=' ')
    print(i)