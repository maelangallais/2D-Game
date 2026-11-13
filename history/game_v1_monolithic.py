#Cree le 23 Juillet 2023
from ion import *
from kandinsky import *
from time import *

toad=[[0,0,0,0,1,1,1,1,0,0,0,0],
      [0,0,1,1,1,3,3,1,1,1,0,0],
      [0,1,1,1,3,3,3,3,1,1,1,0],
      [0,1,1,1,3,3,3,3,1,1,1,0],
      [3,1,1,1,3,3,3,3,1,1,1,3],
      [3,3,1,1,1,3,3,1,1,1,1,3],
      [3,3,1,1,1,1,1,1,1,1,1,3],
      [3,1,1,6,6,6,6,6,6,1,1,3],
      [1,1,6,4,4,4,4,4,4,6,1,1],
      [0,0,4,4,2,4,4,2,4,4,0,0],
      [0,0,4,4,2,4,4,2,4,4,0,0],
      [0,0,4,4,4,4,4,4,4,4,0,0],
      [0,0,0,4,4,4,4,4,4,0,0,0],
      [0,0,6,5,5,6,6,5,5,6,0,0],
      [0,4,6,5,5,4,4,5,5,6,4,0],
      [0,6,5,5,5,4,4,5,5,5,6,0],
      [4,6,5,5,5,4,4,5,5,5,6,4],
      [4,6,5,5,5,4,4,5,5,5,6,4],
      [4,6,5,5,1,1,1,1,5,5,6,4],
      [4,6,5,5,1,1,1,1,5,5,6,4],
      [0,0,0,1,1,1,1,1,1,0,0,0],
      [0,0,0,1,1,0,0,1,1,0,0,0],
      [0,0,0,1,1,0,0,1,1,0,0,0],
      [0,0,0,7,7,0,0,7,7,0,0,0],
      [0,0,7,7,7,0,0,7,7,7,0,0]]

rocher=[[0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]]


interface=(255,181,59)

running=True

menu=True
new_menu=True
hauteur_menu=[32,96,150,192]
crochet_menu=0

credits=False
hauteur_credits=-20

save=False
new_save=False
back=1
hauteur_save=[50]
crochet_save=0
correct=False
chiffre=[105,125,145,165,185,205]
nombre=0
code=0

options=False
new_options=False
hauteur_options=[5,33,71,112,140,168,196]
crochet_options=0

game=False
new_game=False
blanc,noir,bleu=(255,255,255),(0,0,0),(0,0,255)
herbe=(150,252,100)
route,ligne=(127,127,127),(255,216,94)
chemin=(70,40,15)
caillou=(99,101,99)
x,y,m,t=0,0,20,2
grand=True
taille_caillou=2

while running:
  while menu:
    while new_menu:
      new_menu=False
      fill_rect(0,0,320,222,interface)
      draw_string("Commencer une",95,hauteur_menu[0]-10)
      draw_string("nouvelle partie",85,hauteur_menu[0]+10)
      draw_string("Charger un point",80,hauteur_menu[1]-10)
      draw_string("de sauvegarde",95,hauteur_menu[1]+10)
      draw_string("Credits",125,hauteur_menu[2])
      draw_string("Quitter le jeu",90,hauteur_menu[3])
      fill_rect(60,65,10,100,interface)
      fill_rect(260,65,10,100,interface)
      draw_string("[",60,hauteur_menu[crochet_menu],bleu)
      draw_string("]",250,hauteur_menu[crochet_menu],bleu)
      sleep(0.2)
    if keydown(KEY_OK):
      if crochet_menu==0:
        game=True
        new_game=True
        menu=False
      elif crochet_menu==1:
        save=True
        new_save=True
        back=1
        menu=False
        sleep(0.2)
      elif crochet_menu==2:
        credits=True
        sleep(0.2)
      elif crochet_menu==3:
        menu=False
        running=False
    elif keydown(KEY_DOWN):
      if crochet_menu<3:
        crochet_menu+=1
        new_menu=True
    elif keydown(KEY_UP):
      if crochet_menu>0:
        crochet_menu-=1
        new_menu=True

    while credits:
      fill_rect(0,0,320,222,interface)
      draw_string("Jeu créé,",115,hauteur_credits)
      draw_string("inventé,",120,hauteur_credits-20)
      draw_string("codé,",135,hauteur_credits-40)
      draw_string("pensé,",130,hauteur_credits-60)
      draw_string("et mis",130,hauteur_credits-80)
      draw_string("en oeuvre",115,hauteur_credits-100)
      draw_string("par:",140,hauteur_credits-120)
      draw_string("Maelan Gallais",90,hauteur_credits-140)
      draw_string("'OK'",280,0)
      if hauteur_credits<=362:
        hauteur_credits+=1
      else:
        hauteur_credits=0
      if keydown(KEY_OK):
        credits=False
        menu=True
        new_menu=True
        sleep(0.2)
      sleep(0.005)

  while save:
    while new_save:
      new_save=False
      fill_rect(0,0,320,222,interface)
      draw_string("Selectionnez la",85,0)
      draw_string("sauvegarde :",100,18)
      draw_string("Tunnel",130,hauteur_save[0])
      draw_string("[",60,hauteur_save[crochet_save],bleu)
      draw_string("]",250,hauteur_save[crochet_save],bleu)
      draw_string("Touche 'clear' pour",65,186)
      draw_string("revenir en arriere",70,204)
      sleep(0.2)
    if keydown(KEY_OK):
      fill_rect(0,0,320,222,interface)
      draw_string("Entrez la",115,20)
      draw_string("combinaison",105,40)
      draw_string("de 6 chiffres",95,60)
      draw_string("pour aller au",95,80)
      draw_string("point de",120,100)
      draw_string("sauvegarde :",100,120)
      if crochet_save==0:
        draw_string("Tunnel",130,150)
      while not nombre==6:
        if keydown(KEY_ZERO):
          draw_string("0",chiffre[nombre],170,bleu)
          code+=0*10**(5-nombre)
          nombre+=1
          sleep(0.2)
        elif keydown(KEY_ONE):
          draw_string("1",chiffre[nombre],170,bleu)
          code+=1*10**(5-nombre)
          nombre+=1
          sleep(0.2)
        elif keydown(KEY_TWO):
          draw_string("2",chiffre[nombre],170,bleu)
          code+=2*10**(5-nombre)
          nombre+=1
          sleep(0.2)
        elif keydown(KEY_THREE):
          draw_string("3",chiffre[nombre],170,bleu)
          code+=3*10**(5-nombre)
          nombre+=1
          sleep(0.2)
        elif keydown(KEY_FOUR):
          draw_string("4",chiffre[nombre],170,bleu)
          code+=4*10**(5-nombre)
          nombre+=1
          sleep(0.2)
        elif keydown(KEY_FIVE):
          draw_string("5",chiffre[nombre],170,bleu)
          code+=5*10**(5-nombre)
          nombre+=1
          sleep(0.2)
        elif keydown(KEY_SIX):
          draw_string("6",chiffre[nombre],170,bleu)
          code+=6*10**(5-nombre)
          nombre+=1
          sleep(0.2)
        elif keydown(KEY_SEVEN):
          draw_string("7",chiffre[nombre],170,bleu)
          code+=7*10**(5-nombre)
          nombre+=1
          sleep(0.2)
        elif keydown(KEY_EIGHT):
          draw_string("8",chiffre[nombre],170,bleu)
          code+=8*10**(5-nombre)
          nombre+=1
          sleep(0.2)
        elif keydown(KEY_NINE):
          draw_string("9",chiffre[nombre],170,bleu)
          code+=9*10**(5-nombre)
          nombre+=1
          sleep(0.2)
      if crochet_save==0:
        if code==123456:
          draw_string("Code correct !",90,200)
          game=True
          new_game=True
          save=False
          x,y,m,t=-350,0,10,1
          sleep(1)
        else:
          draw_string("Code incorrect !",80,200)
          sleep(1)
          new_save=True
          nombre=0
          code=0
    elif keydown(KEY_DOWN):
      if crochet_save<0:
        crochet_save+=1
        new_save=True
    elif keydown(KEY_UP):
      if crochet_save>0:
        crochet_save-=1
        new_save=True
    elif keydown(KEY_BACKSPACE):
      save=False
      if back==1:
        menu=True
        new_menu=True
      elif back==2:
        options=True
        new_options=True

  while options:
    while new_options:
      new_options=False
      fill_rect(0,0,320,222,interface)
      draw_string("Reprendre",115,hauteur_options[0])
      draw_string("Nouvelle partie",85,hauteur_options[1])
      draw_string("Charger un point",80,hauteur_options[2]-10)
      draw_string("de sauvegarde",95,hauteur_options[2]+10)
      draw_string("Difficulté",110,hauteur_options[3])
      draw_string("Language",120,hauteur_options[4])
      draw_string("Commandes",115,hauteur_options[5])
      draw_string("Retourner au menu",75,hauteur_options[6])
      draw_string("[",60,hauteur_options[crochet_options],bleu)
      draw_string("]",250,hauteur_options[crochet_options],bleu)
      sleep(0.2)
    if keydown(KEY_OK):
      if crochet_options==0:
        game=True
        new_game=True
        options=False
      elif crochet_options==1:
        x,y,m,t=0,0,20,2
        game=True
        new_game=True
        options=False
      elif crochet_options==2:
        save=True
        new_save=True
        back=2
        options=False
      elif crochet_options==6:
        options=False
        menu=True
        new_menu=True
    elif keydown(KEY_DOWN):
      if crochet_options<6:
        crochet_options+=1
      new_options=True
    elif keydown(KEY_UP):
      if crochet_options>0:
        crochet_options-=1
      new_options=True

  dx,dy=160-6*t,int(round(111-12.5*t,0))

  while game:
    while new_game:
      fill_rect(0,0,320,222,noir)
      fill_rect(-50+x,-50+y,420,322,herbe)
      fill_rect(130+x,-50+y,60,322,route)
      fill_rect(158+x,-44+y,4,310,ligne)
      fill_rect(180+x,081+y,240,60,route)
      fill_rect(162+x,109+y,252,4,ligne)
      fill_rect(420+x,096+y,300,30,chemin)
      for a in range(15):
        for b in range(18):
          if rocher[a][b]==1:
            fill_rect(12+b*taille_caillou+x,96+a*taille_caillou+y,taille_caillou,taille_caillou,caillou)
      for a in range(25):
        for b in range(12):
          if toad[a][b]==1:
            fill_rect(dx+b*t,dy+a*t,t,t,blanc)
          elif toad[a][b]==2:
            fill_rect(dx+b*t,dy+a*t,t,t,noir)
          elif toad[a][b]==3:
            fill_rect(dx+b*t,dy+a*t,t,t,(249,32,42))
          elif toad[a][b]==4:
            fill_rect(dx+b*t,dy+a*t,t,t,(253,201,142))
          elif toad[a][b]==5:
            fill_rect(dx+b*t,dy+a*t,t,t,(20,32,151))
          elif toad[a][b]==6:
            fill_rect(dx+b*t,dy+a*t,t,t,(241,106,40))
          elif toad[a][b]==7:
            fill_rect(dx+b*t,dy+a*t,t,t,(100,56,0))
      sleep(0.1)
      ok=0
      new_game=False
    if get_pixel(dx+12*t+m,dy+12*t)==(66,40,8) and grand:
      m=10
      t=1
      dx,dy=160-6*t,int(round(111-12.5*t,0))
      new_game=True
      grand=False
    elif get_pixel(dx+12*t+m*3,dy+12*t)!=(66,40,8) and not grand:
      m=20
      t=2
      dx,dy=160-6*t,int(round(111-12.5*t,0))
      new_game=True
      grand=True
    elif keydown(KEY_TOOLBOX):
      options=True
      new_options=True
      crochet_options=0
      game=False
    elif keydown(KEY_UP):
      for i in range(12*t):
        if get_pixel(dx+i,dy-m)!=noir:
          if get_pixel(dx+i,dy-m)!=caillou:
            ok+=1
      if ok==i+1:
        if y<=300 and dy==int(round(111-12.5*t,0)):
          y+=m
        else:
          dy-=m
        ok=0
      new_game=True
    elif keydown(KEY_DOWN):
      for i in range(12*t):
        if get_pixel(dx+i,dy+25*t+m-1)!=noir:
          if get_pixel(dx+i,dy+25*t+m-1)!=caillou:
            ok+=1
      if ok==i+1:
        if y>=-50 and dy==int(round(111-12.5*t,0)):
          y-=m
        else:
          dy+=m
        ok=0
      new_game=True
    elif keydown(KEY_LEFT):
      for i in range(25*t):
        if get_pixel(dx-m,dy+i)!=noir:
          if get_pixel(dx-m,dy+i)!=caillou:
            ok+=1
      if ok==i+1:
        if x<=50 and dx==160-6*t:
          x+=m
        else:
          dx-=m
      new_game=True
    elif keydown(KEY_RIGHT):
      for i in range(25*t):
        if get_pixel(dx+12*t+m-1,dy+i)!=noir:
          if get_pixel(dx+12*t+m-1,dy+i)!=caillou:
            ok+=1
      if ok==i+1:
        if x>=-400 and dx==160-6*t:
          x-=m
        else:
          dx+=m
      new_game=True
