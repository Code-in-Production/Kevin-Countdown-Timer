import time
from datetime import timedelta

import sys, pygame

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize pygame window
pygame.init()
size = width, height = 400, 200
screen = pygame.display.set_mode(size)

def show_text(text):
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 24)
    img = font.render(text, True, WHITE)
    mid1, mid2 = img.get_rect()[2]//2, img.get_rect()[3]//2
    screen.blit(img, (200-mid1, 100-mid2))
    pygame.display.update()

hr, mi, si = list(map(int, input().split(":")))

timer = timedelta(
    hours = hr,
    minutes = mi,
    seconds = si
)
second = timedelta(seconds=1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if timer.total_seconds() > 0:
        print(timer)
        show_text(str(timer))
        timer -= second
        time.sleep(1)
    else:
        show_text("Time is up!")
