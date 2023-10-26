import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


snake = [(5, 5)]
snake_direction = (1, 0)
snake_speed = 10


food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            if event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            if event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            if event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    
    x, y = snake[0]
    x += snake_direction[0]
    y += snake_direction[1]

    
    if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT or (x, y) in snake:
        pygame.quit()
        sys.exit()

    snake.insert(0, (x, y))

    
    if snake[0] == food:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()
        
    screen.fill(WHITE)

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.update()
    
    pygame.time.Clock().tick(snake_speed)
