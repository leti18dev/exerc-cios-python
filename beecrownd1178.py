N = [0]*100

valor = float(input())

for i in range(100):
  N[i] = valor
  valor = valor/2

for i in range(100):
  print(f'N[{i}] = {valor:.4f}')