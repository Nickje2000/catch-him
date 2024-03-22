input.onButtonPressed(Button.A, function () {
    if (playermovement == 0) {
        player.change(LedSpriteProperty.Y, -1)
    } else if (playermovement == 1) {
        player.change(LedSpriteProperty.X, -1)
    }
})
input.onButtonPressed(Button.AB, function () {
    if (playermovement == 1) {
        playermovement = 0
    } else if (playermovement == 0) {
        playermovement = 1
    }
})
input.onButtonPressed(Button.B, function () {
    if (playermovement == 0) {
        player.change(LedSpriteProperty.Y, 1)
    } else if (playermovement == 1) {
        player.change(LedSpriteProperty.X, 1)
    }
})
let movement = 0
let player: game.LedSprite = null
let playermovement = 0
game.startCountdown(60000)
playermovement = 0
let enemy = game.createSprite(2, 2)
player = game.createSprite(0, 0)
enemy.set(LedSpriteProperty.Brightness, 5)
basic.forever(function () {
    if (player.isTouching(enemy)) {
        game.addScore(1)
        enemy.delete()
        player.delete()
        enemy = game.createSprite(2, 2)
        player = game.createSprite(0, 0)
        enemy.set(LedSpriteProperty.Brightness, 5)
    }
})
basic.forever(function () {
    movement = randint(1, 4)
    if (movement == 1) {
        enemy.change(LedSpriteProperty.Y, -1)
        enemy.ifOnEdgeBounce()
    } else if (movement == 2) {
        enemy.change(LedSpriteProperty.X, 1)
        enemy.ifOnEdgeBounce()
    } else if (movement == 3) {
        enemy.change(LedSpriteProperty.Y, 1)
        enemy.ifOnEdgeBounce()
    } else if (movement == 4) {
        enemy.change(LedSpriteProperty.X, -1)
        enemy.ifOnEdgeBounce()
    }
    basic.pause(200)
})
