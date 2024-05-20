matriculas_matematica = []

for POSMAT in range(1, 10):
    matricula = input(f"Digite a matrícula do aluno {POSMAT} de Matemática: ")
    matriculas_matematica.append(matricula)

print("Matrículas dos alunos inscritos em Matemática:")
for matricula in matriculas_matematica:
    print(matricula)

