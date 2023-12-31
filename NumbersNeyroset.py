import pygame, neyroset, sys
import numpy as np

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
sur = my_font.render("1", (0,0,0), (0,0,0))
texts = [my_font.render("1", (0,0,0), (0,0,0)), my_font.render("1", (0,0,0), (0,0,0)),my_font.render("1", (0,0,0), (0,0,0)), my_font.render("1", (0,0,0), (0,0,0)),my_font.render("1", (0,0,0), (0,0,0)), my_font.render("1", (0,0,0), (0,0,0)),my_font.render("1", (0,0,0), (0,0,0)), my_font.render("1", (0,0,0), (0,0,0)),my_font.render("1", (0,0,0), (0,0,0)), my_font.render("1", (0,0,0), (0,0,0))]

class pixel:
    def __init__(self, x, y):
        self.x = x*20+5
        self.y = y*20+7.5
        self.r = 0
        self.g = 0
        self.b = 0
        self.color = (self.r, self.g, self.b)
    def paint(self, pos):
        if pos[0] <= self.x+20 and pos[0] >= self.x and pos[1] >= self.y and pos[1] <= self.y+20:
            if IsMouseBut[1] == 1 and self.color[0] < 240:
                self.r += 20
                self.g += 20
                self.b += 20
            elif IsMouseBut[1] == 3:
                self.color = (0, 0, 0)
                self.r = 0
                self.b = 0
                self.g = 0
        elif pos[0] <= self.x+40 and pos[0] >= self.x-20 and pos[1] >= self.y-20 and pos[1] <= self.y+40:
            if IsMouseBut[1] == 1 and self.color[0] < 240:
                self.r += 10
                self.g += 10
                self.b += 10
            elif IsMouseBut[1] == 3:
                self.color = (0, 0, 0)
                self.r = 0
                self.b = 0
                self.g = 0


WIDTH = 810
HEIGHT = 570

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Нейросеть - цифры")

win.fill((255, 255, 255))

clock = pygame.time.Clock()

Processing = True
IsMouseBut = [False, 0]


x = 0

pixels = []

img = np.zeros((28, 28))

for i in range(28):
    for k in range(28):
        pixels.append(pixel(i, k))

while Processing:
    win.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Processing = False
            sys.exit() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            IsMouseBut = [True, event.button]
        if event.type == pygame.MOUSEBUTTONUP:
            IsMouseBut = [False, 0]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                for i in pixels:
                    i.color = (0,0,0)
                    i.r = 0
                    i.g = 0
                    i.b = 0
    for i in pixels:
        if IsMouseBut[0]:
            i.paint(event.pos)
        i.color = (i.r, i.g, i.b)
        pygame.draw.rect(win, i.color, (i.x, i.y, 20, 20))
        img[int((i.y-7.5)/20), int((i.x-5)/20)] = i.color[0]/255
    x += 1
    if x > 300:
        x = 0
        for i, prob in enumerate(neyroset.predict_img(img)[1]):
            texts[i] = my_font.render(str(i) + " - " + str(prob*100)[:4] + "%", (255, 255, 255), (0, 0, 0))
    for i in range(10):
        win.blit(texts[i], (570, 10+50*i))
    clock.tick(60)
    pygame.display.update()