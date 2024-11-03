import json

# Classe BancoDeDados
class BancoDeDados:
    def __init__(self, arquivo='ranking.json'):
        # Arquivo JSON onde ficará o ranking
        self.arquivo = arquivo
        # Armazena dados puxados do arquivo
        self.dados = self.carregar_ranking()

    def salvar_pontuacao(self, usuario):
        # Adiciona a pontuação do usuário e ordena para manter apenas o top 5
        self.dados.append({'nome': usuario.nome, 'pontuacao': usuario.pontuacao})
        
        # Ordena o ranking em ordem decrescente e mantém apenas os 5 maiores
        self.dados = sorted(self.dados, key=lambda x: x['pontuacao'], reverse=True)[:5]
        
        # Salva o ranking atualizado no arquivo JSON
        with open(self.arquivo, 'w') as f:
            json.dump(self.dados, f)

    def carregar_ranking(self):
        try:
            with open(self.arquivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def obter_ranking(self):
        # Retorna o ranking ordenado por pontuação em ordem decrescente
        return sorted(self.dados, key=lambda x: x['pontuacao'], reverse=True)
