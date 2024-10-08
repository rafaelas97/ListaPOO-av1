numerosInteiros = input("Escreva 10 números separados apenas por espaços: ").split()
pares = 0
impares = 0
for numero in numerosInteiros:
    numero = int(numero)
    if numero % 2 == 0:
        pares += 1  
    else:
        impares += 1  
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
