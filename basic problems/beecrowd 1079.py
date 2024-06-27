x = int(input())

for i in range (x):
    a,b,c=list(map(float,input().split()))
    average = (a*2 + b*3 + c*5)/10
    print('{:.1f}'.format(average))
