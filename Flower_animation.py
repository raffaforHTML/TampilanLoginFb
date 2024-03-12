import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Lebar dan tinggi layar
width, height = 800, 600

# Warna
white = (255, 255, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)

# Inisialisasi layar
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flower Animation")

# Fungsi untuk menggambar bunga
def draw_flower(x, y):
    pygame.draw.circle(screen, yellow, (x, y), 50)  # Pusat bunga
    pygame.draw.circle(screen, white, (x - 30, y - 30), 20)  # Kelopak bunga 1
    pygame.draw.circle(screen, white, (x + 30, y - 30), 20)  # Kelopak bunga 2
    pygame.draw.circle(screen, white, (x - 30, y + 30), 20)  # Kelopak bunga 3
    pygame.draw.circle(screen, white, (x + 30, y + 30), 20)  # Kelopak bunga 4
    pygame.draw.circle(screen, green, (x, y + 80), 30)  # Batang bunga

# Loop utama
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Hapus layar
    screen.fill((0, 0, 0))

    # Mendapatkan posisi mouse
    x, y = pygame.mouse.get_pos()

    # Menggambar bunga pada posisi mouse
    draw_flower(x, y)

    # Update layar
    pygame.display.flip()

    # Menetapkan FPS
    clock.tick(30)
