import pygame
import random
import os

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 64
GAME_DURATION = 30  # Game duration in seconds

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Alphabet Mini-Game")
font = pygame.font.Font(None, FONT_SIZE)

# Load images for each alphabet
def load_images():
    images = {}
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        image_path = f"images/{letter}.jpeg"
        if os.path.exists(image_path):
            images[letter] = pygame.image.load(image_path)
        else:
            print(f"Image for {letter} not found.")
    return images

alphabet_images = load_images()

# Game variables
score = 0
start_time = pygame.time.get_ticks()
current_letter = random.choice(list(alphabet_images.keys()))

# Game loop
running = True
while running:
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    if elapsed_time > GAME_DURATION:
        running = False
        continue

    screen.fill(WHITE)
    screen.blit(alphabet_images[current_letter], (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.upper() == current_letter:
                score += 1
            else:
                score -= 1
            current_letter = random.choice(list(alphabet_images.keys()))

    # Draw the score and timer
    score_text = font.render(f"Score: {score}", True, BLACK)
    time_text = font.render(f"Time: {int(GAME_DURATION - elapsed_time)}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 50))

    pygame.display.flip()

# Display final score
screen.fill(WHITE)
final_score_text = font.render(f"Final Score: {score}", True, BLACK)
screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 32))
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.wait(3000)
pygame.quit()
