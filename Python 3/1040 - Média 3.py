N1,N2,N3,N4 = input().split()
N1,N2,N3,N4= float(N1),float(N2),float(N3),float(N4)

media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10

if media >= 7.0:
    print('Media: %.1f'%media )
    print('Aluno aprovado.')
elif media < 5.0:
    print('Media: %.1f'%media )
    print('Aluno reprovado.')
elif media >= 5.0 and media <= 6.9:
    print('Media: %.1f'%media )
    print('Aluno em exame.')
    N_exame = float(input())
    print('Nota do exame: %.1f'%N_exame)
    nova_media = (media + N_exame)/2
    print('Aluno aprovado.')
    print('Media final: %.1f'%nova_media)