primeiroAno= 1995
salario = 1000.00
ultimoAno = 2025
aumento = 0.015 

for anos in range(primeiroAno + 1, ultimoAno + 1):
    if anos > 1996:
        aumento *= 2 
        if aumento > 1:  
            aumento = 1
    salario *= (1 + aumento)  
print(f"O salário em 2025 será de R$ {salario:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
