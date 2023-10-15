from pygame import *
font.init()

window = display.set_mode((700, 500))
display.set_caption('ping_pong')

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,  player_speed, size1, size2):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size1,  size2))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.x += self.speed
    
    def update_2(self):
       keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < 400:
            self.rect.x += self.speed
    

player = Player('platform.png', 10, 10, 10, 100, 50 )
player_2 = Player('platform.png', 50, 50, 10, 100, 50 )


game = True

while game:
    for e in event.get():
     if e.type == QUIT:
         game = False

    display.update()
    clock.tick(FPS)
