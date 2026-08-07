import pygame
import random
import sys

# Set up the window
WIDTH = 800
HEIGHT = 600
GRAVITY = 0.2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Particle System")
clock = pygame.time.Clock()

# This list will hold all the particles that are currently on screen.
# Each particle is just a dictionary with a few values instead of a class,
# to keep things simple.
particles = []


def make_particle(x, y):
    particle = {
        "x": x,
        "y": y,
        "vx": random.uniform(-3, 3),
        "vy": random.uniform(-6, -2),
        "radius": random.randint(2, 5),
        "color": (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)),
        "life": 255
    }
    return particle


def update_particle(particle):
    # Gravity pulls the particle down a little bit each frame
    particle["vy"] = particle["vy"] + GRAVITY
    particle["x"] = particle["x"] + particle["vx"]
    particle["y"] = particle["y"] + particle["vy"]

    # Bounce off the bottom of the screen
    if particle["y"] > HEIGHT - particle["radius"]:
        particle["y"] = HEIGHT - particle["radius"]
        particle["vy"] = particle["vy"] * -0.6

    # Bounce off the left and right sides
    if particle["x"] < particle["radius"] or particle["x"] > WIDTH - particle["radius"]:
        particle["vx"] = particle["vx"] * -1

    # Slowly fade out over time
    particle["life"] = particle["life"] - 2


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Create a burst of new particles where the user clicked
            for i in range(100):
                new_particle = make_particle(mouse_x, mouse_y)
                particles.append(new_particle)

    # Update every particle currently on screen
    for particle in particles:
        update_particle(particle)

    # Remove any particles that have completely faded away
    still_alive = []
    for particle in particles:
        if particle["life"] > 0:
            still_alive.append(particle)
    particles = still_alive

    # Draw the background and every particle
    screen.fill((20, 20, 30))
    for particle in particles:
        pygame.draw.circle(
            screen,
            particle["color"],
            (int(particle["x"]), int(particle["y"])),
            particle["radius"]
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
