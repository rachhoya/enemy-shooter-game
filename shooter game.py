import pgzrun
import random
HEIGHT=600
WIDTH=1200
score=0
ship=Actor("space_ship")
ship.dead=False
ship.pos=(600,550)
speed=5
bullets=[]
enemies=[]
for i in range(5):
    enemy=Actor("enemy")
    enemy.pos=random.randint(50,1150),-50
    enemies.append(enemy)
def on_key_down(key):
    if ship.dead==False:
        if key==keys.UP:
            bullet=Actor("bullet")
            bullet.pos=ship.x,ship.y-30
            bullets.append(bullet)
def update():
    global score
    if ship.dead==False:
        if keyboard.left:
            ship.x-=10
        if keyboard.right:
            ship.x+=10
    for bullet in bullets:
        bullet.y-=10
        if bullet.y<0:
            bullets.remove(bullet)
    for enemy in enemies:
        enemy.y+=5
        if enemy.y>600:
            enemy.y=-50
            enemy.x=random.randint(50,1150)
        for bullet in bullets:
            if enemy.colliderect(bullet):
                bullets.remove(bullet)
                enemy.y=-50
                enemy.x=random.randint(50,1150)
                score=score+10
def draw():
    screen.fill("light blue")
    if ship.dead==False:
        ship.draw()
        for enemy in enemies:
            enemy.draw()
        for bullet in bullets:
            bullet.draw()
pgzrun.go()