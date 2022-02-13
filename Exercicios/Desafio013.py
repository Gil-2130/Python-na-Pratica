"""
Faça um algoritmo que leia o salario de um funcionário
e mostre seu novo salario com 15% de aumento
"""

sal = float(input('Qual o seu salario? '))
#n_sal = sal + (sal * 0.15)
n_sal = sal + (sal * 15 / 100)
print('Seu antigo salário era de {}$\n'.format(sal),
      'Agora seu novo salário com ajuste de 15% é de {}$'.format(n_sal))
