import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel, Listbox, PhotoImage

# Função para validar a matrícula
def validar_matricula(numero_matricula):
    """Valida o número de matrícula."""
    return len(numero_matricula) == 5 and numero_matricula.isdigit()

# Função para mostrar os alunos matriculados
def mostrar_alunos(alunos, disciplina):
    """Mostra uma nova janela com a lista de alunos matriculados."""
    janela = Toplevel()
    janela.title(f"Alunos Matriculados em {disciplina}")
    listbox = Listbox(janela, bg='white', fg='black')
    listbox.pack(fill='both', expand=True)
    for matricula, nome in alunos.items():
        listbox.insert('end', f"{matricula}: {nome}")

# Função para realizar a matrícula
def fazer_matricula(alunos, disciplina, root):
    """Realiza o processo de matrícula em uma disciplina."""
    numero_matricula = simpledialog.askstring("Matrícula", "Digite o número da matrícula (5 dígitos):", parent=root)
    if numero_matricula and validar_matricula(numero_matricula):
        if numero_matricula in alunos:
            messagebox.showerror("Erro", "Aluno já matriculado nesta disciplina.")
        else:
            nome_aluno = simpledialog.askstring("Nome do Aluno", "Digite o nome do aluno:", parent=root)
            if nome_aluno:
                alunos[numero_matricula] = nome_aluno
                messagebox.showinfo("Sucesso", f"Aluno {nome_aluno} matriculado com sucesso em {disciplina}.")
    else:
        messagebox.showerror("Erro", "Número de matrícula inválido.")

# Função principal
def main():
    root = tk.Tk()
    root.title("Sistema de Matrícula")

    # Carregar a imagem
    imagem = PhotoImage(file='python.png.png')
    label_imagem = tk.Label(root, image=imagem)
    label_imagem.pack(pady=10)

    alunos = {}
    disciplina = "Matemática I"

    # Botão para mostrar alunos matriculados
    btn_mostrar = tk.Button(root, text=f"Ver Alunos de {disciplina}", command=lambda: mostrar_alunos(alunos, disciplina))
    btn_mostrar.pack(pady=10)

    # Botão para matricular alunos
    btn_matricular = tk.Button(root, text=f"Matricular em {disciplina}", command=lambda: fazer_matricula(alunos, disciplina, root))
    btn_matricular.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
