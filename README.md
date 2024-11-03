# CampoMinadoPOO

Campo Minado em Python
Este é um projeto de Campo Minado desenvolvido em Python, utilizando uma abordagem orientada a objetos e a biblioteca Tkinter para a interface gráfica. O jogo oferece uma experiência de quebra-cabeça com diferentes níveis de dificuldade e mantém um ranking de pontuações dos jogadores.

Funcionalidades
Interface Gráfica com Tkinter: Interface intuitiva que permite ao usuário interagir com o tabuleiro de forma visual.
Níveis de Dificuldade: Três níveis de dificuldade disponíveis: Fácil, Médio e Difícil, cada um com um tabuleiro de tamanho e número de bombas diferentes.
Ranking de Pontuações: Sistema de ranking que salva e exibe as pontuações dos 5 melhores jogadores.
Progressão de Nível: O jogador avança de nível ao completar o tabuleiro atual sem acionar bombas.
Detecção de Bombas e Casas Vazias: O jogo revela automaticamente células adjacentes quando uma célula vazia é aberta.
Estrutura do Projeto
Classes Principais
BancoDeDados: Classe para gerenciamento do ranking de pontuações, salvando e carregando dados de um arquivo JSON.
Celula: Representa cada célula do tabuleiro, armazenando se é uma bomba, se foi revelada, e o número de bombas adjacentes.
Interface: Classe que gerencia a interface do jogo, incluindo a tela inicial, o tabuleiro, e o ranking.
Jogo: Classe principal que gerencia o progresso do jogo, a lógica de avanço de nível e as jogadas do usuário.
Tabuleiro: Responsável pela criação e manipulação do tabuleiro, posicionamento das bombas e revelação das células adjacentes.
Imagens
Tela de Identificação do Usuário

Tela do Jogo - Tabuleiro

Tela de Ranking

Requisitos
Python 3.x
Tkinter (geralmente já incluído nas distribuições Python)
JSON (incluído no Python)
Como Executar
Clone o repositório:
bash
Copiar código
git clone https://github.com/seuusuario/seurepositorio.git
Navegue até o diretório do projeto:
bash
Copiar código
cd campo-minado
Execute o jogo:
bash
Copiar código
python main.py
Como Jogar
Iniciar Jogo: Digite seu nome na tela inicial e clique em "Iniciar".
Selecionar Células: Clique em uma célula no tabuleiro para revelar seu conteúdo.
Se a célula contiver uma bomba, você será movido para o próximo nível (ou o jogo terminará se for o último nível).
Se a célula estiver vazia, as células adjacentes também serão reveladas automaticamente.
Avançar de Nível: Complete cada tabuleiro sem acionar bombas para avançar ao próximo nível.
Consultar Ranking: O ranking com as pontuações dos 5 melhores jogadores pode ser acessado na tela inicial.
Contribuição
Contribuições são bem-vindas! Se você tiver sugestões, sinta-se à vontade para abrir uma issue ou enviar um pull request.
