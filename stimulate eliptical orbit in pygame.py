import math
import random
import pygame
class Particle ():
def __init__ (self, x, y, colour=0x000000):
self.x = x
self.y = y
self.vx = 0
self.vy = 0
self.colour = colour
def apply_gravity (self, target):
dsqd = (self.x - target.x) ** 2 + (self.y - target.y) ** 2
#g = G*m/dsqd * normalized (self - target)
if dsqd == 0:
return
self.vx += -1 / dsqd * (self.x - target.x) / dsqd ** 0.5
self.vy += -1 / dsqd * (self.y - target.y) / dsqd ** 0.5
def update (self):
self.x += self.vx
self.y += self.vy
pygame.init()
window = pygame.display.set_mode ((600, 400))
main_surface = pygame.Surface ((600, 400))
colours = [0x000000, 0x111111, 0x222222, 0x333333,
0x444444,0x555555, 0x666666, 0x777777, 0x888888, 0x999999,
0xaaaaaa, 0xbbbbbb] + [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00,
0xFF00FF, 0x00FFFF, 0x888888, 0xFFFFFF, 0x808000, 0x008080,
0x800080, 0x800000]
particles = [Particle (200, 100, colours [i]) for i in range (20)]
earth = Particle (200, 200)

71

for i, p in enumerate (particles):
p.vx = i / 100
while (True):
#main_surface.fill(0x000000)
pygame.draw.circle (main_surface, 0x00FF00, (earth.x, earth.y),
5, 2)

for p in particles:
p.apply_gravity (earth)
p.update ()
spygame.draw.circle (main_surface, p.colour, (int (p.x), int (p.y)),
5, 2)
window.blit(main_surface, (0,0))
pygame.disply.flip()
