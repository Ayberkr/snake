import pygame
import time
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set the window size
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# Set the block size
BLOCK_SIZE = 10

# Set the FPS
FPS = 30

# Initialize Pygame
pygame.init()

# Set the font for the score
FONT = pygame.font.SysFont("comicsansms", 30)

# Set the caption for the window
pygame.display.set_caption("Snake Game")

# Create the game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the clock
clock = pygame.time.Clock()

def draw_snake(snake_block_size, snake_list):
    """Draws the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(game_window, GREEN, [x[0], x[1], snake_block_size, snake_block_size])

def display_score(score):
    """Displays the player's score on the screen."""
    text = FONT.render("Score: " + str(score), True, WHITE)
    game_window.blit(text, [0, 0])

def game_loop():
    """Main game loop."""
    # Set the initial position of the snake
    x = WINDOW_WIDTH / 2
    y = WINDOW_HEIGHT / 2
    
    # Set the initial change in position
    x_change = 0
    y_change = 0

    # Set the initial snake length
    snake_list = []
    snake_length = 1

    # Set the initial food position
    food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    # Set the initial score
    score = 0

    # Set the game over flag
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = BLOCK_SIZE

        # Move the snake
        x += x_change
        y += y_change

        # Check for collision with the window boundaries
        if x >= WINDOW_WIDTH or x < 0 or y >= WINDOW_HEIGHT or y < 0:
            game_over = True

        # Create a new food block if the snake eats the old one
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1
            score += 10
                    # Create the snake head
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        # Remove the old blocks in the snake
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collision with the snake itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True

        # Draw the background and the food block
        game_window.fill(BLACK)
        pygame.draw.rect(game_window, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Draw the snake on the screen
        draw_snake(BLOCK_SIZE, snake_list)

        # Display the player's score on the screen
        display_score(score)

        # Update the game window
        pygame.display.update()

        # Set the FPS
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()

    # Quit the program
    quit()

# Call the game loop function
game_loop()