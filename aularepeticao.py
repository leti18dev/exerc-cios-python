#listas 
m = 0
while m < 1 or m > 12:
  m = int(input('Qual o mês (1..12)?'))

meses = ['jan','fev','mar','abr','maio', 'jun','jul','ago ','set','out','novem', 'deze']

print(meses[m -1])