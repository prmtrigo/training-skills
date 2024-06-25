import math

a,b,c = list(map(float,input().split()))

delta = ((b**2) - 4*a*c)

if (0 > delta or a == 0):
    print("Impossivel calcular")

elif (delta == 0):
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = x1
    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))

else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))
