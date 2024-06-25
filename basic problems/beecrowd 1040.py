n1,n2,n3,n4 = list(map(float,input().split()))

media = (n1*2+n2*3+n3*4+n4)/10
print("Media: {:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    n5 = float(input())
    print("Nota do exame: {:.1f}".format(n5))
    media_final = (media + n5)/2

    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final: {:.1f}".format(media_final))
