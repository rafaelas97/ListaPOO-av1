print("Lojas Quase Dois - Preços")
for itens in range(1, 51):
    valorCompra = itens * 1.99
    print(f"{itens} - R$ {valorCompra: .2f}")

quantidade = int(input("Digite a quantidade de itens (até 50): "))
if 1 >= quantidade <= 50:
    print("Aguarde valor final da compra:")
else:
    valorFinal = quantidade * 1.99
    print(f"Valor da compra: R$ {valorFinal: .2f}")