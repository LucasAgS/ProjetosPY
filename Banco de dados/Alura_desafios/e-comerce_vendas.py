'''Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. 
Os dados das vendas foram armazenados em um dicionário
Escreva um código que calcule o total de vendas e o produto mais vendido'''

Vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
           'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
Maior = {'Produto': '', 'Quantidade': 0}
Total = sum(Vendas.values())

for produto, quantidade in Vendas.items():
    if quantidade > Maior['Quantidade']:
        Maior['Produto'] = produto
        Maior['Quantidade'] = quantidade
        
print(f'O total de vendas foi de: {Total}\nO produto mais vendido foi {Maior['Produto']} com {Maior['Quantidade']} vendas')


