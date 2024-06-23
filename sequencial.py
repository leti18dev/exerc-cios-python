# se encontrar retorna o indice
#se não retorna -1

def pesq_sequencial(vet, valor):
    for i in range(len(vet)):
        if vet[i]==valor:
            return i
    return -1
        




vet = [2,44,5,6,100,23,45]
print(pesq_sequencial(vet,100))

