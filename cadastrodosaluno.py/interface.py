import tkinter as tk
from tkinter import simpledialog, messagebox

def validar_matricula(numero_matricula):
    """Valida o número de matrícula."""
    return len(numero_matricula) <= 5 and numero_matricula.isdigit() and int(numero_matricula) != 0

def fazer_matricula(alunos, vagas_disponiveis, disciplina, root):
    """Realiza o processo de matrícula em uma disciplina."""
    while vagas_disponiveis > 0:
        numero_matricula = simpledialog.askstring("Matrícula", "Digite o número da matrícula (até 5 dígitos):", parent=root)
        if numero_matricula is None:  # Usuário cancelou
            break
        nome_aluno = simpledialog.askstring("Nome do Aluno", "Digite o nome do aluno:", parent=root)
        if nome_aluno is None:  # Usuário cancelou
            break
        if not validar_matricula(numero_matricula):
            messagebox.showerror("Erro", "Número de matrícula inválido. Tente novamente.")
            continue
        if numero_matricula in alunos:
            messagebox.showerror("Erro", "Aluno já matriculado nesta disciplina.")
            continue
        alunos[numero_matricula] = nome_aluno
        vagas_disponiveis -= 1
        messagebox.showinfo("Sucesso", f"Aluno {nome_aluno} matriculado com sucesso em {disciplina}.")
        continuar = messagebox.askyesno("Continuar", "Deseja matricular outro aluno?")
        if not continuar:
            break
    return alunos, vagas_disponiveis

def main():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    alunos_matematica = {}
    alunos_contabilidade = {}
    vagas_matematica = 150
    vagas_contabilidade = 100

    alunos_matematica, vagas_matematica = fazer_matricula(alunos_matematica, vagas_matematica, "Matemática I", root)
    alunos_contabilidade, vagas_contabilidade = fazer_matricula(alunos_contabilidade, vagas_contabilidade, "Contabilidade I", root)

    # Aqui você pode adicionar o código para exibir os alunos matriculados e outras informações conforme necessário

    root.mainloop()

if __name__ == "__main__":
    main()
