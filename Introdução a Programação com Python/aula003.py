# a = int(input('Digite o valor A: '))
# b = int(input('Digite o valor B: '))
# c = int(input('Digite o valor C: '))
# if a > b and a > c:
#     print('O maior número é A = {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é B = {}'.format(b))
# else:
#     print('O maior número é C = {}'.format(c))

# print('Descobrir se é par:')
# a = int(input('Digite um valor: '))
# resto = a % 2
# if resto == 0:
#     print('{} É par'.format(a))
# else:
#     print('{} É ímpar'.format(a))

print('Validando nota')
print()
a = int(input('Digite a primeira nota: '))
b = int(input('Digite a segunda nota: '))
c = int(input('Digite a terceira nota: '))
d = int(input('Digite a quarta nota: '))
media = (a+b+c+d)/4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('Média: {}'.format(media))
    if media >= 7:
        print('Vpcê foi aprovado')
    else:
        print('Você foi reprovado.')
else:
    print('Foi informado alguma nota errada.')