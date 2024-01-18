import pygame as pg
import sys

size_ventana = (700, 500)
color_fondo = (139,188,210)
color_objeto = (75,20,150)
pos_x = 325
pos_y = 400

pg.init()
ventana = pg.display.set_mode(size = size_ventana)

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                pos_x += 50
            elif event.key == pg.K_LEFT:
                pos_x -= 50
            elif event.key == pg.K_UP:
                pos_y -= 50
            elif event.key == pg.K_DOWN:
                pos_y += 50

    ventana.fill(color_fondo)
    pg.draw.rect(ventana,color_objeto,(pos_x,pos_y,50,50))
    pg.display.update()