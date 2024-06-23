#Escrever um programa Python que lê cinco números inteiros, armazenando-os em um vetor (list).
##posição não pode ser menor que o valor da posição anterior. Enquanto esta restrição não for atendida,
#exibir mensagem e ler novamente. No final da entrada de dados, exibir o vetor em ordem inversa.
#Atenção: perceba que não é para ler fora de ordem e ordenar depois. A ordenação deve ser assegurada na
#entrada dos dados.
def main():
    vetor = []
    
    print("Informe 5 valores ordenados:")
    
    while len(vetor) < 5:
        valor = int(input())
        
        if len(vetor) > 0 and valor < vetor[-1]:
            print("Inválido, informe outro:")
        else:
            vetor.append(valor)
    
    print("Valores em ordem inversa:")
    for num in reversed(vetor):
        print(num)

if __name__ == "__main__":
    main()
