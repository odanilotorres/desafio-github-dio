# conjunto = {1, 2, 3, 4, 2, 4} #nao existe duplicidade, só vai motrar uma única vez cada elemento
# conjunto.add(5) #adicionando um elemnto no conjunto
# conjunto.discard(2) #removendo um elemento do conjunto
# print(conjunto)

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9}
conjunto_uniao = conjunto1.union(conjunto2) #unindo conjunto
print('Uniao: {}'.format(conjunto_uniao))

conjunto_intersection = conjunto1.intersection(conjunto2)
print('INtersection: {}'.format(conjunto_intersection)) #mostra o que se repete nos conjuntos

conjunto_diferenca1 = conjunto1.difference(conjunto2) #mostra apenas o que tem no conjunto 1 tirando o que se repete no 2
conjunto_diferenca2 = conjunto2.difference(conjunto1) #mostra apenas o que tem no conjunto 2 tirando o que se repete no 1
print('Diferenca 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferenca 2 e 1: {}'.format(conjunto_diferenca2))

conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2) #mostra o que tem nos dois, sem as repeticoes
print('Diferenca simetrica : {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b) #mostra se conjutno a esta dentro de conjunto b
print('A é subconjunto de B: {}'.format(conjunto_subset))

conjunto_superset = conjunto_b.issuperset(conjunto_a) #conjunto B contem os valores do conjunto a dentro de si
print('B é superconjunto de A: {}'.format(conjunto_superset))

#Convertendo Lista para Conjunto para tirar a duplicidade

lista = {'cachorro', 'cachorro', 'gato', 'gato', 'elefante'}
conjunto_animais = set(lista)
print(conjunto_animais)