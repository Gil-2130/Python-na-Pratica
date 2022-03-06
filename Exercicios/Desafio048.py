"""
Faça um programa que calcule a soma entre todos os numeros ímpares
que são multiplos de três e que se encontram no intervalo entre 1 até 500
"""
# Criando uma variavel que irá armazenar os valores para soma 
soma = 0

# Laço com um range d evalores
for i in range(1, 500):
    
    # Contador
    soma += i
    
    # Condicional para números divisíveis por 03 e apenas ímpares
    if i % 3 == 0 and i % 2 == 1:
      
        print(i)

# Imprimindo a soma total
print(soma)
