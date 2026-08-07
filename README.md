# python-particle-system

A simple 2D particle system I built with Python and Pygame. Click anywhere on the screen to spawn a burst of particles that fall with gravity, bounce off the walls and floor, and slowly fade away.

## How it works

- Each particle is stored as a dictionary with its position, speed, color, radius, and remaining "life."
- Every frame, gravity is added to each particle's vertical speed, and its position is updated.
- Particles bounce when they hit the floor or the left/right edges of the screen.
- Once a particle's life reaches 0, it's removed from the list.

## Running it

1. Install Pygame:
   ```
   pip install pygame
   ```
2. Run the script:
   ```
   python particle_system.py
   ```
3. Click anywhere in the window to create particles.

## Why I made this

This was a way for me to practice basic 2D graphics and animation concepts (gravity, collisions, particle life cycles) using Python, building on what I learned in my Computer Graphics coursework.
