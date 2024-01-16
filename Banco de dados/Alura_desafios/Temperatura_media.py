'''Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. 
Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. 
Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual
e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).'''

Mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
        'junho', 'Julho', 'Agosto', 'Outubro', 'Novembro', 'Dezembro']
Temperatura = []

for i in range(11):
    try:
        Temperatura.append(float(input(f'Digite a temperatura do mês de {Mes[i]}: ')))
         
    except ValueError:
        entrada = False
        print('Valor invalido.')
        while True:
            try:
                Temperatura.append(float(input(f'Digite a temperatura do mês de {Mes[i]}: ')))
                break
            except ValueError:
                print('Valor invalido')

media = sum(Temperatura) / len(Temperatura)

print(f'A media do ano foi de :{media:.1f}ºC\nOs meses que superaram a media anual foram: ')
for i in range(len(Temperatura)):
    if Temperatura[i] > media:
        print(f'{Mes[i]} {Temperatura[i]}ºC')
        