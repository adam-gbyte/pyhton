import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Garis Koordinat dengan Pygame")

# Warna
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Loop utama
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Isi layar dengan warna putih
    screen.fill(white)

    # Garis horizontal (sumbu X)
    pygame.draw.line(screen, black, (0, height // 2), (width, height // 2), 2)

    # Garis vertikal (sumbu Y)
    pygame.draw.line(screen, black, (width // 2, 0), (width // 2, height), 2)

    # Menggambar garis tambahan (grid)
    for x in range(0, width, 20):
        pygame.draw.line(screen, blue, (x, 0), (x, height), 1)
    for y in range(0, height, 20):
        pygame.draw.line(screen, blue, (0, y), (width, y), 1)

    # Perbarui layar
    pygame.display.flip()

# Keluar dari Pygame
pygame.quit()
sys.exit()
