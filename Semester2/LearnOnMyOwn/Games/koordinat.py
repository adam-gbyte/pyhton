import pygame

pygame.init()

# Warna
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)


def garis_koordinat(window, w, h, camera_x, camera_y):
    # Garis horizontal (sumbu X)
    pygame.draw.line(window, blue, (0 - camera_x, 0 // 2 - camera_y), (w - camera_x, 0 // 2 - camera_y), 2)

    # Garis vertikal (sumbu Y)
    pygame.draw.line(window, red, (0 // 2 - camera_x, 0 - camera_y), (0 // 2 - camera_x, h - camera_y), 2)

    # Menggambar garis tambahan (grid)
    for x_grid in range(0, w, 20):
        pygame.draw.line(window, red, (x_grid - camera_x, 0 - camera_y), (x_grid - camera_x, h - camera_y), 1)
    for y_grid in range(0, h, 20):
        pygame.draw.line(window, blue, (0 - camera_x, y_grid - camera_y), (w - camera_x, y_grid - camera_y), 1)


# Warna
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 24)  # Gunakan font default dengan ukuran 48


# Fungsi untuk menampilkan angka
def draw_number(window, number, x, y):
    number_text = font.render(str(round(number, 2)), True, black)
    window.blit(number_text, (x, y))
