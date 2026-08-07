import pygame
import random
import sys

WIDTH, HEIGHT = 800, 600
GRAVITY = 0.15
PARTICLE_COUNT = 150


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-6, -2)
        self.radius = random.randint(2, 5)
        self.color = [random.randint(100, 255) for _ in range(3)]
        self.life = 255

    def update(self):
        self.vy += GRAVITY
        self.x += self.vx
        self.y += self.vy

        if self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            self.vy *= -0.6

        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.vx *= -1

        self.life -= 1.5

    def is_alive(self):
        return self.life > 0

    def draw(self, screen):
        color = (
            max(0, min(255, self.color[0])),
            max(0, min(255, self.color[1])),
            max(0, min(255, self.color[2])),
        )
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Python Particle System")
    clock = pygame.time.Clock()

    particles = []
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for _ in range(PARTICLE_COUNT):
                    particles.append(Particle(mx, my))

        particles = [p for p in particles if p.is_alive()]
        for p in particles:
            p.update()

        screen.fill((15, 15, 25))
        for p in particles:
            p.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
