preço = float(input("Digite o preço da mercadoria:"))
desconto = float(input("Digite o percentual de desconto:"))
valor_do_desconto = preço * desconto / 100
a_pagar = preço - valor_do_desconto
print("Um desconto de %5.2f %% em uma mercadoria de R$ %7.2f" % (desconto, preço))
print("vale R$ %7.2f." % valor_do_desconto)
print("O valor a pagar é de R$ %7.2f" % a_pagar)

def calculo(quant, preco, desc):
    preco_total = quant * preco
    valor_desconto = preco_total * (desc / 100)
    preco_final = preco_total - valor_desconto
    return preco_final

# Programa principal
def main():
    try:
        quant = int(input("Informe a quantidade: "))
        preco = float(input("Informe o preço unitário: "))
        desc = float(input("Informe o percentual de desconto: "))
        
        preco_final = calculo(quant, preco, desc)
        
        print("Preço final: {:.2f}".format(preco_final))
    except ValueError:
        print("Por favor, insira um valor válido.")

if __name__ == "__main__":
    main()