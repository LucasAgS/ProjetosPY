''' Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs
dados por números inteiros sabendo que os produtos com ID par são doces e os com ID
ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade
de produtos doces e amargos. '''
Doce = 0
Amargo = 0
Identificador = []

for i in range(0, 10):
   # Identificador.append(int(input('Digite o ID do produto: '))) -> maneira encurtada.
    try:
        valor = int(input('Digite o ID do produto: '))
        Identificador.append(valor)
        if valor % 2 == 0:
            Doce += 1
        else:
            Amargo += 1
    except ValueError:
        print('valor invalido')
print(f'Foram adicionados {Doce} produtos doces e {Amargo} Amargos')
print(f"Os ID's foram: {', '.join(map(str, Identificador))}")
