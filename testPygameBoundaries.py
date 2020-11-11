import sys
import pygame as pg

def main():
    width, height = 640, 480
    hbox, vbox = 20, 20
    screen = pg.display.set_mode((width, height))
    clock = pg.time.Clock()
    rect = pg.Rect(300, 220, hbox, vbox)
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        keys = pg.key.get_pressed()

        # booster
        move = 8 if keys[pg.K_LSHIFT] else 4

        if keys[pg.K_a]:  #to move left
            rect.x -= move
        if rect.x < 0 : rect.x = 0

        if keys[pg.K_d]: #to move right
            rect.x += move
        if rect.x > width-hbox : rect.x = width - hbox

        if keys[pg.K_w]:  #to move up
            rect.y -= move
        if rect.y < 0: rect.y = 0

        if keys[pg.K_s]: #to move down
            rect.y += move
        if rect.y > height - hbox: rect.y = height - vbox

        screen.fill((40, 40, 40))
        pg.draw.rect(screen, (150, 200, 20), rect)

        pg.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
