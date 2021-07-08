import ctypes
import pygame


class GUI:
    def __init__(self):
        user32 = ctypes.windll.user32
        self.WIDTH = int(user32.GetSystemMetrics(0) * 0.75)
        self.HEIGHT = int(user32.GetSystemMetrics(1) * 0.75)
        self.FPS = 30

    @classmethod
    def callable(cls):
        obj = cls()
        obj.run()

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        clock = pygame.time.Clock()

        running = True
        while running:
            clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Start rendering
            screen.fill((0, 0, 0))
            # Code here ...
            pygame.display.flip()

        pygame.quit()


GUI.callable()

