def on_button_pressed_a():
    if playermovement == 0:
        player.change(LedSpriteProperty.Y, -1)
    elif playermovement == 1:
        player.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global playermovement
    if playermovement == 1:
        playermovement = 0
    elif playermovement == 0:
        playermovement = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if playermovement == 0:
        player.change(LedSpriteProperty.Y, 1)
    elif playermovement == 1:
        player.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

movement = 0
player: game.LedSprite = None
playermovement = 0
game.start_countdown(60000)
playermovement = 0
enemy = game.create_sprite(2, 2)
player = game.create_sprite(0, 0)
enemy.set(LedSpriteProperty.BRIGHTNESS, 5)

def on_forever():
    global enemy, player
    if player.is_touching(enemy):
        game.add_score(1)
        enemy.delete()
        player.delete()
        enemy = game.create_sprite(2, 2)
        player = game.create_sprite(0, 0)
        enemy.set(LedSpriteProperty.BRIGHTNESS, 5)
basic.forever(on_forever)

def on_forever2():
    global movement
    movement = randint(1, 4)
    if movement == 1:
        enemy.change(LedSpriteProperty.Y, -1)
        enemy.if_on_edge_bounce()
    elif movement == 2:
        enemy.change(LedSpriteProperty.X, 1)
        enemy.if_on_edge_bounce()
    elif movement == 3:
        enemy.change(LedSpriteProperty.Y, 1)
        enemy.if_on_edge_bounce()
    elif movement == 4:
        enemy.change(LedSpriteProperty.X, -1)
        enemy.if_on_edge_bounce()
    basic.pause(200)
basic.forever(on_forever2)
