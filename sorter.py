import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (100, 149, 237)
RED = (255, 69, 0)

# Sorting Algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw_array(arr, j, j+1)
                yield True

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_array(arr, i, min_idx)
        yield True

# Draw array
def draw_array(arr, colorA=None, colorB=None):
    WIN.fill(BLACK)
    bar_width = WIDTH // len(arr)
    for i, value in enumerate(arr):
        color = BLUE
        if i == colorA:
            color = RED
        elif i == colorB:
            color = WHITE
        pygame.draw.rect(WIN, color, (i * bar_width, HEIGHT - value, bar_width, value))
    pygame.display.update()

# Main loop
def main():
    running = True
    sorting = False
    array = [random.randint(10, HEIGHT - 10) for _ in range(50)]
    sort_algo = bubble_sort(array)
    algo_name = "Bubble Sort"
    
    while running:
        draw_array(array)
        if sorting:
            try:
                next(sort_algo)
            except StopIteration:
                sorting = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not sorting:
                    sorting = True
                    sort_algo = bubble_sort(array)
                if event.key == pygame.K_s and not sorting:
                    sorting = True
                    sort_algo = selection_sort(array)
                    algo_name = "Selection Sort"

    pygame.quit()

if __name__ == "__main__":
    main()
