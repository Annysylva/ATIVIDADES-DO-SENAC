matriculas_matematica = set()
matriculas_contabilidade = set()

while True:
    matricula = input("Digite a matrícula do aluno em Matemática I (ou 'fim' para encerrar): ")
    if matricula.lower() == 'fim':
        break
    matriculas_matematica.add(matricula)

while True:
    matricula = input("Digite a matrícula do aluno em Contabilidade I (ou 'fim' para encerrar): ")
    if matricula.lower() == 'fim':
        break
    matriculas_contabilidade.add(matricula)

alunos_em_ambas_disciplinas = matriculas_matematica & matriculas_contabilidade

print("\nAlunos inscritos em ambas as disciplinas:")
for matricula in alunos_em_ambas_disciplinas:
    print(matricula)
