import pygame
import random


pygame.init()


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BALL_SIZE = 20
PLAYER_SIZE = 50
BALL_SPEED = 5
PLAYER_SPEED = 10


WHITE = (255, 255, 255)
RED= (255, 0, 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Ball")

player_x = (SCREEN_WIDTH - PLAYER_SIZE) // 2
player_y = SCREEN_HEIGHT - PLAYER_SIZE
player_speed_x = 0


balls = []


def create_ball():
    ball_x = random.randint(0, SCREEN_WIDTH - BALL_SIZE)
    ball_y = 0
    balls.append((ball_x, ball_y))


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed_x = -PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                player_speed_x = PLAYER_SPEED

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_speed_x = 0

    
    player_x += player_speed_x

    
    if random.random() < 0.1:
        create_ball()

    
    new_balls = []
    for ball in balls:
        ball_x, ball_y = ball
        ball_y += BALL_SPEED
        if ball_y < SCREEN_HEIGHT:
            new_balls.append((ball_x, ball_y))
    balls = new_balls

    
    for ball in balls:
        ball_x, ball_y = ball
        if (
            player_x < ball_x + BALL_SIZE
            and player_x + PLAYER_SIZE > ball_x
            and player_y < ball_y + BALL_SIZE
            and player_y + PLAYER_SIZE > ball_y
        ):
            balls.remove(ball)

    
    screen.fill(WHITE)

    
    pygame.draw.rect(screen, RED, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))

    
    for ball in balls:
        ball_x, ball_y = ball
        pygame.draw.circle(screen, RED, (ball_x + BALL_SIZE // 2, ball_y + BALL_SIZE // 2), BALL_SIZE // 2)

    pygame.display.update()
    clock.tick(60)


pygame.quit()
