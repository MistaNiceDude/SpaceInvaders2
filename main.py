import pygame
import time
from pygame import key


pygame.init()
window = WIDTH, HEIGHT = (600,900)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(window)
bg = pygame.image.load('sprites/spacebg.jpeg')
ship = pygame.image.load('sprites/Spaceship.png')
red_laser = pygame.image.load('sprites/red_laser.png')

running = True
pygame.display.set_caption('Invaders')

FPS = 60
spaceship = ship.get_rect()
spaceship_center = (window[0] / 2, window[1] / 2)
spaceship.x = spaceship_center[0]
spaceship.y = spaceship_center[1]
ship_laser = red_laser.get_rect()

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, HEIGHT):
        return not(self.y <= HEIGHT and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)


class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health, img,):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = img
        self.rect = self.ship_img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lasers = []
        self.cool_down_counter = 0
        self.vel = 10


    def draw(self,window):
        window.blit(self.self_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        self.lasers.append(Laser(self.x, self.y, red_laser))

    def update(self, window):
        self.draw(window)

    def move(self):
        x_vel = 0
        y_vel = 0
        if key.get_pressed()[pygame.K_a]:
            x_vel = -self.vel
        elif key.get_pressed()[pygame.K_d]:
            x_vel = self.vel
        if key.get_pressed()[pygame.K_w]:
            y_vel = -self.vel
        if key.get_pressed()[pygame.K_s]:
            y_vel = self.vel



#def collide(obj1, obj2):
    #offset_x = obj2.x - obj1.x
    #offset_y = obj2.y - obj1.y
    #return obj.1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
Player_ship = Ship(spaceship_center[0], spaceship_center[1], 100,ship)


#def redlaser():
    #screen.blit(ship_laser)

#main game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # controls

    # movement boundaries
    if spaceship.left < 0:
        spaceship.left = 0
    elif spaceship.right > WIDTH:
        spaceship.right = WIDTH
    if spaceship.top < HEIGHT/2:
        spaceship.top = HEIGHT/2
    elif spaceship.bottom > HEIGHT:
        spaceship.bottom = HEIGHT

    #laser
    #if key.get_pressed()[pygame.K_SPACE]:











    screen.blit(bg, (0, 0))
    screen.blit(ship, spaceship)
    #screen.blit(red_laser)
    pygame.display.flip()
    clock.tick(FPS)


