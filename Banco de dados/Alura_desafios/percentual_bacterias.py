#percentual de crescimento bacterias
bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
percentual = 0
crescimento_dia = []


#100*(amostra_atual-amostra_passada)/(amostra_passada)

for i in range(len(bacterias)):
  try:
    percentual = round(abs(100 * (bacterias[i] - bacterias[i+1]) / (bacterias[i])), 2)
    crescimento_dia.append(percentual)
  except IndexError:
    pass
   
print(crescimento_dia)
