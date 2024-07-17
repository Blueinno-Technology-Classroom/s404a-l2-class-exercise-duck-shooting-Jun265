import pgzrun
import random


WIDTH = 720
HEIGHT = 480
whiteduck= Actor("duck_outline_white")
whiteduck.x = random.randint(0,WIDTH)
whiteduck.top=random.randint(0,HEIGHT-whiteduck.height)



yellowduck= Actor("duck_outline_yellow")
yellowduck.x = random.randint(0,WIDTH)
yellowduck.top=random.randint(0,HEIGHT-yellowduck.height)


brownduck = Actor("duck_outline_brown")
brownduck.x = random.randint(0,WIDTH)
brownduck.top=random.randint(0,HEIGHT-brownduck.height)


target1 = Actor("target_red1")
target1.x = WIDTH/2
target1.y = HEIGHT/2

target2 = Actor("target_red2")
target2.right = WIDTH
target2.bottom = HEIGHT

def update():
    target1.x +=1
    target2.x -= 1
    brownduck.x +=random.randint(0,10)
    whiteduck.x +=random.randint(0,10)
    yellowduck.x +=random.randint(0,10)

    if target1.left > WIDTH:
        target1.right = 0
        target1.top = random.randint(0,HEIGHT-target1.height)


    if target2.right < 0:
       target2.left = WIDTH
       target2.top = random.randint(0,HEIGHT-target2.height)

    if brownduck.left > WIDTH:
        brownduck.right = 0
        brownduck.top = random.randint(0,HEIGHT-brownduck.height)

    if whiteduck.left > WIDTH:
        whiteduck.right = 0
        whiteduck.top = random.randint(0,HEIGHT-whiteduck.height)

    if yellowduck.left > WIDTH:
        yellowduck.right = 0
        yellowduck.top = random.randint(0,HEIGHT-yellowduck.height)







def draw():
    screen.clear()
    target1.draw()
    target2.draw()
    brownduck.draw()
    yellowduck.draw()
    whiteduck.draw()


    



pgzrun.go()



