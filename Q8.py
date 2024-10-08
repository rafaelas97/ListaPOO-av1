def verificarNota(respostas, gabarito):
    acertos = 0
    for R in range(len(gabarito)):
        if respostas[R] == gabarito[R]:
            acertos += 1
            return acertos

def main():
    gabarito = ['A', 'D', 'S', 'A', 'B', 'C', 'D', 'E', 'R', 'L']
    acertosGeral = []
    alunosGeral = 0
    
    while True:
        alunosGeral += 1
        respostas_aluno = []

        print(f"Aluno {alunosGeral}:")
        
        for R in range(10):
            resposta = input(f"Digite a resposta da questão {R+1}: ").strip().upper()
            respostas_aluno.append(resposta)
        
        acertos = verificarNota(respostas_aluno, gabarito)
        acertosGeral.append(acertos)
        
        proximo = input("Digite (P) para o próximo aluno responder ou digite (E) para encerrar a atividade: ").strip().lower()
        if proximo != 'p':
            break
    
    if acertosGeral:
        maior_acerto = max(acertosGeral)
        menor_acerto = min(acertosGeral)
        media_notas = sum(acertosGeral) / len(acertosGeral)
        
        print("Resultados finais:")
        print(f"Maior acerto: {maior_acerto}")
        print(f"Menor acerto: {menor_acerto}")
        print(f"Total de alunos: {alunosGeral}")
        print(f"Média das notas da turma: {media_notas:.2f}")

if __name__ == "__main__":
    main()