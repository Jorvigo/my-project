
from ursina import *

# import everything we need with one line.
app = Ursina()

player = Entity(model='culebra', color=color.orange, scale_y=2, origin = Vec3(0,0,0))
def update():   # update gets automatically called.
    player.x += held_keys['d'] * .1
    player.x -= held_keys['a'] * .1
    player.y += held_keys['w'] * .1
    player.y -= held_keys['s'] * .1

ground = Entity(
    model = 'cube',
    color = color.magenta,
    z = -.1,
    y = -3,
    origin = (0, .5),
    scale = (20, 1, 5),
    collider = 'box'
    )

app.run()