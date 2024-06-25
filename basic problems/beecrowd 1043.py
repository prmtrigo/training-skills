a,b,c=list(map(float,input().split()))

if (c < a+b and b < a+c and a < b+c):
    print("Perimetro = {:.1f}".format(a+b+c))
else:
    print("Area = {:.1f}".format((a+b)*c/2))