contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtração': lambda a, b: a - b,
    'multiplicação': lambda a, b: a * b,
    'divisão': lambda a, b: a / b
}
soma = calculadora['soma']
multiplicacao = calculadora['multiplicação']
print(soma(10, 5))
print(multiplicacao(2, 8))
