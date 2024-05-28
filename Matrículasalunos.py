def validar_matricula(numero_matricula):
    """Valida o número de matrícula."""
    return len(numero_matricula) <= 5 and numero_matricula.isdigit() and int(numero_matricula) != 0

def fazer_matricula(alunos, vagas_disponiveis, disciplina):
    """Realiza o processo de matrícula em uma disciplina."""
    while True:
        numero_matricula = input("Digite o número da matrícula (até 5 dígitos): ").strip()
        nome_aluno = input("Digite o nome do aluno: ").strip()
        if not validar_matricula(numero_matricula):
            print("Número de matrícula inválido. Tente novamente.")
            continue
        if numero_matricula in alunos:
            print("Aluno já matriculado nesta disciplina.")
            continue
        if vagas_disponiveis > 0:
            alunos[numero_matricula] = nome_aluno
            vagas_disponiveis -= 1
            print(f"Aluno {nome_aluno} matriculado com sucesso em {disciplina}.")
        else:
            print(f"Não há vagas disponíveis em {disciplina}.")
            break
        
        continuar = input("Deseja matricular outro aluno? (sim/não): ").lower()
        if continuar != "sim":
            break
    return alunos

def main():
    alunos_matematica = {}
    alunos_contabilidade = {}
    vagas_matematica = 150
    vagas_contabilidade = 100

    print("Matrícula em Matemática I:")
    alunos_matematica = fazer_matricula(alunos_matematica, vagas_matematica, "Matemática I")

    print("\nMatrícula em Contabilidade I:")
    alunos_contabilidade = fazer_matricula(alunos_contabilidade, vagas_contabilidade, "Contabilidade I")

    print("\nMatrícula em Matemática I:")
    for matricula, nome in alunos_matematica.items():
        print(f"{matricula}: {nome}")

    print("\nMatrícula em Contabilidade I:")
    for matricula, nome in alunos_contabilidade.items():
        print(f"{matricula}: {nome}")

    alunos_em_ambos = set(alunos_matematica.keys()) & set(alunos_contabilidade.keys())
    if alunos_em_ambos:
        print("\nAlunos matriculados em ambas as disciplinas:")
        for matricula in alunos_em_ambos:
            nome = alunos_matematica[matricula]
            print(f"{matricula}: {nome}")
    else:
        print("\nNão há alunos matriculados em ambas as disciplinas.")

if __name__ == "__main__":
    main()
