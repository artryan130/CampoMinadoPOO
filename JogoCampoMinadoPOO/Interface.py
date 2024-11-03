import tkinter as tk
from tkinter import messagebox
from BancoDeDados import BancoDeDados
from Usuario import Usuario
from Jogo import Jogo

# Classe Interface
class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Campo Minado")
        self.jogo = None
        self.usuario = None
        self.label_nivel = None  # Rótulo para exibir o nível do jogo

    def criar_tela_identificacao(self):
        # Limpa a tela anterior
        self.limpar_tela()

        #Centralizar o conteúdo
        frame_identificacao = tk.Frame(self.root)
        frame_identificacao.pack(expand=True)

        #Exibir texto
        label_nome = tk.Label(frame_identificacao, text="Digite seu nome:", font=("Arial", 14))
        label_nome.pack(pady=10)  # Adiciona margem superior e inferior

        #Widget para inserir nome
        nome_entry = tk.Entry(frame_identificacao, font=("Arial", 12), justify="center")
        nome_entry.pack(padx=20, pady=10)  # Adiciona margem ao redor

        #Botão para iniciar o jogo
        botao_iniciar = tk.Button(frame_identificacao, text="Iniciar", font=("Arial", 12), command=lambda: self.iniciar_jogo(nome_entry.get()), width=10)
        botao_iniciar.pack(pady=5)  # Adiciona margem inferior

        #Botão para acessar o ranking
        botao_ranking = tk.Button(frame_identificacao, text="Ranking", font=("Arial", 12), command=self.mostrar_ranking, width=10)
        botao_ranking.pack(pady=5)  # Adiciona margem inferior

        # Centraliza o Frame na tela
        frame_identificacao.pack(expand=True)


    def iniciar_jogo(self, nome): #recebe o nome inserido pelo usuário
        #tratamento de erro - caso o nome esteja vazio
        if nome.strip() == '':
            messagebox.showwarning("Aviso", "Por favor, insira um nome.")
            return
        #cria objeto da classe Usuario
        self.usuario = Usuario(nome)
        #cria objeto da classe Jogo
        self.jogo = Jogo(self.usuario, self)
        self.jogo.iniciar_jogo()

    def mostrar_ranking(self):
        self.limpar_tela()
        banco = BancoDeDados()
        ranking = banco.obter_ranking()
        # Ordena o ranking por pontuação de forma decrescente e exibe apenas os 5 primeiros
        ranking_top5 = sorted(ranking, key=lambda item: item['pontuacao'], reverse=True)[:5]

        tk.Label(self.root, text="Ranking de Pontuações - TOP 5").pack()
        for idx, item in enumerate(ranking_top5):
            tk.Label(self.root, text=f"{idx+1}. {item['nome']} - {item['pontuacao']}").pack()
        tk.Button(self.root, text="Voltar", command=self.criar_tela_identificacao).pack()

    def criar_tela_jogo(self):
        self.limpar_tela()


        self.label_nivel = tk.Label(self.root, text=f"Nível: {self.jogo.niveis[self.jogo.nivel_atual]}", font=("Arial", 12))
        self.label_nivel.pack(pady=5)

        # Criando um Frame para conter o tabuleiro
        frame_tabuleiro = tk.Frame(self.root)
        frame_tabuleiro.pack(expand=True)
        
        #obtém o tamanho do tabuleiro a ser criado (interface possui um jogo, jogo possui tabuleiro, que possui tamanho)
        tamanho = self.jogo.tabuleiro.tamanho
        #botoes é uma lista de listas (matriz de tamanho x tamanho)
        self.botoes = [[None for _ in range(tamanho)] for _ in range(tamanho)]

        #Inserindo botões dentro do Frame e centralizando com 'grid'
        #para cada item da matriz botoes, cria uma botão correspondente
        for x in range(tamanho):
            for y in range(tamanho):
                btn = tk.Button(frame_tabuleiro, width=2, height=1)
                btn.config(command=lambda x=x, y=y: self.clicar_celula(x, y))
                btn.grid(row=x, column=y)
                self.botoes[x][y] = btn

        #Centraliza o Frame no root
        frame_tabuleiro.pack(expand=True)


    def clicar_celula(self, x, y):
        #passa a posição da célula e processa a jogada
        self.jogo.processar_jogada(x, y)

    def atualizar_celulas(self):
        tamanho = self.jogo.tabuleiro.tamanho
        for x in range(tamanho):
            for y in range(tamanho):
                celula = self.jogo.tabuleiro.grid[x][y]
                btn = self.botoes[x][y]
                if celula.revelada and not celula.eh_bomba:
                    btn.config(text=str(celula.numero_adj) if celula.numero_adj > 0 else '', bg='lightblue')
                    btn.config(state='disabled')
                elif celula.revelada and celula.eh_bomba:
                    btn.config(text='B', bg='red')
                    btn.config(state='disabled')

    def atualizar_nivel(self, novo_nivel):
        """Atualiza o rótulo do nível com o novo nível."""
        self.label_nivel.config(text=f"Nível: {novo_nivel}")

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def iniciar(self):
        self.criar_tela_identificacao()
        #mantém a janela aberta e ativa
        self.root.mainloop()