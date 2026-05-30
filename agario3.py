from pygame import *
from math import hypot
from random import randint

class Ball:
    def __init__(self, x, y, radius, color_, speed=0):
        self.speed = speed
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color_

    def move(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.y -= self.speed
        if keys[K_DOWN]:
            self.y += self.speed
        if keys[K_LEFT]:
            self.x -= self.speed
        if keys[K_RIGHT]:
            self.x += self.speed

    def reset(self):
        self.scale = max(0.3, min(50 / self.radius, 1.5))

        player_screen_radius = int(self.radius * self.scale)
        draw.circle(window, self.color, (size[0] // 2, size[1] // 2), player_screen_radius)

    def collide_circle(self, ball2):
        distance = hypot(self.x - ball2.x, self.y - ball2.y)
        return distance < (self.radius + ball2.radius)

init()

size = 1000, 800
window = display.set_mode(size)
display.set_caption('Моя гра')
clock = time.Clock()

bg = image.load("img/img.png")
bg = transform.scale(bg, size)

ball = Ball(300, 300, 25, (255, 100, 255), speed=5)

f = font.Font(None, 25)
running = True
lose = False


cells = [Ball(randint(-2000, 2000), randint(-2000, 2000), 10,
              (randint(50, 220), randint(50, 220), randint(50, 220)))
         for _ in range(300)]




while running:
    for e in event.get():
        if e.type == QUIT:
            running = False


    scale = max(0.3, min(50 / ball.radius, 1.5))
    player_screen_radius = = int(self.radius * scale)
    window.blit(bg, (0, 0))
    to_remove = []
    if cell.colide_circle(ball):
        to_remove.append(cell)
        ball.radius += int(cell.radius * 0.2)
    else:
        sx = int((cell.x - ball.x)*ball.scale + size[0] // 2)
        sy = int((cell.y - ball.y) * ball.scale + size[1] // 2)

        cell_radius = int(cell.radius *.scale)
        draw.circle(window, cell.color, (sx, sy),cell_radius)
for cell in to_remove:
    cells.remove(cell)

    if lose:
        t = f.render('U lose!', 1, (244, 0, 0)0
        window.blit(t, (400, 500))

    display.update()
    clock.tick()

    ball.move()
    ball.reset()

    display.update()
    clock.tick(60)