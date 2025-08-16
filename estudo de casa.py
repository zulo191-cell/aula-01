nota1 = int(input('qual a sua nota do 1° semestre \n'))
nota2 = int(input('qual a sua nota do 2° semestre \n'))
media = (nota1+nota2)/2

# if: se for tal coisa
# else: se não for tal coisa

if nota1<=100 and nota2<=100:
    if media >= 60:
        print(f'sua nota é {media} você foi aprovado')
    else:
        print(f'sua nota é {media} e você foi repeovado')
else:
    print('\n as notas não podem ser maiores que 100 \n')