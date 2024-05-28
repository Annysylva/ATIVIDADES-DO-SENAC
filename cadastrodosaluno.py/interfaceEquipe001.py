import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel, Listbox

def validar_matricula(numero_matricula):
    """Valida o número de matrícula."""
    return len(numero_matricula) <= 5 and numero_matricula.isdigit() and int(numero_matricula) != 0

def mostrar_alunos(alunos, disciplina):
    """Mostra uma nova janela com a lista de alunos matriculados."""
    janela = Toplevel()
    janela.title(f"Alunos Matriculados em {disciplina}")
    listbox = Listbox(janela)
    listbox.pack(fill='both', expand=True)
    for matricula, nome in alunos.items():
        listbox.insert('end', f"{matricula}: {nome}")
    janela.mainloop()

def fazer_matricula(alunos, vagas_disponiveis, disciplina, root):
    """Realiza o processo de matrícula em uma disciplina."""
    while vagas_disponiveis > 0:
        numero_matricula = simpledialog.askstring("Matrícula", "Digite o número da matrícula (até 5 dígitos):", parent=root)
        if numero_matricula is None:  
            break
        nome_aluno = simpledialog.askstring("Nome do Aluno", "Digite o nome do aluno:", parent=root)
        if nome_aluno is None:  
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
    root.withdraw()  

    alunos_matematica = {}
    alunos_contabilidade = {}
    vagas_matematica = 150
    vagas_contabilidade = 100

    alunos_matematica, vagas_matematica = fazer_matricula(alunos_matematica, vagas_matematica, "Matemática I", root)
    alunos_contabilidade, vagas_contabilidade = fazer_matricula(alunos_contabilidade, vagas_contabilidade, "Contabilidade I", root)

    
    root.deiconify() 
    btn_matematica = tk.Button(root, text="Ver Alunos de Matemática I", command=lambda: mostrar_alunos(alunos_matematica, "Matemática I"))
    btn_matematica.pack()

    
    btn_contabilidade = tk.Button(root, text="Ver Alunos de Contabilidade I", command=lambda: mostrar_alunos(alunos_contabilidade, "Contabilidade I"))
    btn_contabilidade.pack()

    root.mainloop()

if __name__ == "__main__":
    main()