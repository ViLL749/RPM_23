import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Лабиринт')

# Определяем цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Загружаем фон
background_image = pygame.image.load('background.jpg')  # Убедитесь, что файл существует
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Параметры игрока
player_radius = 10
player_speed = 5
player_x = screen_width // 2
player_y = screen_height // 2

# Создаем объект Clock для управления FPS
clock = pygame.time.Clock()

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка движения игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Отображение фона
    screen.blit(background_image, (0, 0))

    # Отображение игрока
    pygame.draw.circle(screen, red, (player_x, player_y), player_radius)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS до 60
    clock.tick(60)

# Завершение Pygame
pygame.quit()
