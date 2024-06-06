import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 300
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Games')

# Memuat gambar tombol
button_image = pygame.image.load('coin.jpg')
button_rect = button_image.get_rect()
button_rect.topleft = (screen_width // 2 - button_rect.width // 2, screen_height // 2 - button_rect.height // 2)

# Warna latar belakang
background_color = (0, 0, 0)


# Fungsi utama
def main():
    running = True
    coin = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    coin += 1
                    print(f'Balance {coin}')

        screen.fill(background_color)
        screen.blit(button_image, button_rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
