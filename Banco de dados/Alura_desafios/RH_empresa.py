'''O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:

Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.'''

Setores = {
 'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
#idade media de cada setor = OK
#idade media geral Ok
#quantas pessoas estão a cima da idade media geral Ok
Media_setor = {}
Media_geral = 0
Acima_idade_geral = 0

for setor, idade in Setores.items():
    media_idade = int(sum(idade) / 10)
    Media_setor[setor] = media_idade
for setor, idade in Media_setor.items():
    Media_geral += idade / 4
for setor, idade in Setores.items():
    for numeros in range(len(idade)):
        if idade[numeros] > Media_geral:
            Acima_idade_geral += 1
print(f'{'-' * 40}')
print(f'{'Setor':<20} | {'Media idade':<20}')
for setor, idade in Media_setor.items():
    print(f'{setor:<20} | {idade:<20}')
print(f'{'-' * 40}')
print(f'{'Media geral de idade':<20} | {int(Media_geral):<20}')
print(f'{'Acima idade geral':<20} | {Acima_idade_geral:<20}')
print(f'{'-' * 40}')
