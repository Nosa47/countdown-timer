import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600  # Window size
FONT_SIZE = 300           # Font size for timer
TIMER_START = 1           # Change this value to update the countdown (in minutes)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Countdown Timer")

# Font Setup
font = pygame.font.Font(None, FONT_SIZE)

# Timer Variables
time_left = TIMER_START * 60  # Convert minutes to seconds
running = True  # Timer is running by default

clock = pygame.time.Clock()
last_update_time = time.time()

def draw_text(text, color, y_offset=0):
    """ Helper function to draw centered text """
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + y_offset))
    screen.blit(text_surface, text_rect)

while True:
    screen.fill(BLACK)  # Clear screen

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Press "Spacebar" to pause/unpause
                running = not running

    # Timer Logic
    current_time = time.time()
    if running and time_left > 0:
        if current_time - last_update_time >= 1:  # Only decrease every second
            time_left -= 1
            last_update_time = current_time

    # Display Time
    if time_left > 0:
        minutes = time_left // 60
        seconds = time_left % 60
        timer_text = f"{minutes:02}:{seconds:02}"
        draw_text(timer_text, WHITE)
    else:
        draw_text("TIME UP", WHITE)

    pygame.display.flip()  # Update the screen
    clock.tick(30)  # Run smoothly at 30 FPS
