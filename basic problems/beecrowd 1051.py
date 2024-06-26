x = float(input())

if 0 < x <= 2000:
    print("Isento")
elif 2000 < x <= 3000:
    dif = x - 2000
    tax = dif * 0.08
    print("R$ %.2f" % tax)
elif 3000 < x <= 4500:
    dif = x - 3000
    tax = dif * 0.18 + (1000 * 0.08)
    print("R$ %.2f" % tax)
else:
    dif = x - 4500
    tax = dif * 0.28 + (1500 * 0.18) + (1000 * 0.08)
    print("R$ %.2f" % tax)
