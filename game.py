import tkinter as tk
from tkinter import messagebox
import random


class JogoAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Adivinhação de Números")
        self.root.configure(bg="#1e1e1e")
        self.root.attributes("-fullscreen", True)

        self.numero_secreto = random.randint(1, 100)
        self.max_tentativas = 10
        self.tentativas = 0

        self.setup_ui()

    def setup_ui(self):
        # Frame principal
        self.frame_principal = tk.Frame(self.root, bg="#1e1e1e")
        self.frame_principal.pack(expand=True, fill=tk.BOTH)

        # Layout Grid
        self.frame_principal.grid_rowconfigure(0, weight=1)
        self.frame_principal.grid_rowconfigure(1, weight=1)
        self.frame_principal.grid_rowconfigure(2, weight=1)
        self.frame_principal.grid_rowconfigure(3, weight=1)
        self.frame_principal.grid_rowconfigure(4, weight=1)

        self.frame_principal.grid_columnconfigure(0, weight=1)

        # Título
        self.titulo = tk.Label(self.frame_principal, text="ADIVINHE O NÚMERO", font=("Arial", 24, "bold"), fg="#ffffff",
                               bg="#1e1e1e")
        self.titulo.grid(row=0, column=0, pady=(100, 20), sticky='nsew')  # Ajusta o espaço acima e abaixo do título

        # Instruções
        self.instrucoes = tk.Label(self.frame_principal,
                                   text=f"Digite um número entre 1 e 100.\nVocê tem {self.max_tentativas} tentativas.",
                                   font=("Arial", 16), fg="#ffffff", bg="#1e1e1e")
        self.instrucoes.grid(row=1, column=0, pady=10, sticky='nsew')

        # Caixa de Entrada
        self.entrada = tk.Entry(self.frame_principal, font=("Arial", 18), width=15, justify='center')
        self.entrada.grid(row=2, column=0, pady=10, sticky='nsew')

        # Botão de Verificação
        self.botao_verificar = tk.Button(self.frame_principal, text="VERIFICAR", font=("Arial", 18, "bold"),
                                         command=self.verificar_palpite, bg="#4CAF50", fg="#ffffff",
                                         activebackground="#45a049")
        self.botao_verificar.grid(row=3, column=0, pady=20, sticky='nsew')

        # Mensagem
        self.mensagem = tk.Label(self.frame_principal, text="", font=("Arial", 16), fg="#ffffff", bg="#1e1e1e")
        self.mensagem.grid(row=4, column=0, pady=10, sticky='nsew')

        # Instruções adicionais
        self.instrucoes_adicionais = tk.Label(self.frame_principal, text="Pressione ESC para sair.", font=("Arial", 12),
                                              fg="#ffffff", bg="#1e1e1e")
        self.instrucoes_adicionais.grid(row=5, column=0, pady=10, sticky='nsew')

        # Bind para tecla ESC
        self.root.bind("<Escape>", self.quit_app)

    def verificar_palpite(self):
        try:
            palpite = int(self.entrada.get())
            if palpite < 1 or palpite > 100:
                self.mostrar_mensagem("O número deve estar entre 1 e 100.")
                return

            self.tentativas += 1

            if palpite < self.numero_secreto:
                self.mostrar_mensagem("O número é maior. Tente novamente.")
            elif palpite > self.numero_secreto:
                self.mostrar_mensagem("O número é menor. Tente novamente.")
            else:
                self.mostrar_mensagem(f"Você acertou o número {self.numero_secreto}!")
                messagebox.showinfo("Parabéns!",
                                    f"Você acertou o número {self.numero_secreto} em {self.tentativas} tentativas!")
                self.resetar_jogo()

            if self.tentativas >= self.max_tentativas and palpite != self.numero_secreto:
                self.mostrar_mensagem(f"Você esgotou todas as tentativas. O número secreto era {self.numero_secreto}.")
                self.resetar_jogo()

        except ValueError:
            self.mostrar_mensagem("Entrada inválida. Por favor, insira um número inteiro.")

    def mostrar_mensagem(self, mensagem):
        self.mensagem.config(text=mensagem)

    def resetar_jogo(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
        self.entrada.delete(0, tk.END)
        self.mensagem.config(text="Digite um número entre 1 e 100.")

    def quit_app(self, event):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = JogoAdivinhacao(root)
    root.mainloop()