import pygame as pg
from Board import *
from setting import *
board = Board(w, h, 200)

pg.init()
screen = pg.display.set_mode((w, h))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.QUIT()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            board.click(event.pos)

    screen.fill("#FFFFFF")
    board.render(screen)
    pg.display.update()

    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        pg.quit()
        exit()


