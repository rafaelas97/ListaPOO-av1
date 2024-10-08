numeroTabuada = int(input("Escreva um número (entre 1 e 10) para visualisar a tabuada: "))  
if 1 <= numeroTabuada <= 10:
    print(f"Tabuada do {numeroTabuada}:") 
    for multiplicador in range(1, 11):
        print(f"{numeroTabuada} X {multiplicador} = {numeroTabuada * multiplicador}")
else:
        print("O número precisa ser entre 1 e 10.")


