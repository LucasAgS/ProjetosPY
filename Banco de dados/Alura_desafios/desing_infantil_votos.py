'''Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, 
informe o design vencedor e a porcentagem de votos recebidos.'''

Votos = { 'Design 1':1334, 'Design 2':982, 
          'Design 3':751, 'Design 4':210, 
          'Design 5':1811}
Vencedor = {'Design':'', 'Votos': 0}

Total_votos = sum(Votos.values())
for design, votos in Votos.items():
    if votos > Vencedor['Votos']:
        Vencedor['Design'] = design
        Vencedor['Votos'] = votos

Design_vencedor = Vencedor['Votos']
percentual = round(abs((Design_vencedor / sum(Votos.values())) * 100), 2)
print(f'O vencedor foi o {Vencedor['Design']} com {Vencedor['Votos']} votos. Um total de {percentual}% dos {Total_votos} recebidos.')