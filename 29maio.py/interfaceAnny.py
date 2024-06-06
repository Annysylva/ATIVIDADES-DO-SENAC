import tkinter as tk
from tkinter import messagebox, simpledialog, Button, Text, Scrollbar
import os

class Anny:
    def __init__(self, nome="Anny", estudando=False, dormindo=False, maquiando=False, comendo=False):
        self.nome = nome
        self.estudando = estudando
        self.dormindo = dormindo
        self.maquiando = maquiando
        self.comendo = comendo
        self.diario = []

    def estudar(self):
        self.estudando = True
        self.dormindo = False
        self.maquiando = False
        self.comendo = False
        messagebox.showinfo("Status", f"{self.nome} está estudando. Legal!")

    def dormir(self):
        self.estudando = False
        self.dormindo = True
        self.maquiando = False
        self.comendo = False
        messagebox.showinfo("Status", f"{self.nome} está dormindo. Zzzzzz...")

    def maquiar(self):
        self.estudando = False
        self.dormindo = False
        self.maquiando = True
        self.comendo = False
        messagebox.showinfo("Status", f"{self.nome} está se maquiando, ficou linda!")

    def comer(self):
        if self.dormindo:
            messagebox.showinfo("Status", f"{self.nome} não pode comer enquanto dorme!")
        else:
            self.comendo = True
            self.estudando = False
            self.maquiando = False
            messagebox.showinfo("Status", f"{self.nome} está comendo. Muito saboroso!")

    def status(self):
        status = {
            "estudando": self.estudando,
            "dormindo": self.dormindo,
            "maquiando": self.maquiando,
            "comendo": self.comendo
        }
        status_message = "\n".join([f"{self.nome} está {atividade}: {estado}" for atividade, estado in status.items()])
        messagebox.showinfo("Status Atual", status_message)

    def adicionar_diario(self, entrada):
        self.diario.append(entrada)

    def limpar_diario(self):
        self.diario.clear()

    def mostrar_diario(self):
        if self.diario:
            diary_window = tk.Toplevel()
            diary_window.title("Diário de Anny")

            scrollbar = Scrollbar(diary_window)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            diary_text = Text(diary_window, yscrollcommand=scrollbar.set)
            diary_text.pack(fill=tk.BOTH, expand=True)

            for entry in self.diario:
                diary_text.insert(tk.END, entry + "\n")

            scrollbar.config(command=diary_text.yview)

            clear_button = Button(diary_window, text="Limpar Diário", command=self.limpar_diario)
            clear_button.pack(pady=10)
        else:
            messagebox.showinfo("Diário", "O diário está vazio.")

class AnnyApp:
    def __init__(self, root):
        self.anny = Anny()
        self.root = root
        self.root.title("Anny's Activity Tracker")
        self.root.geometry("400x400")
        self.root.configure(bg="#A020F0")  # Define a cor de fundo para rosa escuro

        self.create_widgets()

    def create_widgets(self):
        # Estilo para os botões
        button_style = {"font": ("Helvetica", 14), "height": 2, "width": 15}

        # Caminho da imagem
        image_path = "anny.png"  # Alterar para o caminho da sua imagem
        if not os.path.isfile(image_path):
            messagebox.showerror("Erro", f"A imagem não foi encontrada no caminho: {image_path}")
            return

        self.img = tk.PhotoImage(file=image_path)
        self.img_label = tk.Label(self.root, image=self.img, bg="#8B0000")  # Define a cor de fundo para rosa escuro
        self.img_label.pack(pady=10)

        self.diario_button = Button(self.root, text="Adicionar ao Diário", command=self.adicionar_diario, **button_style, bg="yellow", fg="black")
        self.diario_button.pack(pady=5)

        self.mostrar_diario_button = Button(self.root, text="Mostrar Diário", command=self.mostrar_diario, **button_style, bg="cyan", fg="black")
        self.mostrar_diario_button.pack(pady=5)

    def adicionar_diario(self):
        entrada = simpledialog.askstring("Diário", "Escreva sua entrada para o diário:")
        if entrada:
            self.anny.adicionar_diario(entrada)
            self.animate_button(self.diario_button)
            messagebox.showinfo("Diário", "Entrada adicionada ao diário.")

    def mostrar_diario(self):
        self.anny.mostrar_diario()

    def animate_button(self, button):
        button.config(relief=tk.SUNKEN)
        self.root.after(200, lambda: button.config(relief=tk.RAISED))

if __name__ == "__main__":
    root = tk.Tk()
    app = AnnyApp(root)
    root.mainloop()
