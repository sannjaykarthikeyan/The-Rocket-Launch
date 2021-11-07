import pygame, sys, time
import timeit

def main():
    main2()
def main2():
    import time
    start_time = time.time()
    pygame.init()
    surface = pygame.display.set_mode([1200, 750])
    pygame.display.set_caption("The Rocket Launch")
    titleX = 300
    titleY = -500
    stars = open("starbackground.png")
    starBKG = pygame.image.load(stars)
    title = open("The Rocket Launch title.png")
    titleImg = pygame.image.load(title)
    earthImg = open("Earth.png")
    imgEarth = pygame.image.load(earthImg)
    moon = open("moon.png")
    moonImg = pygame.image.load(moon)
    rocketRight = open("rocket_rotated_right.png")
    rocket_rotated_right = pygame.image.load(rocketRight)
    scene3 = open("scene3_edited.png")
    scene3_BKG = pygame.image.load(scene3)
    timeSleep = 0
    posX = 387
    posY = 200
    rocketImg = open('Rocket.png')
    imgRocket = pygame.image.load(rocketImg)
    dialogue1 = open("dialogue_full.wav")
    pygame.mixer.music.load(dialogue1)
    pygame.mixer.music.play(0)
    rocketRight_X = 0
    rocketRight_Y = 0
    astronaut = open("astronaut1.png")
    astronaut1 = pygame.image.load(astronaut)
    astronaut2 = open("astronaut2.png")
    astronaut_2 = pygame.image.load(astronaut2)
    scene4 = open("scene4_edited.png")
    scene4_BKG = pygame.image.load(scene4)
    info1 = open("info_1.png")
    info_scene1 = pygame.image.load(info1)
    info2 = open("info_2.png")
    info3 = open("info_3.png")
    info_scene3 = pygame.image.load(info3)
    dialogue1 = open("dialogue_1.png")
    dialogue_1 = pygame.image.load(dialogue1)
    dialogue1_X = 0
    dialogue1_Y = -200
    dialogue2 = open("dialogue_2.png")
    dialogue_2 = pygame.image.load(dialogue2)
    dialogue3 = open("dialogue_3.png")
    dialogue_3 = pygame.image.load(dialogue3)
    dialogue4 = open("dialogue_4.png")
    dialogue_4 = pygame.image.load(dialogue4)
    dialogue5 = open("dialogue_5.png")
    dialogue_5 = pygame.image.load(dialogue5)
    dialogue6 = open("dialogue_6.png")
    dialogue_6 = pygame.image.load(dialogue6)
    dialogue7 = open("dialogue_7.png")
    dialogue_7 = pygame.image.load(dialogue7)
    info_scene2 = pygame.image.load(info2)
    rocketX = 315
    rocketY = -500
    astronaut1_X = 325
    astronaut1_Y = 100
    astronaut2_X = 325
    astronaut2_Y = 100
    dialogue6_X = -100
    dialogue6_Y = 250
    while True:
        seconds = time.time() - start_time
        seconds = int(seconds)
        event = pygame.event.poll()
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            break
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        surface.blit(starBKG, (0, 0))
        pygame.draw.circle(surface, (255, 255, 0), (1200, -50), 350, 0)
        surface.blit(imgEarth, (15, 35))
        surface.blit(titleImg, (titleX, titleY))
        if titleY < 60:
            changeTitleY = 20
            titleY = titleY + changeTitleY
        if seconds == 3:
            time.sleep(2)
        if seconds >= 5 and seconds < 60:
            scene = 1
            if scene == 1:
                timeSleep = 0
                time.sleep(0)
                scene1 = open("scene1_Edited.png")
                scene1_BKG = pygame.image.load(scene1)
                surface.blit(scene1_BKG, (0, 0))
                surface.blit(info_scene1, (-50, -150))
                myFont = pygame.font.SysFont("Arial", 50)
                words = myFont.render("5,", 1, (255, 0, 0))
                surface.blit(words, (475, 635))
                words = myFont.render("4,", 1, (255, 0, 0))
                surface.blit(words, (525, 635))
                words = myFont.render("3,", 1, (255, 0, 0))
                surface.blit(words, (575, 635))
                words = myFont.render("2,", 1, (255, 0, 0))
                surface.blit(words, (625, 635))
                words = myFont.render("1, 0.", 1, (255, 0, 0))
                surface.blit(words, (675, 635))
                words = myFont.render("Ignition, Liftoff!", 1, (255, 0, 0))
                surface.blit(words, (475, 685))
                if seconds >= 11 and seconds < 60:
                    scene = 2
                if scene == 2:
                    changeY = -5
                    posY = posY + changeY
                    posY = posY + changeY
                    posY = posY + changeY
                    if posY < 95:
                        imgRocket = pygame.image.load(open("rocket_blast.png"))
                        posY = posY + changeY
                        posY = posY + changeY
                        posY = posY + changeY
                surface.blit(imgRocket, (posX, posY))
            if seconds >= 16 and seconds < 60:
                scene = 3
            if scene == 3:
                surface.blit(starBKG, (0, 0))
                time.sleep(0)
                pygame.draw.circle(surface, (255, 255, 0), (1200, 900), 315, 0)
                surface.blit(imgEarth, (15, 35))
                surface.blit(info_scene2, (-50, -150))
                surface.blit(moonImg, (900, -100))
                if dialogue1_X < 1200:
                    dialogue1_changeX = 20
                    dialogue1_X = dialogue1_X + dialogue1_changeX
                    dialogue1_X = dialogue1_X + dialogue1_changeX
                surface.blit(dialogue_1, (dialogue1_X, dialogue1_Y))
                if rocketRight_X < 1200:
                    rocketRight_changeX = 20
                    rocketRight_X = rocketRight_X + rocketRight_changeX
                    rocketRight_X = rocketRight_X + rocketRight_changeX
                surface.blit(rocket_rotated_right, (rocketRight_X, rocketRight_Y))
            if seconds >= 24 and seconds < 60:
                scene = 4
            if scene == 4:
                surface.blit(scene3_BKG, (0, 0))
                if rocketY < 75:
                    changeY = 20
                    rocketY = rocketY + changeY
                    rocketY = rocketY + changeY
                surface.blit(info_scene3, (0, 0))
                pygame.draw.circle(surface, (255, 69, 0), (1200, -50), 350, 0)
                imgRocket = pygame.image.load(open("Rocket.png"))
                surface.blit(imgRocket, (rocketX, rocketY))
                if rocketX == 315 and rocketY == 100:
                    surface.blit(astronaut1, (astronaut1_X, astronaut1_Y))
                    surface.blit(astronaut_2, (astronaut2_X, astronaut2_Y))
                    if astronaut1_Y < 230:
                        changeY = 10
                        changeX = 20
                        astronaut1_Y = astronaut1_Y + changeY
                        astronaut1_Y = astronaut1_Y + changeY
                        astronaut1_Y = astronaut1_Y + changeY
                        astronaut1_Y = astronaut1_Y + changeY
                        astronaut1_X = astronaut1_X + changeX
                        astronaut1_X = astronaut1_X + changeX
                    if astronaut1_X == 485:
                        time.sleep(1)
                        surface.blit(dialogue_3, (205, 45))
                    if astronaut2_X == 165:
                        time.sleep(1)
                        surface.blit(dialogue_2, (445, 45))
                    if astronaut2_Y < 230:
                        changeY = 10
                        changeX = -20
                        astronaut2_Y = astronaut2_Y + changeY
                        astronaut2_Y = astronaut2_Y + changeY
                        astronaut2_Y = astronaut2_Y + changeY
                        astronaut2_Y = astronaut2_Y + changeY
                        astronaut2_X = astronaut2_X + changeX
                        astronaut2_X = astronaut2_X + changeX
                    if seconds >= 36 and seconds < 60:
                        scene = 5
                    if scene == 5:
                        surface.blit(scene4_BKG, (0, 0))
                        surface.blit(scene4_BKG, (0, 0))
                        surface.blit(dialogue_4, (0, 0))
                        surface.blit(dialogue_5, (250, 250))
                        if dialogue6_Y < 260:
                            dialogue6_Y += 5
                        surface.blit(dialogue_6, (dialogue6_X, dialogue6_Y))
                        if dialogue6_Y == 260:
                            words = myFont.render("The end!", 1, (0, 0, 0))
                            surface.blit(starBKG, (0, 0))
                            pygame.draw.circle(surface, (255, 255, 0), (1200, -50), 350, 0)
                            pygame.draw.circle(surface, (255, 69, 0), (1200, 900), 315, 0)
                            surface.blit(imgEarth, (15, 35))
                            surface.blit(titleImg, (titleX, titleY))
                            surface.blit(words, (520, 500))
                            time.sleep(2)
                            if 43 <= seconds <= 60:
                                main()
        pygame.display.update()
    time.sleep(timeSleep)


if __name__ == '__main__':
    surface = main()
