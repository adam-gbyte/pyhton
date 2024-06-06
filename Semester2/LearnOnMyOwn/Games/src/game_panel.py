import pygame
import sys
import setting
import os

pygame.init()

width, height = 800, 600


def _load_image(file_name):
    # Fungsi untuk memuat gambar dari direktori
    return pygame.image.load(os.path.join("../asset/character/", file_name))


def _load_font(file_name, size):
    # Fungsi untuk memuat font dari direktori
    return pygame.font.Font(os.path.join('../asset/fonts/', file_name), size)


class Game:
    def __init__(self):
        # Ukuran layar
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Velocity Game')

        # Posisi dan kecepatan awal objek
        x, y = width // 2, height // 2
        self.velocity_x, self.velocity_y = 0, 0
        self.acceleration = 0.2  # Percepatan untuk mempercepat objek
        self.friction = 0.05  # Gesekan untuk memperlambat objek

        # Ukuran objek
        self.object_size = 20

        # Kamera
        self.camera_x, self.camera_y = x - width // 2, y - height // 2

        # Loop utama game
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        # Membuat grup sprite
        all_sprites = pygame.sprite.Group()
        sprite = Sprite()
        all_sprites.add(sprite)

        while self.running:
            self.clock.tick(60)

            # Mengambil input pengguna
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            all_sprites.update()

            self.screen.fill(setting.color['white'])

            all_sprites.draw(self.screen)

            # Menampilkan teks
            self._draw_text(self.screen, 'Adam Gumilang', 'Canavar.ttf', 48, setting.color['black'], (100, 100))
            # Menapilkan nomor
            self._draw_number(self.screen, 1253, 'Canavar.ttf', 48, position=(100, 250))
            # Menampilkan gambar
            self._display_image(self.screen, 'player/boy_up_1.png', width=100, height=100, position=(250, 200))

            pygame.display.flip()

        # Keluar dari pygame
        pygame.quit()
        sys.exit()

    @staticmethod
    def _draw_text(window,
                   text: str,
                   font_name,
                   font_size: int,
                   color=(0, 0, 0),
                   position=(10, 10)):
        font = _load_font(font_name, font_size)
        text_surface = font.render(text, True, color)
        window.blit(text_surface, position)

    @staticmethod
    def _draw_number(window,
                     number: int,
                     font_name,
                     font_size=24,
                     color=(0, 0, 0),
                     position=(10, 10)):
        font = _load_font(font_name, font_size)
        number_text = font.render(str(round(number, 2)), True, color)
        window.blit(number_text, position)

    @staticmethod
    def _display_image(window,
                       image_path,
                       position,
                       width=100,
                       height=100):
        image = _load_image(image_path)
        image = pygame.transform.scale(image, (width, height))
        window.blit(image, position)


class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        # Mengambil gambar-gambar sprite dari direktori
        for i in range(1, 3):
            self.images.append(_load_image(f"player/boy_up_{i}.png"))
        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)

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


if __name__ == '__main__':
    g = Game()
    g.run()
