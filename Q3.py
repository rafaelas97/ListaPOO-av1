numeroInteiro = int(input("Escreva um número:"))
if numeroInteiro < 2:
    print(f"{numeroInteiro} não é primo")
primo = True
for divisor in range(2, numeroInteiro):
    if numeroInteiro % divisor == 0:
        primo = False      
if primo:
    print(f"{numeroInteiro} é primo")
else:
    print(f"{numeroInteiro} não é primo")