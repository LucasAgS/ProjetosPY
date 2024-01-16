''' Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. 
Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta
foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D'''

Gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
Gabarito_aluno = []
nota = 0

for i in range(10):
    Gabarito_aluno.append(input(f'Digite a sua resposta da pergunta {i+1}: ').upper().strip())
    if Gabarito_aluno[i] not in 'A' 'B' 'C' 'D':
        while Gabarito_aluno[i] not in 'A' 'B' 'C' 'D':
            del Gabarito_aluno[i]
            print('Valor invalido')
            Gabarito_aluno.append(input(f'Digite a sua resposta da pergunta {i+1}: ').upper().strip())
            print(Gabarito_aluno)
for n in range(len(Gabarito)):
    if Gabarito[n] == Gabarito_aluno[n]:
        nota += 1

print(f'Sua nota foi: {nota:.1f}\nO gabarito correto: {', '.join(map(str, Gabarito))}\nSeu gabarito: {', '.join(map(str, Gabarito_aluno))}')
