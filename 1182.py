#beecrowd | 1182
coluna = int(input())
op = input()
soma = 0
matriz = []
vetor = []


for lin in range(12):
  for col in range(12):
    valor = float(input())
    vetor.append(valor)
    if(col==coluna):
      soma+=valor
  matriz.append(vetor)
  vetor = []
if(op=='S'):
  print('%.1f'%soma)
if(op=='M'):
  print('%.1f'%(soma/12))


