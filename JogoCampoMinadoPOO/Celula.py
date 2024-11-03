# Classe Celula
class Celula:
    def __init__(self, x, y):
        #posição no tabuleiro
        self.x = x
        self.y = y
        #indica se foi escolhida para ser bomba ou não
        self.eh_bomba = False
        #indica se já foi revelada ou não
        self.revelada = False
        #indica o número de bombas nas células adjacentes
        self.numero_adj = 0

    def revelar(self):
        self.revelada = True

    def marcar_como_bomba(self):
        self.eh_bomba = True

    #chama o contador de bombas adjacentes (classe tabuleiro)
    def definir_numero_adj(self, num):
        self.numero_adj = num