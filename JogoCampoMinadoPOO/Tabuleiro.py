import random
from Celula import Celula

# Classe Tabuleiro
class Tabuleiro:
    def __init__(self, tamanho, nivel):
        self.tamanho = tamanho
        self.nivel = nivel  # nivel é um inteiro representando o nível atual
        self.grid = [[Celula(x, y) for y in range(tamanho)] for x in range(tamanho)]
        self.celulas_restantes = tamanho * tamanho
        self.inicializar_tabuleiro()
    
    #Posiciona as bombas aleatoriamente
    #Define "num_adjacente" de cada célula vizinha de uma bomba
    def inicializar_tabuleiro(self):
        #Define número de bombas (baseado no nível)
        #Posiciona bombas aleatoriamente -> eh_bomba da Célula vira True
        num_bombas = int((self.tamanho ** 2) * 0.15)
        # Posicionar bombas
        bombas_colocadas = 0
        random.seed(42 + self.nivel)  # Usar self.nivel em vez de self.nivel_atual
        while bombas_colocadas < num_bombas:
            #escolhe celula aleatória do grid
            x = random.randint(0, self.tamanho - 1)
            y = random.randint(0, self.tamanho - 1)
            celula = self.grid[x][y]
            #Se não for bomba, a célula escolhida vira uma
            if not celula.eh_bomba:
                #faz "eh_bomba" dar celula ser True
                celula.marcar_como_bomba()
                bombas_colocadas += 1
                self.celulas_restantes -= 1
                #Coloca bombas até o número definido ser alcançado
                
        #Define "numero_adj" da célula - como faz isso?
        #Usando a função contat_bombas_adjacentes
        for x in range(self.tamanho):
            for y in range(self.tamanho):
                #Passa por cada célula do grid
                celula = self.grid[x][y]
                #Verifica se é bomba. Se não for, usa contar_bombas_adjacentes  
                if not celula.eh_bomba:
                    num_adj = self.contar_bombas_adjacentes(x, y)
                    celula.definir_numero_adj(num_adj)
    
    
    
    #usada no momento de definir "numero_adj" 
    def contar_bombas_adjacentes(self, x, y): #percorre as celulas adjacentes e conta o número de bombas
        direcoes = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)] #casas adjacentes
        #indica o número de bombas nas casas adjacentes
        contador = 0
        #percorrendo as casas adjacentes
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            #verifica se não está "saindo" do tabuleiro
            if 0 <= nx < self.tamanho and 0 <= ny < self.tamanho:
                #se achar uma bomba, adiciona 1 no tabuleiro
                if self.grid[nx][ny].eh_bomba:
                    contador += 1
        return contador

    #verifica se a celula já foi revelada - se já tiver sido, retorna 0
    #se não for, faz "revelada" de celula ser True
    #se for bomba, retorna -1
    #se for celula vazia ("numero_adj" = 0), revela celulas vazias vizinhas
    #se não for bomba e não estiver revelada, retorna numero de celulas reveladas
    def revelar_celula(self, x, y):
        celula = self.grid[x][y]
        if celula.revelada:
            return 0  # Nenhuma nova célula revelada
        celula.revelar()
        total_revelado = 1
        if celula.eh_bomba:
            return -1  # Indica uma bomba
        self.celulas_restantes -= 1
        #importante: se for uma célula vazia revela celulas vazias vizinhas
        if celula.numero_adj == 0:
            total_revelado += self.revelar_celulas_vazias(x, y)
        return total_revelado

    #se uma celula vazia ("numero_adj = 0") for selecionada, ela é chamada
    #percorre celulas vizinhas dessa celula vazia procurando outras celulas sem bombas e as revela
    #uma vez que econtrou uma celula sem bomba, a revela e percorre suas vizinhas também
    def revelar_celulas_vazias(self, x, y):
        total_revelado = 0
        direcoes = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        #percorrendo celulas vizinhas
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            #cuidado para não "sair" do tabuleiro
            if 0 <= nx < self.tamanho and 0 <= ny < self.tamanho:
                vizinho = self.grid[nx][ny]
                #verifica se a celula vizinha ja foi revelada e se é bomba
                if not vizinho.revelada and not vizinho.eh_bomba:
                    vizinho.revelar()
                    self.celulas_restantes -= 1
                    total_revelado += 1
                    if vizinho.numero_adj == 0:
                        total_revelado += self.revelar_celulas_vazias(nx, ny)
        return total_revelado

    def verificar_vitoria(self):
        # Verifica se todas as células não-bomba foram reveladas
        return self.celulas_restantes == 0