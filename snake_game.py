import pygame
import time
import random

pygame.init()

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Display dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Snake parameters
SNAKE_BLOCK_SIZE = 10
SNAKE_SPEED = 15

FONT_STYLE = pygame.font.SysFont("bahnschrift", 25)
SCORE_FONT = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    """Displays the current score on the screen."""
    value = SCORE_FONT.render(f"Your Score: {score}", True, BLACK)
    game_display.blit(value, [0, 0])

def draw_snake(snake_block_size, snake_segments):
    """Draws the snake on the screen."""
    for segment in snake_segments:
        pygame.draw.rect(game_display, GREEN, [segment[0], segment[1], snake_block_size, snake_block_size])

def display_message(message_text, color):
    """Displays a message on the screen."""
    mesg = FONT_STYLE.render(message_text, True, color)
    game_display.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2
    x1_change = 0
    y1_change = 0

    snake_segments = []
    snake_length = 1

    food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK_SIZE) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(BLUE)
            display_message("You Lost! Press Q-Quit or C-Play Again", RED)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()  # Restart the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK_SIZE
                    x1_change = 0

        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_display.fill(BLUE)
        pygame.draw.rect(game_display, YELLOW, [food_x, food_y, SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE])
        snake_head = [x1, y1]
        snake_segments.append(snake_head)

        if len(snake_segments) > snake_length:
            del snake_segments[0]

        for segment in snake_segments[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK_SIZE, snake_segments)
        display_score(snake_length - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

if __name__ == '__main__':
    game_loop()
