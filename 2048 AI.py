import pygame
import numpy as np
import random
import tensorflow as tf
from tensorflow.keras.models import load_model

# Constants
BACKGROUND_COLOR = (187, 173, 160)
TEXT_COLOR = (119, 110, 101)
TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}
EMPTY_COLOR = (205, 192, 180)
TILE_SIZE = 100
TILE_MARGIN = 15
FONT_SIZE = 36
ACTION_MAP = {
    0: 'UP',
    1: 'DOWN',
    2: 'LEFT',
    3: 'RIGHT'
}

def init_grid():
    return np.zeros((4, 4), dtype=int)

def add_tile(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2 if random.random() < 0.9 else 4
    return grid

def draw_grid(screen, grid, score):
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font(None, FONT_SIZE)
    for i in range(4):
        for j in range(4):
            value = grid[i][j]
            color = TILE_COLORS.get(value, EMPTY_COLOR)
            pygame.draw.rect(screen, color, ((TILE_SIZE + TILE_MARGIN) * j + TILE_MARGIN,
                                             (TILE_SIZE + TILE_MARGIN) * i + TILE_MARGIN,
                                             TILE_SIZE, TILE_SIZE))
            if value:
                text_surface = font.render(f"{value}", True, TEXT_COLOR)
                text_rect = text_surface.get_rect(center=((TILE_SIZE + TILE_MARGIN) * j + TILE_MARGIN + TILE_SIZE // 2,
                                                          (TILE_SIZE + TILE_MARGIN) * i + TILE_MARGIN + TILE_SIZE // 2))
                screen.blit(text_surface, text_rect)
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (20, 4 * (TILE_SIZE + TILE_MARGIN) + 20))
    pygame.display.update()

def compress(grid):
    new_grid = np.zeros((4, 4), dtype=int)
    done = False
    for i in range(4):
        count = 0
        for j in range(4):
            if grid[i][j] != 0:
                new_grid[i][count] = grid[i][j]
                if j != count:
                    done = True
                count += 1
    return new_grid, done

def merge(grid):
    done = False
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j + 1] = 0
                done = True
    return grid, done

def reverse(grid):
    return np.fliplr(grid)

def transpose(grid):
    return np.transpose(grid)

def move(grid, direction):
    print(direction)
    if direction == 'LEFT':
        grid, done = compress(grid)
        grid, temp = merge(grid)
        done = done or temp
        grid, _ = compress(grid)
    elif direction == 'RIGHT':
        grid = reverse(grid)
        grid, done = compress(grid)
        grid, temp = merge(grid)
        done = done or temp
        grid, _ = compress(grid)
        grid = reverse(grid)
    elif direction == 'UP':
        grid = transpose(grid)
        grid, done = compress(grid)
        grid, temp = merge(grid)
        done = done or temp
        grid, _ = compress(grid)
        grid = transpose(grid)
    elif direction == 'DOWN':
        grid = transpose(grid)
        grid = reverse(grid)
        grid, done = compress(grid)
        grid, temp = merge(grid)
        done = done or temp
        grid, _ = compress(grid)
        grid = reverse(grid)
        grid = transpose(grid)
    return grid, done

def main():
    pygame.init()
    screen = pygame.display.set_mode((4 * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN,
                                      4 * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN + 60))
    pygame.display.set_caption("2048 AI Game")
    
    model = load_model('prod_model.keras')
    grid = init_grid()
    grid = add_tile(grid)
    score = 0
    draw_grid(screen, grid, score)

    # Create a USEREVENT that triggers every 1000 milliseconds (1 second)
    MOVE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVE_EVENT, 1000)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # model the game
                    model = load_model('prod_model.keras')
                    grid = init_grid()
                    grid = add_tile(grid)
                    score = 0
                    draw_grid(screen, grid, score)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        grid, done = move(grid, 'LEFT')
                    elif event.key == pygame.K_RIGHT:
                        grid, done = move(grid, 'RIGHT')
                    elif event.key == pygame.K_UP:
                        grid, done = move(grid, 'UP')
                    elif event.key == pygame.K_DOWN:
                        grid, done = move(grid, 'DOWN')
                    if done:
                        grid = add_tile(grid)
                        score += np.sum(grid[grid >= 2] // 2)  # Simple scoring
                    draw_grid(screen, grid, score)
            if event.type == MOVE_EVENT:
                grid_input = grid.reshape(1, 4, 4, 1)
                # Predict the best move
                print(grid)
                predictions = model.predict(grid_input)
                print(predictions)
                action = np.argmax(predictions[0])
                grid, done = move(grid, ACTION_MAP[action])
                if done:
                    grid = add_tile(grid)
                    score += np.sum(grid[grid >= 2] // 2)  # Simple scoring
                draw_grid(screen, grid, score)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
