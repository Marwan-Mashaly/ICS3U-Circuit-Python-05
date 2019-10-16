# /usr/bin/env python3

# Created by: Marwan Mashaly
# Created on: September 2019
# This programs draws

import ugame
import stage
import Constants


def main():
    # this function sets the scene
    # an image bank for circuitpython
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
    # a list of sprites that will be updated every frame
    sprites = []

    ship = stage.Sprite(image_bank_1, 5, int(Constants.SCREEN_X / 2
                        - Constants.SPRITE_SIZE / 2),
                        int(Constants.SCREEN_Y - Constants.SPRITE_SIZE
                        + Constants.SPRITE_SIZE / 2))
    sprites.append(ship)  # insert at the top of the sprite list

    # sets the background to image 0 in the bank
    # backgrounds do not have magents as a transparent color
    background = stage.Grid(image_bank_1, 10, 8)
    # create a sprite
    # parameters (image_bank, image # in bank, x, y)
    alien = stage.Sprite(image_bank_1, 8, 64, 56)
    sprites.append(alien)

    # create a stage for the background to show up on
    #  and set the frame rate to 60
    game = stage.Stage(ugame.display, Constants.FPS)
    # set the layers, items show up in order
    game.layers = sprites + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, or you turn it off
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # update_game_logic
        # move ship to the right and the left
        if keys & ugame.K_RIGHT != 0:
            if ship.x > Constants.SCREEN_X - Constants.SPRITE_SIZE:
                ship.move(Constants.SCREEN_X - Constants.SPRITE_SIZE, ship.y)
            else:
                ship.move(ship.x + 1, ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x < 0:
                ship.move(0, ship.y)
            else:
                ship.move(ship.x - 1, ship.y)
            pass
        # move ship up and down
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        elif keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
            pass
        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    main()
