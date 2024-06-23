def pesq_binaria(vet,valor):
    inicio = 0
    final = len(vet)-1
    while inicio <= final:
        meio = (inicio + final) // 2
        if vet[meio] == valor :
            return meio
        elif vet[meio]< valor:
            inicio = meio +1
        else:
            final = meio - 1
    return -1

vet = [10,20,30,40,50,60,70,80,90,100]
print(pesq_binaria(vet,20))
