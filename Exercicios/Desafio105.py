'''

Faça um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:
=> Quantidade de notas
=> A maior nota
=> A menor nota
=> A média da turma
=> A situação (opcional)

Adicione também as DOCSTRINGS da função.

'''


# Criando função que receberá vária notas como parâmetro e situação(opcional)
def notas(*n, situacao=False):
    """
    => Função para analisar as notas e situações de alunos.
    :param n: Receberá várias notas.
    :param situacao: (opcional) mostra a situação do aluno.
    :return: retorna um dicionário contendo a nota mais baixa, média das notas, nota máxima e total de notas.
    """
    # Criando dicionário
    r = dict()
    # Total de notas
    r['Total'] = len(n)
    # Maior nota
    r['Maior'] = max(n)
    # Menor nota
    r['Menor'] = min(n)
    # Média das notas
    r['Média'] = sum(n) / len(n)

    # Parâmetro opcional para imprimir situação
    if situacao:
        if r['Média'] > 7:
            r['Situação'] = 'Aprovado'
        elif 5 < r['Média'] < 7:
            r['Situação'] = 'Recuperação'
        else:
            r['Situação'] = 'Reprovado'

    return r


# Programa Principal
resp = notas(5.5, 5.2, 9, 8.5)
print(resp)
