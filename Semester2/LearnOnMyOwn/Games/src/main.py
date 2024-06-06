import pygame
import os

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Animation")

# Warna
WHITE = (255, 255, 255)


# Fungsi untuk memuat gambar dari direktori
def load_image(file_name):
    return pygame.image.load(os.path.join("../asset/character/player/", file_name))


# Kelas Sprite
class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.images = []
        # Mengambil gambar-gambar sprite dari direktori
        for i in range(1, 3):
            print(i)
            self.images.append(load_image(f"boy_up_{i}.png"))

        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.animation_speed = 0.2
        self.last_update = pygame.time.get_ticks()

    def update(self):
        # Mengatur kecepatan animasi
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:
            self.last_update = now
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]


# Fungsi utama
def main():
    # Inisialisasi Pygame
    pygame.init()

    # Mengatur font
    font = pygame.font.SysFont(None, 36)

    # Membuat objek sprite
    sprite = Sprite()

    # Grup semua sprite
    all_sprites = pygame.sprite.Group()
    all_sprites.add(sprite)

    # Variabel kontrol game loop
    running = True

    # Game Loop
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        all_sprites.update()

        # Rendering
        SCREEN.fill(WHITE)
        all_sprites.draw(SCREEN)

        # Update layar
        pygame.display.flip()

    # Quit
    pygame.quit()


if __name__ == "__main__":
    main()

