import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da Tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders Clássico")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonte
font = pygame.font.SysFont("Courier", 24)
large_font = pygame.font.SysFont("Courier", 48)

# FPS
clock = pygame.time.Clock()
FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = -5
        if keys[pygame.K_RIGHT]:
            self.speedx = 5

        self.rect.x += self.speedx

        # Limites da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -7

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 2

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.speedx = -self.speedx
            self.rect.y += 30 # Desce quando bate na borda

# Grupos de sprites
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Criação do jogador
player = Player()
all_sprites.add(player)

# Criação dos inimigos
def create_enemies():
    for row in range(4):
        for col in range(10):
            enemy = Enemy(50 + col * 60, 50 + row * 40)
            all_sprites.add(enemy)
            enemies.add(enemy)

create_enemies()

# Variáveis do jogo
score = 0
lives = 3
game_over = False

# Loop principal
running = True
while running:
    # 1. Processamento de eventos (Input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                player.shoot()
            elif event.key == pygame.K_r and game_over:
                # Reiniciar jogo
                game_over = False
                score = 0
                lives = 3
                for enemy in enemies:
                    enemy.kill()
                for bullet in bullets:
                    bullet.kill()
                create_enemies()
                player.rect.centerx = WIDTH // 2

    if not game_over:
        # 2. Atualização
        all_sprites.update()

        # Verifica colisão: tiro acerta inimigo
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            score += 10
        
        # Verifica se todos inimigos foram mortos (próxima fase)
        if len(enemies) == 0:
            create_enemies()
            score += 100

        # Verifica colisão: inimigo acerta jogador ou chega no fundo
        for enemy in enemies:
            if enemy.rect.bottom >= HEIGHT:
                lives -= 1
                for e in enemies:
                    e.kill()
                if lives > 0:
                    create_enemies()
                break

        hits = pygame.sprite.spritecollide(player, enemies, False)
        if hits:
            lives -= 1
            for enemy in enemies:
                enemy.kill()
            if lives > 0:
                create_enemies()
        
        if lives <= 0:
            game_over = True

    # 3. Desenho / Renderização
    screen.fill(BLACK)
    
    all_sprites.draw(screen)

    # UI (Score e Vidas)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(lives_text, (WIDTH - 120, 10))

    if game_over:
        go_text = large_font.render("GAME OVER", True, RED)
        restart_text = font.render("Pressione 'R' para reiniciar", True, WHITE)
        screen.blit(go_text, (WIDTH//2 - go_text.get_width()//2, HEIGHT//2 - 50))
        screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 20))

    pygame.display.flip()
    
    # Mantém o FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()
