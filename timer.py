import pygame
import sys
import time
import json
import threading
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600  # Window size
FONT_SIZE = 300           # Font size for timer
CONFIG_FILE = "config.json"  # File to store timer value

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)  # Red background for "TIME UP"

# Initialize Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Countdown Timer")

# Font Setup
font = pygame.font.Font(None, FONT_SIZE)

# Load Timer from Config
def load_timer():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)["TIMER_START"] * 60  # Convert minutes to seconds
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        return 60  # Default to 1 minute if config is missing or invalid

time_left = load_timer()
running = True  # Timer is running by default

clock = pygame.time.Clock()
last_update_time = time.time()
last_modified = os.path.getmtime(CONFIG_FILE)

# Blinking Variables
blink_timer = 0
blink_visible = True  # Controls the visibility of "TIME UP"

# Watch for Config Changes
def check_config_update():
    global time_left, last_modified
    while True:
        try:
            modified_time = os.path.getmtime(CONFIG_FILE)
            if modified_time != last_modified:
                last_modified = modified_time
                new_time = load_timer()
                if new_time != time_left:  # Update only if the time changed
                    time_left = new_time
                    print(f"Timer updated: {time_left} seconds remaining")
        except Exception as e:
            print("Error checking config:", e)
        time.sleep(1)

# Start file monitoring in a separate thread
threading.Thread(target=check_config_update, daemon=True).start()

# Function to Draw Text
def draw_text(text, color, y_offset=0):
    """ Helper function to draw centered text """
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + y_offset))
    screen.blit(text_surface, text_rect)

# Main Loop
while True:
    screen.fill(BLACK if time_left > 0 else RED)  # Change background when "TIME UP"

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Press "Spacebar" to pause/unpause
                running = not running
            elif event.key == pygame.K_r:  # Press "R" to reset the timer
                time_left = load_timer()  # Reload from config
                running = True  # Resume automatically after reset
                blink_visible = True  # Reset blinking effect

    # Timer Logic
    current_time = time.time()
    if running and time_left > 0:
        if current_time - last_update_time >= 1:  # Only decrease every second
            time_left -= 1
            last_update_time = current_time

    # Blinking Effect Logic
    if time_left == 0:
        if current_time - blink_timer >= 0.3:  # Toggle visibility every 0.5 seconds
            blink_visible = not blink_visible
            blink_timer = current_time

    # Display Time or Blinking "TIME UP"
    if time_left > 0:
        minutes = time_left // 60
        seconds = time_left % 60
        draw_text(f"{minutes:02}:{seconds:02}", WHITE)
    else:
        if blink_visible:  # Show "TIME UP" only when blink_visible is True
            draw_text("TIME UP", WHITE)

    pygame.display.flip()  # Update the screen
    clock.tick(30)  # Run smoothly at 30 FPS
