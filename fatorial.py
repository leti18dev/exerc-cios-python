# 5! = 5*4*3*2*1 = 120
# 4! = 4*3*2*1 = 24
# 3! = 3*2*1 = 6
# 2! = 2*1 = 2
# 1! = 1 * 0!


def fatorial(n):
    if n==0:
        return 1
    else:
        return n * fatorial(n - 1)
    
print(fatorial(5))


