paisA = 80000
paisB = 200000
crescimentoA = 0.03  
crescimentoB = 0.015 
anos = 0
while paisA < paisB:
    paisA += paisA * crescimentoA
    paisB += paisB * crescimentoB
    anos += 1
print(f"Vão levar {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")