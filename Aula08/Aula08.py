nome = str(input('Digite seu nome: ')).upper()

# Condição simples (possui apenas um IF)
if nome == 'Eduardo':
    print('Que nome bonito')
print('Tenha um bom dia, {}'.format(nome))
print('-=-'*20)

#=============== Condição Composta ===============
# usei esse método para colocar o nome em maiusculo,
# e atender a condição caso o usuario digite em minusculo.
if nome == 'Eduardo'.upper():
    print('Que nome bonito')
else:
    print('Seu nome é bem normal rsrs...')
print(f'tenha um bom dia, {nome}')
print('-=-'*20)


#================ Estrutura condicional aninhada ===============
# usei esse método para colocar o nome em maiusculo,
# e atender a condição caso o usuario digite em minusculo.
if nome == 'Eduardo':
    print('Que nome bonito')
elif nome == 'Pedro'.upper() or nome == 'Maria'.upper() or nome == 'Paulo'.upper():
    print('Seu nome é bem Popular!!')
elif nome in 'Ana Claudia Jessica Juliana'.upper():
    print('Lindo nome Feminino!')
else:
    print('Seu nome é bem normal rsrs...')
print(f'tenha um bom dia, {nome}')
