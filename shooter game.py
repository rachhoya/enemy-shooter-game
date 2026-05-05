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
bombs=[]
for i in range(5):
    enemy=Actor("enemy")
    enemy.pos=random.randint(50,1150),-50
    enemies.append(enemy)
for i in range(2):
    bomb=Actor("bomb")
    bomb.pos=random.randint(50,1150),-50
    bombs.append(bomb)
def on_key_down(key):
    if ship.dead==False:
        if key==keys.UP:
            bullet=Actor("bullet")
            bullet.pos=ship.x,ship.y-30
            bullets.append(bullet)
def update():
    global score,enemies,bombs
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
                sounds.eep.play()
                bullets.remove(bullet)
                enemy.y=-50
                enemy.x=random.randint(50,1150)
                score=score+10
        if enemy.colliderect(ship):
            sounds.gameover.set_volume(0.5)
            sounds.gameover.play()
            ship.dead=True
            enemies=[]
            bombs=[]
    for bomb in bombs:
        bomb.y+=5
        if bomb.y>600:
            bomb.y=-50
            bomb.x=random.randint(50,1150)
        for bullet in bullets:
            if bomb.colliderect(bullet):
                sounds.gameover.set_volume(0.3)
                sounds.gameover.play()
                ship.dead=True
                enemies=[]
                bombs=[]
        if bomb.colliderect(ship):
            sounds.gameover.set_volume(0.5)
            sounds.gameover.play()
            ship.dead=True
        
def draw():
    screen.fill("orange")
    if ship.dead==False:
        ship.draw()
        for enemy in enemies:
            enemy.draw()
        for bullet in bullets:
            bullet.draw()
        for bomb in bombs:
            bomb.draw()
        screen.draw.text("score:{}".format(score),topleft=(20,20),color="white",fontsize=30)
    else:
        screen.fill("red")
        screen.draw.text("Game Over!\nfinal score:{}".format(score),center=(600,300),color="white",fontsize=50)
pgzrun.go() 
