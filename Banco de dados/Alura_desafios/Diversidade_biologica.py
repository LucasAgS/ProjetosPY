''' os valores nas listas correspondem às espécies de plantas 
e animais nas áreas, respectivamente.
Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica. Dica: use as funções built-in sum() e len().'''

Area_diversidade = {
'Área Norte': [2819, 7236],
'Área Leste': [1440, 9492],
'Área Sul': [5969, 7496],
'Área Oeste': [14446, 49688],
'Área Centro': [22558, 45148]}

Media_diversidade = {}
Maior_diversidade = {'Área': '', 'Diversidade': 0}
#0-plantas 1-animais
for areas, animais in Area_diversidade.items():
    diversidade = sum(animais)

    if diversidade > Maior_diversidade['Diversidade']:
        Maior_diversidade['Área'] = areas
        Maior_diversidade['Diversidade'] = diversidade

    area = {areas:int(sum(animais) / 2)}
    Maior_diversidade
    Media_diversidade.update(area)
print(f'{'Área':<20} | {'Media Especies':<20}')
for areas, especies in Media_diversidade.items():
    print(f'{areas:<20} | {especies:<20}')
print(f'{'-' * 40}')
print(f'{'Maior área':<20} | {'Total Especies':<20}')
print(f'{Maior_diversidade['Área']:<20} | {Maior_diversidade['Diversidade']:<20}')