casos = int(input())

for i in range(casos):
  A = input()
  B = input()

if(len(B) > len(A)):
  print('nao encaixa')
else:
    A = A[(len(A) - len(B)):]
    print('encaixa' if A == B else 'nao encaixa')




