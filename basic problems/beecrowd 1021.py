#beecrowd 1021
money = float(input())

notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
remaing_money = int(money * 100)
for note in notes:
    note_in_cents = int(note * 100)
    count = remaing_money // note_in_cents
    remaing_money -= count * note_in_cents
    print('{} nota(s) de R$ {:.2F}'.format(count, note))

print('MOEDAS:')
for coin in coins:
    coin_in_cents = int(coin * 100)
    count = remaing_money // coin_in_cents
    remaing_money -= count * coin_in_cents
    print('{} moeda(s) de R$ {:.2F}'.format(count, coin))