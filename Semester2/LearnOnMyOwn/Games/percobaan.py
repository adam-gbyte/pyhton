import pygame
import sys

import koordinat

# Inisialisasi pygame
pygame.init()

# Ukuran layar
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Velocity Game')

# Warna
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Posisi dan kecepatan awal objek
x, y = width // 2, height // 2
velocity_x, velocity_y = 0, 0
acceleration = 0.2  # Percepatan untuk mempercepat objek
friction = 0.05     # Gesekan untuk memperlambat objek

# Ukuran objek
object_size = 20

# Kamera
camera_x, camera_y = x - width // 2, y - height // 2

# Loop utama game
running = True
clock = pygame.time.Clock()


while running:
    # Mengatur frame rate
    clock.tick(60)

    # Mengambil input pengguna
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        velocity_x -= acceleration
    if keys[pygame.K_RIGHT]:
        velocity_x += acceleration
    if keys[pygame.K_UP]:
        velocity_y -= acceleration
    if keys[pygame.K_DOWN]:
        velocity_y += acceleration
    # button = koordinat.tombol(velocity_x, velocity_y, acceleration)

    # Menambahkan gesekan
    velocity_x *= (1 - friction)
    velocity_y *= (1 - friction)

    # Memperbarui posisi objek
    x += velocity_x
    y += velocity_y

    # # Memastikan objek tetap di dalam layar
    if x < 0:
        x = 0
        velocity_x = 0
    elif x > width - object_size:
        x = width - object_size
        velocity_x = 0

    if y < 0:
        y = 0
        velocity_y = 0
    elif y > height - object_size:
        y = height - object_size
        velocity_y = 0

    # Memperbarui posisi kamera
    camera_x = x - width // 2
    camera_y = y - height // 2

    screen.fill(white)

    # Menggambar latar belakang dan garis koordinat
    koordinat.garis_koordinat(screen, width, height, 0, 0)

    # Menggambar objek
    koordinat.draw_number(screen, velocity_x, 20, 20)
    koordinat.draw_number(screen, velocity_y, 20, 60)
    koordinat.draw_number(screen, x / object_size, 20, 100)
    koordinat.draw_number(screen, y / object_size, 20, 140)

    pygame.draw.rect(screen, black, (x, y, object_size, object_size))
    # pygame.draw.rect(screen, black, (x - camera_x / 1, y - camera_y / 1, object_size, object_size))
    pygame.display.flip()

# Keluar dari pygame
pygame.quit()
sys.exit()
