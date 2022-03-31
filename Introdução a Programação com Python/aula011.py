lista = [1, 10]

try:
    divisão = 10 / 1
    numero = lista[1]
    x = a
except ZeroDivisionError:
    print('Nao e possivel realizar uma divisao por 0')

except IndexError:
    print('Erro ao acessar um indice.')

except BaseException as ex: #usa esse quando você não sabe qual erro vira
    print('Erro desconhecido: {}'.format(ex))
else:
    print('Executa quando nao ocorre excessao')
finally:
    print('Sempre executa')