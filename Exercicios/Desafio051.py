"""
Desenvolva um programa que leia o primeiro termo e a razão de PA (Progressão aritmética)
No final mostre os 10 primeiros termos dessa progressão.
"""

# Solicitando o numero
n = int(input('Digite um número: '))

# Solicitando a PA
pa = int(input('Digite a PA para este número: '))

# Obtendo os 10 primeiros termos da progressão
decimo = n + 10 * pa

# Laço de repetição
for i in range(n, decimo, pa):

    # Imprimindo a sequencia
    print(i)
    
# Fim do programa
print('FIM')
