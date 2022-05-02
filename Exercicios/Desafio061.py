"""
Refaça o desafio051, lendo o primeiro termo e a razão de uma PA, mostrando os 10
primeiros termos da progressão usando a estrutura WHILE
"""

# Imprimindo msg da solução
print('Gerando PA')
print('=-=' * 10)

# Obtendo o primeiro termo
prim = int(input('Primeiro termo: '))
# Obtendo a razão
razao = int(input('Razão da PA: '))
# Termo da progressão
termo = prim
# Contador
cont = 1

while cont <= 10:
    print('{} ⇒ '.format(termo), end='')
    termo = termo + razao
    cont = cont + 1

print('FIM')
