print("Calcule de acordo com sua dívida: ")
divida = float(input("Escreva o valor da sua dívida: "))
parcelas = [1, 3, 6, 9, 12]
juros = [0, 10, 15, 20, 25]
print(f"{"Dívida":<15}{"Juros":<15}{"Parcelas":<15}{"Valor da parcela"}")

for J in range(len(parcelas)):
    valorJuros = divida * (juros[J] / 100)
    valorTotal = divida + valorJuros
    valorParcela = valorTotal / parcelas[J]

    print(f"R$ {valorTotal:,.2f}{" ":<7}{valorJuros:.2f}{" ":<7}{parcelas[J]:<20}R${valorParcela:,.2f}")