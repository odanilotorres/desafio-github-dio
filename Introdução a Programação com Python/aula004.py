# # Mostrar um intervalo de número
# for x in range (100):
#     print('x = {}'.format(x))

# # Descobrir se é um nmero Numero primo
# a = int(input('Digite um numero: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Numero {} é primo.'.format(a))
# else:
#     print('Numero {} nao é primo.'.format(a))

#Descobrir quais são os numeros primos em um range
# for i in range(101):
#     div = 0
#     for x in range(1, i+1):
#         resto = i % x
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print('Numero {} é primo.'.format(i))
#     # else:
#     #     print('Numero {} nao é primo.'.format(i))

# Usando o While
a = int(input('Digite a primeira nota: '))
while a > 10:
    print('Nota errada, digite novamente; ')
    a = int(input('Digite a primeira nota: '))
b = int(input('Digite a segunda nota: '))
while b > 10:
    print('Nota errada, digite novamente; ')
    b = int(input('Digite a segunda nota: '))
c = int(input('Digite a terceira nota: '))
while c > 10:
    print('Nota errada, digite novamente; ')
    c = int(input('Digite a terceira nota: '))
d = int(input('Digite a quarta nota: '))
while d > 10:
    print('Nota errada, digite novamente; ')
    d = int(input('Digite a quarta nota: '))
media = (a + b + c + d)/4
print('Sua média foi {} '.format(media))
if media >= 7:
    print('Você foi aprovado!')
else:
    print('Voc foi reprovado.')
