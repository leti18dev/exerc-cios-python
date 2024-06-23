def foo(n):
    print(f'inicio: {n}')
    if n>0:
        foo(n-1)
    print(f'fim: {n}')
    
foo(5)


    