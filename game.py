
import pygame as p
from sys import exit

# Global Game Settings and Variables
p.init()
game_resolution = (1200, 800)
screen = p.display.set_mode(game_resolution)
p.display.set_caption('Infernum Bound')
clock = p.time.Clock()


# Classes
class Intro(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image_1 = p.image.load('graphics/b_1.png').convert()
        image_1 = p.transform.scale(image_1, game_resolution)
        image_2 = p.image.load('graphics/b_2.png').convert()
        image_2 = p.transform.scale(image_2, game_resolution)
        image_3 = p.image.load('graphics/b_3.png').convert()
        image_3 = p.transform.scale(image_3, game_resolution)
        image_4 = p.image.load('graphics/b_4.png').convert()
        image_4 = p.transform.scale(image_4, game_resolution)
        image_5 = p.image.load('graphics/b_5.png').convert()
        image_5 = p.transform.scale(image_5, game_resolution)
        self.intro_screen = [image_1, image_2, image_3, image_4, image_5]
        self.intro_screen_index = 0
        self.image = self.intro_screen[self.intro_screen_index]
        self.rect = self.image.get_rect(topleft=(0, 0))
        bg_music = p.mixer.Sound('sounds/intro_loop.ogg')
        bg_music.play(loops=-1)

    def animation_state(self):
        keys = p.key.get_pressed()
        if keys[p.K_SPACE]:
            self.intro_screen_index += 1
            self.image = self.intro_screen[self.intro_screen_index]
            p.time.delay(500)
            if self.intro_screen_index == 1:
                p.mixer.Channel(1).play(p.mixer.Sound("sounds/thunder.mp3"))
            elif self.intro_screen_index == 2:
                p.mixer.Channel(1).play(p.mixer.Sound("sounds/wicked_laugh.mp3"))
            elif self.intro_screen_index == 3:
                p.mixer.Channel(1).play(p.mixer.Sound("sounds/opening_door.mp3"))
            elif self.intro_screen_index == 4:
                p.mixer.Channel(1).play(p.mixer.Sound("sounds/closing_door.mp3"))
                self.intro_screen_index = 3

    def update(self):
        self.animation_state()


# Groups
intro = p.sprite.GroupSingle()
intro.add(Intro())

while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            exit()
    # Intro
    intro.draw(screen)
    intro.update()

    p.display.update()
    clock.tick(60)
