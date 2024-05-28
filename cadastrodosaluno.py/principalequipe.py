import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel, Listbox

# Função para validar a matrícula
def validar_matricula(numero_matricula):
    """Valida o número de matrícula."""
    return len(numero_matricula) == 11 and numero_matricula.isdigit() and int(numero_matricula) != 0

# Função para mostrar os alunos matriculados
def mostrar_alunos(alunos, disciplina):
    """Mostra uma nova janela com a lista de alunos matriculados."""
    janela = Toplevel()
    janela.title(f"Alunos Matriculados em {disciplina}")
    janela.configure(background='light grey')  # Cor de fundo da janela de listagem
    listbox = Listbox(janela, bg='white', fg='black')  # Cores do Listbox
    listbox.pack(fill='both', expand=True)
    for matricula, nome in alunos.items():
        listbox.insert('end', f"{matricula}: {nome}")

# Função para realizar a matrícula
def fazer_matricula(alunos, vagas_disponiveis, disciplina, root):
    """Realiza o processo de matrícula em uma disciplina."""
    while vagas_disponiveis > 0:
        numero_matricula = simpledialog.askstring("Matrícula", "Digite seu CPF:", parent=root)
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

# Função principal
def main():
    root = tk.Tk()
    root.title("Sistema de Matrícula")
    root.configure(background='pink')  # Cor de fundo da janela principal
    root.geometry('800x600')

    alunos_matematica = {}
    alunos_contabilidade = {}
    vagas_matematica = 150
    vagas_contabilidade = 100

    # Frame para Matemática I
    frame_matematica = tk.Frame(root, bg='light blue', bd=5)
    frame_matematica.pack(pady=10, padx=10, fill='both')

    # Botão para mostrar alunos matriculados em Matemática I
    btn_matematica = tk.Button(frame_matematica, text="Ver Alunos de Matemática I", command=lambda: mostrar_alunos(alunos_matematica, "Matemática I"), bd=5)
    btn_matematica.pack(pady=5, padx=10)

    # Botão para matricular alunos em Matemática I
    btn_matricula_matematica = tk.Button(frame_matematica, text="Matricular em Matemática I", command=lambda: fazer_matricula(alunos_matematica, vagas_matematica, "Matemática I", root), bd=5)
    btn_matricula_matematica.pack(pady=5, padx=10)

    # Frame para Contabilidade I
    frame_contabilidade = tk.Frame(root, bg='light green', bd=5)
    frame_contabilidade.pack(pady=10, padx=10, fill='both')

    # Botão para mostrar alunos matriculados em Contabilidade I
    btn_contabilidade = tk.Button(frame_contabilidade, text="Ver Alunos de Contabilidade I", command=lambda: mostrar_alunos(alunos_contabilidade, "Contabilidade I"), bd=5)
    btn_contabilidade.pack(pady=5, padx=10)

    # Botão para matricular alunos em Contabilidade I
    btn_matricula_contabilidade = tk.Button(frame_contabilidade, text="Matricular em Contabilidade I", command=lambda: fazer_matricula(alunos_contabilidade, vagas_contabilidade, "Contabilidade I", root), bd=5)
    btn_matricula_contabilidade.pack(pady=5, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
