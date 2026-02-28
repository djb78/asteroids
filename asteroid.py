import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        rand_angle = random.uniform(20, 50)

        velocity_1 = self.velocity.rotate(rand_angle)
        velocity_2 = self.velocity.rotate(-rand_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        frag_1 = Asteroid(self.position.x, self.position.y, new_radius)
        frag_2 = Asteroid(self.position.x, self.position.y, new_radius)

        frag_1.velocity = velocity_1 * 1.2
        frag_2.velocity = velocity_2 * 1.2
