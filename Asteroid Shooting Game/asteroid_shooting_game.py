#Joshua Carrillo
#Mr.Davis
#3/7/17
#Adv. Comp. Programming
#Astroid Game 3.2


'''This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>'''

import pygame, sys, random, time, random
from pygame.locals import *
pygame.init()

file = open("highscores.txt", "r+")
Joshua=(file.read())
lol=(file.read())
print(lol)
file.close()

Boom = pygame.mixer.Sound('Explosion.wav')  ##brings in sound
loselife = pygame.mixer.Sound('DeathSound.wav')
laser = pygame.mixer.Sound('laser.wav')
late = pygame.mixer.Sound('LastLive.wav')


class Entity(pygame.sprite.Sprite):
    """Inherited by any object in the game."""

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # This makes a rectangle around the entity, used for anything

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class Asteroid(Entity):
    """
    The Asteroid!  Moves around the screen.
    """

    def __init__(self, x, y, width, height):
        super(Asteroid, self).__init__(x, y, width, height)


        self.image = asteroidIMg

        self.y_direction = 4
        # Positive = down, negative = up
        # Current speed.
        self.speed = 5

    def update(self):
        # Moves the Asteroid
        self.rect.y+=3

class Spaceship(Entity):
    """
    Player controlled or AI controlled, main interaction with
    the game
    """

    def __init__(self, x, y, width, height):
        super(Spaceship, self).__init__(x, y, width, height)

        self.image = spaceshipImg

class Player(Spaceship):
    """The player controlled Paddle"""

    def __init__(self, x, y, width, height):
        super(Player, self).__init__(x, y, width, height)

        # How many pixels the Player Paddle should move on a given frame.
        self.x_change = 0
        # How many pixels the paddle should move each frame a key is pressed.
        self.x_dist = 6

    def MoveKeyDown(self, key):
        """Responds to a key-down event and moves accordingly"""
        if (key == pygame.K_LEFT):
            self.x_change += -self.x_dist
        elif (key == pygame.K_RIGHT):
            self.x_change += self.x_dist
        elif (key == pygame.K_SPACE):
            # Fires a laser bullet if the user presses the spacebar
            bullet = Bullet(player.rect.x+8, player.rect.y-22, 60, 70)
            # Set the laser bullet so it is where the player is
            # Add the laser bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.append(bullet)

    def MoveKeyUp(self, key):
        """Responds to a key-up event and stops movement accordingly"""
        if (key == pygame.K_LEFT):
            self.x_change += self.x_dist
        elif (key == pygame.K_RIGHT):
            self.x_change += -self.x_dist

    def update(self):

        # Moves it relative to its current location.
        self.rect.move_ip(self.x_change, 0)

        # If the paddle moves off the screen, put it back on.
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > window_width - self.width:
            self.rect.x = window_width - self.width

class Bullet(Entity):
    """ This class represents the bullet . """
    def __init__(self,x, y, width, height):
        super(Bullet, self).__init__(x, y, width, height)


        self.image = laserbulletImg
        laser.play()
        self.y_direction = 5
        # Positive = down, negative = up
        # Current speed.
        self.speed = 5
    def update(self):
        # Move the Asteroid!
        #self.rect.move_ip(self.speed * self.x_direction)
        self.rect.y-=18

def Startup():
    global clock
    window_width = 500
    window_height = 700
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((window_width, window_height))
    background = pygame.image.load('stars.png')
    background = pygame.transform.scale(background, (500, 700))

    font2 = pygame.font.SysFont("Lobster", 28)
    #         R    G    B
    WHITE = (255, 255, 255)
    red=(220, 20, 60)
    while True:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and pygame.K_SPACE:
                main()
        end_txt = font2.render("Welcome", 5, WHITE)
        res_txt = font2.render("Asteroid Shooting", 5, WHITE)
        player_scoretxt = font2.render("Please press Space to keep going", 1, WHITE)
        screen.blit(player_scoretxt, (50, 350))  # displays player's high score
        screen.blit(end_txt, (100, 200))
        screen.blit(res_txt, (100, 250))
        pygame.display.flip()


def gameover():
    global pscore
    font2 = pygame.font.SysFont("Lobster", 28)
    #         R    G    B
    WHITE = (255, 255, 255)
    red=(220, 20, 60)
    while True:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        end_txt = font2.render("GAME OVER", 5, red)
        res_txt = font2.render("High Scores", 5, red)
        gameover_txt= font2.render(Joshua + "\n ", 5, red)
        player_scoretxt = font2.render("YOU LOST  Final Score: {0}".format(pscore), 1, red)
        screen.blit(player_scoretxt, (200, 350))  # displays player's high score
        screen.blit(gameover_txt, (0, 275))
        screen.blit(end_txt, (100, 200))
        screen.blit(res_txt, (100, 250))
        pygame.display.flip()
        clock.tick(60)
def check_screen(asteroids,bullets):
    global pscore
    for i in asteroids:
        if i.rect.y+60>=710:
            i.remove(all_sprites_list)
            asteroids.remove(i)
            if pscore==0:
                pscore+=0
            else:
             pscore-=100

    for i in bullets:
        if i.rect.y<=-10:
            i.remove(all_sprites_list)
            bullets.remove(i)

def check_hit(asteroids):
    global plives
    for i in asteroids:
        if i.rect.colliderect(player.rect):
            asteroids.remove(i)
            i.remove(all_sprites_list)
            plives-=1
            screen.blit(background, (0, 0))
            time.sleep(.25)
            loselife.play()
            if plives==0:
                time.sleep(1)
                late.play()
                gameover()
def bullet_hit(asteroids,bullets):
    global pscore
    for i in asteroids:
        for x in bullet_list:
            if i.rect.colliderect(x):
                i.remove(all_sprites_list)
                x.remove(all_sprites_list)
                dice = (random.randint(1, 10))
                Boom.play()

                asteroids.remove(i)
                bullets.remove(x)

                if dice == 4:
                    pscore+=1000000

                pscore+=100
pygame.init()
def main(): #main game function
    global screen,background, bullet_list, all_sprites_list, clock, player, window_height,\
        window_width, asteroidIMg, spaceshipImg, laserbulletImg, pscore, plives
    spaceshipImg= pygame.image.load('Galaga_ship.png')
    spaceshipImg=pygame.transform.scale(spaceshipImg, (60, 60))
    laserbulletImg=pygame.image.load('laser_bullet.png')
    laserbulletImg=pygame.transform.scale(laserbulletImg, (60, 70))

    asteroidIMg=pygame.image.load('asteroid.png')


    asteroidIMg =pygame.transform.scale(asteroidIMg, (65, 65))
    pygame.mixer.music.load('EyeOfTiger.mp3')
    pygame.mixer.music.play(-2, 10.3)
    window_width = 500
    window_height = 700
    screen = pygame.display.set_mode((window_width, window_height))
    background= pygame.image.load('stars.png')
    background= pygame.transform.scale(background, (500, 700))
    pygame.display.set_caption("Laser Shooting'")
    asteroid_list = []
    bullet_list = []
    pscore=0
    plives=3
    level_time=80
    create_astroid_time=level_time
    #         R    G    B
    WHITE = (255, 255, 255)
    font = pygame.font.SysFont("Impact", 20)
    clock = pygame.time.Clock()
    player = Player((window_width / 2)-30, 600, 60, 60)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player)
    # This represents an asteroid
    first_asteroid = Asteroid(random.randrange(window_width-60), 50, 50, 50)
    asteroid_list.append(first_asteroid)
    all_sprites_list.add(first_asteroid)

    while True: #main game loop
        blue = (70, 130, 180)
        screen.blit(background, (0, 0))
        bullet_hit(asteroid_list, bullet_list)
        check_hit(asteroid_list)
        check_screen(asteroid_list, bullet_list)
        if create_astroid_time <= 0:
            x = Asteroid(random.randrange(window_width-60), -10, 50, 50)
            asteroid_list.append(x)
            all_sprites_list.add(x)
            level_time -= .75
            create_astroid_time = level_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
            elif event.type == pygame.KEYUP:
                player.MoveKeyUp(event.key)
        for ent in all_sprites_list:
            ent.update()

        player_scoretxt = font.render("Player Score: {0}".format(pscore), 1, blue)
        player_livestxt = font.render("Lives: {0}".format(plives),1, blue)
        screen.blit(player_scoretxt, (25, 10))
        screen.blit(player_livestxt, (300, 10))
        all_sprites_list.draw(screen)
        create_astroid_time-=.25
        pygame.display.flip()
        clock.tick(60)

Startup()