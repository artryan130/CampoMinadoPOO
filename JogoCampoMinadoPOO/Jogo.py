from tkinter import messagebox
from BancoDeDados import BancoDeDados
from Tabuleiro import Tabuleiro

# Classe Jogo
class Jogo:
    def __init__(self, usuario, interface):
        self.usuario = usuario
        self.niveis = ['Fácil', 'Médio', 'Difícil']
        self.nivel_atual = 0
        self.config_niveis = {
            'Fácil': 8,
            'Médio': 12,
            'Difícil': 16
        }
        self.tabuleiro = None
        self.interface = interface
        
    #recebe usuario e recebe interface
    def iniciar_jogo(self):
        #zera a pontuação do usuário
        self.usuario.resetar_pontuacao()
        #zera o nível atual
        self.nivel_atual = 0
        self.iniciar_nivel()

    def iniciar_nivel(self):
        #verifica se está no último nível
        if self.nivel_atual < len(self.niveis):
            #se não estiver, cria uma tabuleiro com o tamanho correspondente e inicia tela de jogo
            nivel_nome = self.niveis[self.nivel_atual]
            #obtém o tamanho correspondente do tabuleiro (cada nível tem seu tamanho)
            tamanho = self.config_niveis[nivel_nome]
            self.tabuleiro = Tabuleiro(tamanho, self.nivel_atual)  # Passa o nível atual como inteiro
            # Chama a interface para iniciar o nível
            self.interface.criar_tela_jogo()
            self.interface.atualizar_nivel(nivel_nome)  # Atualiza o nível exibido na interface
        else:
            #se estiver no último nível, finaliza o jogo
            self.finalizar_jogo()

    def processar_jogada(self, x, y):
        #recebe a posição da célula clicada pelo usuário e processa o que vai acontecer
        resultado = self.tabuleiro.revelar_celula(x, y)
        #se revelar_celula retornar -1, quer dizer que uma bomba foi selecionada
        if resultado == -1:
            #quando uma bomba é selecionada, verifica se está no último nível
            #se não estiver, passa para o próximo
            if self.nivel_atual < len(self.niveis) - 1:
                messagebox.showinfo("Bomba!", f"Você encontrou uma bomba! Avançando para o próximo nível.")
                self.nivel_atual += 1
                self.iniciar_nivel()
            #se estiver no último nível, termina o jogo com "finalizar_jogo"
            else:
                messagebox.showinfo("Fim de Jogo", "Você encontrou uma bomba no nível difícil. Fim de jogo.")
                self.finalizar_jogo()
        #se a celula selecionada não for uma bomba (resultado != -1):
        #resultado retornará o número de celulas reveladas na jogada - para atualizar pontuação
        else:
            #atualiza pontuação com o numero de celulas reveladas
            self.usuario.atualizar_pontuacao(resultado)
            #atualiza celulas na interface
            self.interface.atualizar_celulas()
            #verifica vitória com "verificar_vitoria"
            #inicia um novo nível
            if self.tabuleiro.verificar_vitoria():
                messagebox.showinfo("Parabéns", "Você completou o nível!")
                self.nivel_atual += 1
                self.iniciar_nivel()

    def finalizar_jogo(self):
        # Salvar pontuação e retornar à tela de identificação
        banco = BancoDeDados()
        banco.salvar_pontuacao(self.usuario)
        messagebox.showinfo("Fim de Jogo", f"Sua pontuação total foi: {self.usuario.pontuacao}")
        self.interface.criar_tela_identificacao()