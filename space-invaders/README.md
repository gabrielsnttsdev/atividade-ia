# Space Invaders Classico

Jogo inspirado no clássico arcade Space Invaders, desenvolvido em Python com a biblioteca Pygame.

## Tecnologias

- Python 3.x
- Pygame

## Como executar

### 1. Instalar dependências

```bash
pip install pygame
```

### 2. Rodar o jogo

```bash
python main.py
```

## Controles

| Tecla | Acao |
|---|---|
| `←` `→` | Mover nave para esquerda / direita |
| `Espaco` | Atirar |
| `R` | Reiniciar apos Game Over |
| Fechar janela | Sair do jogo |

## Mecanicas

- **Jogador**: nave verde posicionada na base da tela, se move horizontalmente e atira projéteis brancos
- **Inimigos**: 40 inimigos vermelhos distribuídos em 4 linhas x 10 colunas, se movem horizontalmente e descem a cada inversão de direção
- **Colisões**:
  - Tiro acerta inimigo: inimigo é eliminado, +10 pontos
  - Inimigo toca o jogador: -1 vida, inimigos reiniciados
  - Inimigo chega ao fundo da tela: -1 vida, inimigos reiniciados
- **Fases**: ao eliminar todos os inimigos, uma nova onda é criada e +100 pontos são somados
- **Game Over**: quando as 3 vidas se esgotam

## Pontuacao

| Evento | Pontos |
|---|---|
| Inimigo eliminado | +10 |
| Onda completa eliminada | +100 |

## Estrutura do codigo

```
space-invaders/
└── main.py
```

| Classe / Funcao | Responsabilidade |
|---|---|
| `Player` | Sprite do jogador: movimento e disparo |
| `Bullet` | Sprite do projétil: velocidade e remoção ao sair da tela |
| `Enemy` | Sprite do inimigo: movimento horizontal e descida |
| `create_enemies()` | Cria a grade de 4x10 inimigos |
| Loop principal | Entrada, atualização, colisões e renderização a 60 FPS |

## Requisitos do sistema

- Python 3.7 ou superior
- Pygame 2.x ou superior
- Resolucao mínima: 800x600

## Autor

Gabriel Santos — [@gabrielsnttsdev](https://github.com/gabrielsnttsdev)
