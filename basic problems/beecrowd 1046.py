x,y = list(map(int, input().split()))

if ( x < y):
    tempo =  y - x
else:
    tempo = y + 24 - x
print("O JOGO DUROU {} HORA(S)".format(tempo))