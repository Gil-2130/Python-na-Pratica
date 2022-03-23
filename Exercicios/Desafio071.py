Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, pregunte ao usuário qual será o valor a ser sacado(inteiro)
Seu programa deve informar quantas cédulas de cada valor serão entregues.

Obs; Considere que o caixa possui cédulas de 50, 20, 10 e 1

print('='*30)
print('{:=^30}'.format(' BANCO PYTHON '))
print('='*30)

valor = int(input('Qual a Quantia deseja sacar hoje? R$'))

total = valor
cedula = 50
total_ced = 0

while True:
    if total >= cedula:
        total = total - cedula
        total_ced = total_ced + 1

    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R${cedula}')

        if cedula == 50:
            cedula = 20

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 1

        total_ced = 0

        if total == 0:
            break

print('=' * 30)
print('Obrigado por ser cliente do BANCO PYTHON!!')
