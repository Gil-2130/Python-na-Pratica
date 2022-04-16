# EXEMPLO 01
nome = str(input('Qual á o seu nome? '))
if nome == 'Maria'.lower():
    print('Olá {}, seja bem vindo ao Python!'.format(nome))

else:
    print('Olá {}, muito prazer!'.format(nome))

print('Fim do Programa!')

# EXEMPLO 2
tempo = int(input('Quantos anos tem seu veiculo? '))
print('Carro novo' if tempo <=5 else 'Carro velho')
print('=====FIM=====' * 3)

# EXEMPLO 3
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua nota média foi {} pontos'.format(m))

if m>= 6.0:
    print('Sua média foi boa! PARABENS!!')
else:
    print('Sua média foi baixa! Estude Mais!')

# SIMPLIFICANDO
print('PARABÉNS' if m >=6 else 'Nota Ruim, Precisa estudar MAIS')
