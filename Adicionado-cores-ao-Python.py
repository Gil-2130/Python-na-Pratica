"""

Cores no terminal
\033[STYLE;TEXT;BACKGROUNDm
\033[0;33;44m

STYLE -> 0(NoNe),  1(BOLD),  4(Underline), 7(Negative)
TEXT -> 30(White), 31(Red), 32(Green), 33(Yellow), 34(Blue), 35(Magente), 36(Ciano), 37(Gray)
BACKGROUND -> 40(White), 41(Red), 42(Green), 43(Yellow), 44(Blue), 45(Magente), 46(Ciano), 47(Gray)

"""


print('\033[0;30;41mTESTE')
print('\033[4;33;44mTESTE')
print('\033[1;35;43mTESTE')
print('\033[30;42mTESTE')
print('\033[mTESTE')
print('\033[7;30mTESTE')

print('\033[30;43mOlá mundo\033[m')

a = 3
b = 5
print('Os valores sao \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

nome = 'Giliard'
print('Olá, muito prazer em te conhecer, {}{}{}'.format('\033[32m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Olá, muito prazer em te conhecer, {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))
print('Olá, muito prazer em te conhecer, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))
