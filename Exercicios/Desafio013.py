"""
Faça um algoritmo que leia o salario de um funcionário
e mostre seu novo salario com 15% de aumento
"""

# Obtendo o salário
sal = float(input('Qual o seu salario? '))
#n_sal = sal + (sal * 0.15)
# Calculando o novo salário
n_sal = sal + (sal * 15 / 100)
# Imprimindo os resultados obtidos
print('Seu antigo salário era de {}$\n'.format(sal),
      'Agora seu novo salário com ajuste de 15% é de {}$'.format(n_sal))
