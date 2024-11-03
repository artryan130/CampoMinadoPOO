# Classe Usuario
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0

    def atualizar_pontuacao(self, pontos):
        self.pontuacao += pontos

    def resetar_pontuacao(self):
        self.pontuacao = 0