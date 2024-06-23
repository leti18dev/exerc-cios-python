a,b = map(int, input().split())

cachorro = 4.00
xsalada = 4.50
xbacon = 5.00
torrada = 2.00
refri = 1.50


if a == 1 :
    soma = cachorro * b
    print(f'Total: R$ {soma:.2f}')

elif a == 2 :
    soma = xsalada * b
    print(f'Total: R$ {soma:.2f}')

elif a == 3 :
    soma = xbacon * b
    print(f'Total: R$ {soma:.2f}')

elif a == 4 :
    soma = torrada * b
    print(f'Total: R$ {soma:.2f}')
elif a == 5 :
    soma = refri * b
    print(f'Total: R$ {soma:.2f}')



    