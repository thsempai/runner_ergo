from turtle import back


WIDTH = 800
HEIGHT = 600

GROUND = 458
GRAVITY = 100

N_BG = 2

hero = Actor("hero", anchor=('middle', 'bottom'))
hero.pos = (64, GROUND)
hero_speed = 0

game_speed = 100

backgrounds_bottom = []
backgrounds_top = []

for n in range(N_BG):
    bg_b = Actor("bg_1", anchor=('left', 'top'))
    bg_b.pos = n * WIDTH, 0
    backgrounds_bottom.append(bg_b)

    bg_t = Actor("bg_2", anchor=('left', 'top'))
    bg_t.pos = n * WIDTH, 0
    backgrounds_top.append(bg_t)


def draw():
    screen.clear()

    for bg in backgrounds_bottom:
        bg.draw()

    for bg in backgrounds_top:
        bg.draw()
    hero.draw()


def update(dt):

    # hero update
    global hero_speed

    hero_speed -= GRAVITY * dt
    x, y = hero.pos
    y -= hero_speed * dt

    if y > GROUND:
        y = GROUND
        hero_speed = 0

    hero.pos = x, y

    # bg update

    for bg in backgrounds_bottom:
        x, y = bg.pos
        x -= game_speed * dt
        bg.pos = x, y

    if backgrounds_bottom[0].pos[0] < - WIDTH:
        bg = backgrounds_bottom.pop(0)
        bg.pos = (N_BG - 1) * WIDTH, 0
        backgrounds_bottom.append(bg)

    for bg in backgrounds_top:
        x, y = bg.pos
        x -= game_speed/3 * dt
        bg.pos = x, y

    if backgrounds_top[0].pos[0] < - WIDTH:
        bg = backgrounds_top.pop(0)
        bg.pos = (N_BG - 1) * WIDTH, 0
        backgrounds_top.append(bg)


def on_key_down(key):
    global hero_speed

    if key == keys.SPACE:

        if hero_speed <= 0:
            hero_speed = 200
