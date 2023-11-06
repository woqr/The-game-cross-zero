from pygame import *
init()
screen=display.set_mode((726,588))
display.set_caption('Cross-Zero')
icon=image.load('icon/icon.png')#иконка в окне приложения
back=image.load('icon/back.jpg')#задний фон
cross=[image.load('icon/cross/1.png'),image.load('icon/cross/2.png'),image.load('icon/cross/3.png'),image.load('icon/cross/4.png'),\
       image.load('icon/cross/5.png'),image.load('icon/cross/6.png'),image.load('icon/cross/7.png'),image.load('icon/cross/8.png')]
zero=[image.load('icon/zero/1.png'),image.load('icon/zero/2.png'),image.load('icon/zero/3.png'),image.load('icon/zero/4.png'),\
      image.load('icon/zero/5.png'),image.load('icon/zero/6.png'),image.load('icon/zero/7.png'),image.load('icon/zero/8.png')]
lines=[[(304,119),(304,468)],[(420,119),(420,468)],[(188,235),(537,235)],[(188,351),(537,351)]]
display.set_icon(icon)
sqrt=Rect(600//2,400//2,350,350)#поле
sqrt.center=(726//2,588//2)
fonti=font.Font('font/SaarSPDemo.otf',30)
byFruMix=fonti.render('by FruMix',True,'blue')
restart=fonti.render('Играть снова', True, 'black')
restart_rect=restart.get_rect(center=(726//2,588//2))
running=True
gameplay=True
sqrt1,sqrt2,sqrt3,sqrt4,sqrt5,sqrt6,sqrt7,sqrt8,sqrt9=False,False,False,False,False,False,False,False,False
for_cross1,for_cross2,for_cross3,for_cross4,for_cross5,for_cross6,for_cross7,for_cross8,for_cross9=False,False,False,False,False,False,False,False,False
for_zero1,for_zero2,for_zero3,for_zero4,for_zero5,for_zero6,for_zero7,for_zero8,for_zero9=False,False,False,False,False,False,False,False,False
count_sqrt1,count_sqrt2,count_sqrt3,count_sqrt4,count_sqrt5,count_sqrt6,count_sqrt7,count_sqrt8,count_sqrt9=0,0,0,0,0,0,0,0,0
queue=0
clock=time.Clock()
while running:
    if gameplay:
        screen.blit(back,(0,0))#задний фон
        draw.rect(screen,'red',sqrt,10,5)#Вывод квадрата
        for n in lines:
            draw.line(screen,'red',n[0],n[1],10)
        screen.blit(byFruMix,(490,10))
        for events in event.get():
            if events.type==QUIT:
                quit()
                running=False
            #1 sqrt
            if sqrt1:
                pass
            elif 199 < mouse.get_pos()[0] < 299 and 130 < mouse.get_pos()[1] < 230 and events.type == MOUSEBUTTONDOWN:
                sqrt1= True
                queue+=1
            #2 sqrt
            if sqrt2:
                pass
            elif 315 < mouse.get_pos()[0] < 415 and 130 < mouse.get_pos()[1] < 230 and events.type == MOUSEBUTTONDOWN:
                sqrt2 = True
                queue += 1
            #3 sqrt
            if sqrt3:
                pass
            elif 426 < mouse.get_pos()[0] < 531 and 130 < mouse.get_pos()[1] < 230 and events.type == MOUSEBUTTONDOWN:
                sqrt3 = True
                queue += 1
            #4 sqrt
            if sqrt4:
                pass
            elif 199 < mouse.get_pos()[0] < 299 and 246 < mouse.get_pos()[1] < 346 and events.type == MOUSEBUTTONDOWN:
                sqrt4 = True
                queue += 1
            #5 sqrt
            if sqrt5:
                pass
            elif 315 < mouse.get_pos()[0] < 415 and 246 < mouse.get_pos()[1] < 346 and events.type == MOUSEBUTTONDOWN:
                sqrt5 = True
                queue += 1
            #6 sqrt
            if sqrt6:
                pass
            elif 426 < mouse.get_pos()[0] < 531 and 246 < mouse.get_pos()[1] < 346 and events.type == MOUSEBUTTONDOWN:
                sqrt6 = True
                queue += 1
            #7 sqrt
            if sqrt7:
                pass
            elif 199 < mouse.get_pos()[0] < 299 and 362 < mouse.get_pos()[1] < 462 and events.type == MOUSEBUTTONDOWN:
                sqrt7 = True
                queue += 1
            #8 sqrt
            if sqrt8:
                pass
            elif 315 < mouse.get_pos()[0] < 415 and 362 < mouse.get_pos()[1] < 462 and events.type == MOUSEBUTTONDOWN:
                sqrt8 = True
                queue += 1
            #9 sqrt
            if sqrt9:
                pass
            elif 426 < mouse.get_pos()[0] < 531 and 362 < mouse.get_pos()[1] < 462 and events.type == MOUSEBUTTONDOWN:
                sqrt9 = True
                queue += 1
        if count_sqrt1==len(cross):
            if for_cross1:
                screen.blit(cross[-1],cross[-1].get_rect(center=(249,180)))
            else:
                screen.blit(zero[-1], zero[-1].get_rect(center=(249, 180)))
        elif sqrt1:
            if for_cross1 or (queue!=0 and queue%2!=0):
                screen.blit(cross[count_sqrt1],cross[count_sqrt1].get_rect(center=(249,180)))
                count_sqrt1+=1
                for_cross1=True
            else:
                screen.blit(zero[count_sqrt1],zero[count_sqrt1].get_rect(center=(249,180)))
                count_sqrt1 += 1
                for_zero1=True
        if count_sqrt2==len(cross):
            if for_cross2:
                screen.blit(cross[-1],cross[-1].get_rect(center=(363,180)))
            else:
                screen.blit(zero[-1], zero[-1].get_rect(center=(363, 180)))
        elif sqrt2:
            if for_cross2 or (queue!=0 and queue%2!=0):
                screen.blit(cross[count_sqrt2],cross[count_sqrt2].get_rect(center=(363,180)))
                count_sqrt2+=1
                for_cross2=True
            else:
                screen.blit(zero[count_sqrt2], zero[count_sqrt2].get_rect(center=(363, 180)))
                count_sqrt2 += 1
                for_zero2=True
        if count_sqrt3==len(cross):
            if for_cross3:
                screen.blit(cross[-1],cross[-1].get_rect(center=(477,180)))
            else:
                screen.blit(zero[-1], zero[-1].get_rect(center=(477, 180)))
        elif sqrt3:
            if for_cross3 or (queue!=0 and queue%2!=0):
                screen.blit(cross[count_sqrt3],cross[count_sqrt3].get_rect(center=(477,180)))
                count_sqrt3+=1
                for_cross3=True
            else:
                screen.blit(zero[count_sqrt3], zero[count_sqrt3].get_rect(center=(477,180)))
                count_sqrt3 += 1
                for_zero3=True
        if count_sqrt4==len(cross):
            if for_cross4:
                screen.blit(cross[-1],cross[-1].get_rect(center=(249,294)))
            else:
                screen.blit(zero[-1], zero[-1].get_rect(center=(249, 294)))
        elif sqrt4:
            if for_cross4 or (queue != 0 and queue % 2 != 0):
                screen.blit(cross[count_sqrt4],cross[count_sqrt4].get_rect(center=(249,294)))
                count_sqrt4+=1
                for_cross4=True
            else:
                screen.blit(zero[count_sqrt4], zero[count_sqrt4].get_rect(center=(249, 294)))
                count_sqrt4 += 1
                for_zero4=True
        if count_sqrt5==len(cross):
            if for_cross5:
                screen.blit(cross[-1],cross[-1].get_rect(center=(363,294)))
            else:
                screen.blit(zero[-1], zero[-1].get_rect(center=(363, 294)))
        elif sqrt5:
            if for_cross5 or (queue != 0 and queue % 2 != 0):
                screen.blit(cross[count_sqrt5],cross[count_sqrt5].get_rect(center=(363,294)))
                count_sqrt5+=1
                for_cross5=True
            else:
                screen.blit(zero[count_sqrt5], zero[count_sqrt5].get_rect(center=(363, 294)))
                count_sqrt5+=1
                for_zero5=True
        if count_sqrt6==len(cross):
            if for_cross6:
                screen.blit(cross[-1],cross[-1].get_rect(center=(477,294)))
            else:
                screen.blit(zero[-1], zero[-1].get_rect(center=(477,294)))
        elif sqrt6:
            if for_cross6 or (queue != 0 and queue % 2 != 0):
                screen.blit(cross[count_sqrt6],cross[count_sqrt6].get_rect(center=(477,294)))
                count_sqrt6+=1
                for_cross6=True
            else:
                screen.blit(zero[count_sqrt6], zero[count_sqrt6].get_rect(center=(477,294)))
                count_sqrt6+=1
                for_zero6=True
        if count_sqrt7==len(cross):
            if for_cross7:
                screen.blit(cross[-1], cross[-1].get_rect(center=(249, 408)))
            else:
                screen.blit(zero[-1], zero[-1].get_rect(center=(249,408)))
        elif sqrt7:
            if for_cross7 or (queue != 0 and queue % 2 != 0):
                screen.blit(cross[count_sqrt7], cross[count_sqrt7].get_rect(center=(249, 408)))
                count_sqrt7 += 1
                for_cross7 = True
            else:
                screen.blit(zero[count_sqrt7], zero[count_sqrt7].get_rect(center=(249, 408)))
                count_sqrt7 += 1
                for_zero7=True
        if count_sqrt8==len(cross):
            if for_cross8:
                screen.blit(cross[-1], cross[-1].get_rect(center=(365,408)))
            else:
                screen.blit(zero[-1], zero[-1].get_rect(center=(365,408)))
        elif sqrt8:
            if for_cross8 or (queue != 0 and queue % 2 != 0):
                screen.blit(cross[count_sqrt8], cross[count_sqrt8].get_rect(center=(365,408)))
                count_sqrt8 += 1
                for_cross8 = True
            else:
                screen.blit(zero[count_sqrt8], zero[count_sqrt8].get_rect(center=(365,408)))
                count_sqrt8 += 1
                for_zero8=True
        if count_sqrt9==len(cross):
            if for_cross9:
                screen.blit(cross[-1], cross[-1].get_rect(center=(477,408)))
            else:
                screen.blit(zero[-1], zero[-1].get_rect(center=(477,408)))
        elif sqrt9:
            if for_cross9 or (queue != 0 and queue % 2 != 0):
                screen.blit(cross[count_sqrt9], cross[count_sqrt9].get_rect(center=(477,408)))
                count_sqrt9 += 1
                for_cross9 = True
            else:
                screen.blit(zero[count_sqrt9], zero[count_sqrt9].get_rect(center=(477,408)))
                count_sqrt9 += 1
                for_zero9=True
        if (for_cross1 and for_cross2 and for_cross3) or (for_cross4 and for_cross5 and for_cross6) or(for_cross7 and for_cross8 and for_cross9) or \
            (for_cross1 and for_cross4 and for_cross7) or(for_cross2 and for_cross5 and for_cross8) or(for_cross3 and for_cross6 and for_cross9) or \
            (for_cross1 and for_cross5 and for_cross9) or(for_cross3 and for_cross5 and for_cross6):
            gameplay=False
        elif (for_zero1 and for_zero2 and for_zero3) or (for_zero4 and for_zero5 and for_zero6) or(for_zero7 and for_zero8 and for_zero9) or\
        (for_zero1 and for_zero4 and for_zero7) or(for_zero2 and for_zero5 and for_zero8) or(for_zero3 and for_zero6 and for_zero9) or \
        (for_zero1 and for_zero5 and for_zero9) or(for_zero3 and for_zero5 and for_zero6):
            gameplay=False
        elif sqrt1 and sqrt2 and sqrt3 and sqrt4 and sqrt5 and sqrt6 and sqrt7 and sqrt8 and sqrt9:
            gameplay = False
    else:
        for i in event.get():
            if i.type==QUIT:
                quit()
                running=False
        screen.fill('blue')
        screen.blit(restart,restart_rect)
        if restart_rect.collidepoint(mouse.get_pos()) and mouse.get_pressed()[0]:
            gameplay=True
            sqrt1, sqrt2, sqrt3, sqrt4, sqrt5, sqrt6, sqrt7, sqrt8, sqrt9 = False, False, False, False, False, False, False, False, False
            for_cross1, for_cross2, for_cross3, for_cross4, for_cross5, for_cross6, for_cross7, for_cross8, for_cross9 = False, False, False, False, False, False, False, False, False
            for_zero1, for_zero2, for_zero3, for_zero4, for_zero5, for_zero6, for_zero7, for_zero8, for_zero9 = False, False, False, False, False, False, False, False, False
            count_sqrt1, count_sqrt2, count_sqrt3, count_sqrt4, count_sqrt5, count_sqrt6, count_sqrt7, count_sqrt8, count_sqrt9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
            queue = 0
    display.update()
    clock.tick(50)
'''
(188,119)-координаты поля по левому углу
(199,130)- координаты левого квадрата по левому углу
'''