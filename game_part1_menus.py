#Créé le 23 Juillet 2023
from ion import *
from kandinsky import *
from time import *

interface=(255,182,57)
noir,blanc=(0,0,0),(255,255,255)
rouge,vert,bleu=(255,0,0),(0,203,0),(0,0,255)

running=True

menu=True
new_menu=True
hauteur_menu=[10,65,111,148,185]
crochet_menu=0

credits=False
hauteur_credits=-20

settings=False
new_settings=False
hauteur_settings=[23,66,109,152]
crochet_settings=0
back_settings=0

save=False
new_save=False
hauteur_save=[50]
crochet_save=0
back_save=0
correct=False
chiffre=[105,125,145,165,185,205]
code=0
nombre=0

options=False
new_options=False
hauteur_options=[5,33,71,112,140,168,196]
crochet_options=0

difficulte=False
new_difficulte=False
hauteur_difficulte=[0,40,80,120,160]
crochet_difficulte=0
difficulty=3

language=False
new_language=False
hauteur_language=[54,128]
crochet_language=0
langage=1

commandes=False
new_commandes=False

personnage=False
new_personnage=False
w=2
longueur_personnage=[10*w,40*w]
hauteur_personnage=[10*w,40*w]
crochet_hauteur_personnage=0
crochet_longueur_personnage=0

validation=False
new_validation=False
hauteur_validation=[150,180]
crochet_validation=0
back_validation=0

success=False
new_success=False
suces=[0 for _ in range(2)]

statistic=False
new_statistic=False
stats=[0 for i in range(5)]

game=False
new_game=False

while running:
  crochet_menu=0
  hauteur_credits=-20
  crochet_settings=0
  crochet_save=0
  code=0
  nombre=0
  crochet_options=0
  crochet_difficulte=0
  crochet_language=0
  crochet_validation=0
  while menu:
    while new_menu:
      new_menu=False
      fill_rect(0,0,320,222,interface)
      if langage==1:
        draw_string("Commencer une",95,hauteur_menu[0]-10,vert)
        draw_string("nouvelle partie",85,hauteur_menu[0]+10,vert)
        draw_string("Charger un point",80,hauteur_menu[1]-10)
        draw_string("de sauvegarde",95,hauteur_menu[1]+10)
        draw_string("Paramètres",110,hauteur_menu[2])
        draw_string("Crédits",125,hauteur_menu[3])
        draw_string("Quitter le jeu",90,hauteur_menu[4],rouge)
      elif langage==2:
        draw_string("Start a new game",80,hauteur_menu[0])
        draw_string("Load a save point",75,hauteur_menu[1])
        draw_string("Settings",120,hauteur_menu[2])
        draw_string("Credits",125,hauteur_menu[3])
        draw_string("Leave the game",90,hauteur_menu[4],rouge)
      draw_string("[",60,hauteur_menu[crochet_menu],bleu)
      draw_string("]",250,hauteur_menu[crochet_menu],bleu)
      sleep(0.2)
    if keydown(KEY_OK):
      if crochet_menu==0:
        x,y,m,t=0,0,20,2
        game=True
        new_game=True
      elif crochet_menu==1:
        save=True
        new_save=True
        back_save=1
      elif crochet_menu==2:
        settings=True
        new_settings=True
        back_settings=1
      elif crochet_menu==3:
        credits=True
        sleep(0.2)
      elif crochet_menu==4:
        validation=True
        new_validation=True
        back_validation=4
      menu=False
    elif keydown(KEY_DOWN):
      if crochet_menu<4:
        crochet_menu+=1
        new_menu=True
    elif keydown(KEY_UP):
      if crochet_menu>0:
        crochet_menu-=1
        new_menu=True

  while credits:
    fill_rect(0,0,320,222,interface)
    if langage==1:
      draw_string("Jeu créé,",115,hauteur_credits)
      draw_string("inventé,",120,hauteur_credits-20)
      draw_string("codé,",135,hauteur_credits-40)
      draw_string("pensé,",130,hauteur_credits-60)
      draw_string("et mis",130,hauteur_credits-80)
      draw_string("en oeuvre",115,hauteur_credits-100)
      draw_string("par:",140,hauteur_credits-120)
      draw_string("Maëlan Gallais",90,hauteur_credits-140)
    elif langage==2:
      draw_string("Game created,",100,hauteur_credits)
      draw_string("invented,",120,hauteur_credits-20)
      draw_string("coded,",135,hauteur_credits-40)
      draw_string("thought,",125,hauteur_credits-60)
      draw_string("and",145,hauteur_credits-80)
      draw_string("implemented",105,hauteur_credits-100)
      draw_string("by:",145,hauteur_credits-120)
      draw_string("Maëlan Gallais",90,hauteur_credits-140)
    draw_string("'clear'",250,0,rouge)
    if hauteur_credits<=362:
      hauteur_credits+=1
    else:
      hauteur_credits=0
    if keydown(KEY_BACKSPACE):
      credits=False
      menu=True
      new_menu=True
    sleep(0.005)

  while settings:
    while new_settings:
      new_settings=False
      fill_rect(0,0,320,222,interface)
      if langage==1:
        draw_string("Difficulté",110,hauteur_settings[0])
        draw_string("Language",120,hauteur_settings[1])
        draw_string("Commandes",115,hauteur_settings[2])
        draw_string("Changer de perso",80,hauteur_settings[3])
        draw_string("Touche 'clear' pour",65,186,rouge)
        draw_string("revenir en arriere",70,204,rouge)
      elif langage==2:
        draw_string("Difficulty",110,hauteur_settings[0])
        draw_string("Langage",120,hauteur_settings[1])
        draw_string("Controls",115,hauteur_settings[2])
        draw_string("Change character",80,hauteur_settings[3])
        draw_string("'clear' key to go back",50,190,rouge)
      draw_string("[",50,hauteur_settings[crochet_settings],bleu)
      draw_string("]",260,hauteur_settings[crochet_settings],bleu)
      sleep(0.2)
    if keydown(KEY_OK):
      if crochet_settings==0:
        difficulte=True
        new_difficulte=True
      elif crochet_settings==1:
        language=True
        new_language=True
      elif crochet_settings==2:
        commandes=True
        new_commandes=True
        sleep(0.2)
      elif crochet_settings==3:
        personnage=True
        new_personnage=True
      settings=False
    elif keydown(KEY_DOWN):
      if crochet_settings<3:
        crochet_settings+=1
        new_settings=True
    elif keydown(KEY_UP):
      if crochet_settings>0:
        crochet_settings-=1
        new_settings=True
    elif keydown(KEY_BACKSPACE):
      if back_settings==1:
        menu=True
        new_menu=True
      elif back_settings==2:
        options=True
        new_options=True
      settings=False

  while save:
    while new_save:
      new_save=False
      fill_rect(0,0,320,222,interface)
      if langage==1:
        draw_string("Selectionnez la",85,0)
        draw_string("sauvegarde :",100,18)
        draw_string("Cave",130,hauteur_save[0])
        draw_string("Touche 'clear' pour",65,186,rouge)
        draw_string("revenir en arriere",70,204,rouge)
      elif langage==2:
        draw_string("Select the backup :",75,15)
        draw_string("Cave",130,hauteur_save[0])
        draw_string("'clear' key to go back",50,190,rouge)
      draw_string("[",60,hauteur_save[crochet_save],bleu)
      draw_string("]",250,hauteur_save[crochet_save],bleu)
      sleep(0.2)
    if keydown(KEY_OK):
      fill_rect(0,0,320,222,interface)
      if langage==1:
        draw_string("Entrez la",115,20)
        draw_string("combinaison",105,40)
        draw_string("de 6 chiffres",95,60)
        draw_string("pour aller au",95,80)
        draw_string("point de",120,100)
        draw_string("sauvegarde :",100,120)
      elif langage==2:
        draw_string("Enter the",115,20)
        draw_string("6-digit",125,40)
        draw_string("combination",105,60)
        draw_string("to go to",120,80)
        draw_string("the save",120,100)
        draw_string("point :",125,120)       
      if crochet_save==0:
        if langage==1:
          draw_string("Cave",130,150)
        elif langage==2:
          draw_string("Cave",130,150)
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
          if langage==1:
            draw_string("Code bon !",110,200,vert)
          elif langage==2:
            draw_string("Code good !",105,200,vert)
          game=True
          new_game=True
          save=False
          x,y,t=-660,0,2
          m,dx,dy=10*t,160-5*t,111-10*t
          sleep(1)
        else:
          if langage==1:
            draw_string("Code erroné !",95,200,rouge)
          elif langage==2:
            draw_string("Wrong code !",100,200,rouge)
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
      if back_save==1:
        menu=True
        new_menu=True
      elif back_save==2:
        options=True
        new_options=True

  while options:
    while new_options:
      new_options=False
      fill_rect(0,0,320,222,interface)
      if langage==1:
        draw_string("Reprendre",115,hauteur_options[0],vert)
        draw_string("Nouvelle partie",85,hauteur_options[1])
        draw_string("Charger un point",80,hauteur_options[2]-10)
        draw_string("de sauvegarde",95,hauteur_options[2]+10)
        draw_string("Succès",130,hauteur_options[3])
        draw_string("Statistiques",100,hauteur_options[4])
        draw_string("Paramètres",115,hauteur_options[5])
        draw_string("Retourner au menu",75,hauteur_options[6],rouge)
      elif langage==2:
        draw_string("Resume",130,hauteur_options[0],vert)
        draw_string("New game",120,hauteur_options[1])
        draw_string("Load a save point",75,hauteur_options[2])
        draw_string("Success",125,hauteur_options[3])
        draw_string("Statistics",110,hauteur_options[4])
        draw_string("Settings",120,hauteur_options[5])
        draw_string("Return to menu",90,hauteur_options[6],rouge)
      draw_string("[",60,hauteur_options[crochet_options],bleu)
      draw_string("]",250,hauteur_options[crochet_options],bleu)
      sleep(0.2)
    if keydown(KEY_OK):
      if crochet_options==0:
        game=True
        new_game=True
      elif crochet_options==1:
        validation=True
        new_validation=True
        back_validation=1
      elif crochet_options==2:
        validation=True
        new_validation=True
        back_validation=2
      elif crochet_options==3:
        success=True
        new_success=True
      elif crochet_options==4:
        statistic=True
        new_statistic=True
      elif crochet_options==5:
        settings=True
        new_settings=True
        back_settings=2
      elif crochet_options==6:
        validation=True
        new_validation=True
        back_validation=3
      options=False
    elif keydown(KEY_DOWN):
      if crochet_options<6:
        crochet_options+=1
        new_options=True
    elif keydown(KEY_UP):
      if crochet_options>0:
        crochet_options-=1
        new_options=True

  while difficulte:
    while new_difficulte:
      new_difficulte=False
      fill_rect(0,0,320,222,interface)
      if langage==1:
        draw_string("Paisible",120,hauteur_difficulte[0])
        draw_string("Facile",130,hauteur_difficulte[1])
        draw_string("Moyen",135,hauteur_difficulte[2])
        draw_string("Difficile",115,hauteur_difficulte[3])
        draw_string("Hardcore",120,hauteur_difficulte[4])
        draw_string("Touche 'clear' pour",65,186,rouge)
        draw_string("revenir en arriere",70,204,rouge)
      elif langage==2:
        draw_string("Peaceful",120,hauteur_difficulte[0])
        draw_string("Easy",140,hauteur_difficulte[1])
        draw_string("Medium",130,hauteur_difficulte[2])
        draw_string("Hard",140,hauteur_difficulte[3])
        draw_string("Hardcore",120,hauteur_difficulte[4])
        draw_string("'clear' key to go back",50,190,rouge)
      draw_string("[",100,hauteur_difficulte[crochet_difficulte])
      draw_string("]",210,hauteur_difficulte[crochet_difficulte])
      sleep(0.2)
    if keydown(KEY_OK):
      if crochet_difficulte==0:
        difficulty=1
      elif crochet_difficulte==1:
        difficulty=2
      elif crochet_difficulte==2:
        difficulty=3
      elif crochet_difficulte==3:
        difficulty=4
      elif crochet_difficulte==4:
        difficulty=5
      draw_string("OK !",140,101)
      sleep(0.5)
      settings=True
      new_settings=True
      difficulte=False
    elif keydown(KEY_DOWN):
      if crochet_difficulte<4:
        crochet_difficulte+=1
        new_difficulte=True
    elif keydown(KEY_UP):
      if crochet_difficulte>0:
        crochet_difficulte-=1
        new_difficulte=True
    elif keydown(KEY_BACKSPACE):
      settings=True
      new_settings=True
      difficulte=False

  while language:
    while new_language:
      new_language=False
      fill_rect(0,0,320,222,interface)
      draw_string("Francais",120,hauteur_language[0])
      draw_string("English",125,hauteur_language[1])
      if langage==1:
        draw_string("Touche 'clear' pour",65,186,rouge)
        draw_string("revenir en arriere",70,204,rouge)
      elif langage==2:
        draw_string("'clear' key to go back",50,190,rouge)
      draw_string("[",100,hauteur_language[crochet_language],bleu)
      draw_string("]",210,hauteur_language[crochet_language],bleu)
      sleep(0.2)
    if keydown(KEY_OK):
      if crochet_language==0:
        langage=1
      elif crochet_language==1:
        langage=2
      draw_string("OK !",140,101)
      sleep(0.5)
      settings=True
      new_settings=True
      language=False
    elif keydown(KEY_DOWN):
      if crochet_language<1:
        crochet_language+=1
        new_language=True
    elif keydown(KEY_UP):
      if crochet_language>0:
        crochet_language-=1
        new_language=True
    elif keydown(KEY_BACKSPACE):
      settings=True
      new_settings=True
      language=False

  while commandes:
    while new_commandes:
      new_commandes=False
      fill_rect(0,0,320,222,interface)
      draw_string("'clear'",250,0,rouge)
      if langage==1:
        draw_string("Dans le jeu :",0,0)
        draw_string("-Flèches = déplacement",0,25)
        draw_string("-'EXE' = tir",0,50)
        draw_string("-'shift' = verrouillage flèche",0,75)
        draw_string("-'clear' = changement taille",0,100)
        draw_string("-'paste' = options",0,125)
      elif langage==2:
        draw_string("In the game :",0,0)
        draw_string("-Arrows = movements",0,25)
        draw_string("-'EXE' = shot",0,50)
        draw_string("-'shift' = lock arrow",0,75)
        draw_string("-'clear' = change size",0,100)
        draw_string("-'paste' = options",0,125)
    if keydown(KEY_BACKSPACE):
      settings=True
      new_settings=True
      commandes=False

  while personnage:
#(
    fill_rect(0,0,320,222,interface)
    draw_string("Ne fonctionne pas",75,10)
    draw_string("sans l'autre partie.",60,30)
    draw_string("La calculatrice",85,70)
    draw_string("n'accepte pas la",80,90)
    draw_string("combinaison des",85,110)
    draw_string("deux parties.",95,130)
    draw_string("Le fichier est",90,170)
    draw_string("trop volumineux.",80,190)
    new_personnage=False
    settings=True
    new_settings=True
    personnage=False
    sleep(5)
#)
    while new_personnage:
      new_personnage=False
      fill_rect(0,0,320,222,interface)
      fill_rect(longueur_personnage[crochet_longueur_personnage]-5*w,hauteur_personnage[crochet_hauteur_personnage]-5*w,10*w+10*w,20*w+10*w,noir)
      for i in range(2):
        if i==0:
          perso=toad
          px=longueur_personnage[0]
          py=hauteur_personnage[0]
        elif i==1:
          perso=minion
          px=longueur_personnage[1]
          py=hauteur_personnage[0]
        for a in range(20):
          for b in range(10):
            if perso[a][b]==1:
              fill_rect(px+b*w,py+a*w,w,w,blanc)
            elif perso[a][b]==2:
              fill_rect(px+b*w,py+a*w,w,w,noir)
            elif perso[a][b]==3:
              fill_rect(px+b*w,py+a*w,w,w,(249,32,42))
            elif perso[a][b]==4:
              fill_rect(px+b*w,py+a*w,w,w,(253,201,142))
            elif perso[a][b]==5:
              fill_rect(px+b*w,py+a*w,w,w,(20,32,151))
            elif perso[a][b]==6:
              fill_rect(px+b*w,py+a*w,w,w,(241,106,40))
            elif perso[a][b]==7:
              fill_rect(px+b*w,py+a*w,w,w,(100,56,0))
            elif perso[a][b]==8:
              fill_rect(px+b*w,py+a*w,w,w,(255,255,0))
            elif perso[a][b]==9:
              fill_rect(px+b*w,py+a*w,w,w,bleu)
            elif perso[a][b]==10:
              fill_rect(px+b*w,py+a*w,w,w,(125,125,125))
        sleep(0.2)
    if keydown(KEY_OK):
      if crochet_hauteur_personnage==0 and crochet_longueur_personnage==0:
        perso=toad
        draw_string("Toad !",130,101)
      elif crochet_hauteur_personnage==0 and crochet_longueur_personnage==1:
        perso=minion
        draw_string("Minion !",120,101)
      sleep(0.5)
      settings=True
      new_settings=True
      personnage=False
    elif keydown(KEY_RIGHT):
      if crochet_longueur_personnage<1:
        crochet_longueur_personnage+=1
        new_personnage=True
    elif keydown(KEY_LEFT):
      if crochet_longueur_personnage>0:
        crochet_longueur_personnage-=1
        new_personnage=True
    elif keydown(KEY_DOWN):
      if crochet_hauteur_personnage<0:
        crochet_hauteur_personnage-=1
        new_personnage=True
    elif keydown(KEY_UP):
      if crochet_hauteur_personnage>0:
        crochet_hauteur_personnage+=1
        new_personnage=True
    elif keydown(KEY_BACKSPACE):
      settings=True
      new_settings=True
      personnage=False

  while validation:
    while new_validation:
      new_validation=False
      fill_rect(0,0,320,222,interface)
      if langage==1:
        draw_string("Etes-vous sur",95,10)
        draw_string("de vouloir continuer ?",50,30)
        draw_string("Toute progression",75,70)
        draw_string("sera perdue !",95,90)
        draw_string("Ok",150,hauteur_validation[0],rouge)
        draw_string("Annuler",125,hauteur_validation[1],vert)
      elif langage==2:
        draw_string("Are you sure you",80,10)
        draw_string("want to continue ?",70,30)
        draw_string("Any progress",100,70)
        draw_string("will be lost !",90,90)
        draw_string("Ok",150,hauteur_validation[0],rouge)
        draw_string("Cancel",130,hauteur_validation[1],vert)
      draw_string("[",110,hauteur_validation[crochet_validation])
      draw_string("]",200,hauteur_validation[crochet_validation])
      sleep(0.2)
    if keydown(KEY_OK):
      if back_validation==1:
        if crochet_validation==0:
          x,y,m,t=0,0,20,2
          game=True
          new_game=True
        elif crochet_validation==1:
          options=True
          new_options=True
      elif back_validation==2:
        if crochet_validation==0:
          save=True
          new_save=True
          back_save=2
        elif crochet_validation==1:
          options=True
          new_options=True
      elif back_validation==3:
        if crochet_validation==0:
          menu=True
          new_menu=True
        elif crochet_validation==1:
          options=True
          new_options=True
      elif back_validation==4:
        if crochet_validation==0:
          running=False
        elif crochet_validation==1:
          menu=True
          new_menu=True
      validation=False
    elif keydown(KEY_DOWN):
      if crochet_validation<1:
        crochet_validation+=1
        new_validation=True
    elif keydown(KEY_UP):
      if crochet_validation>0:
        crochet_validation-=1
        new_validation=True

  while success:
    while new_success:
      new_success=False
      fill_rect(0,0,320,222,interface)
      draw_string("'clear'",250,0)
      if langage==1:msg=["Tuer un ennemi","Se rapetisser"]
      elif langage==2:msg=["Kill an enemy","Get smaller"]
      lon=int(222/(len(suces)*2+1))
      for i in range(len(suces)):
       if suces[i]:draw_string(msg[i],160-len(msg[i])*5,lon*2*i+lon)
       else:draw_string(len(msg[i])*"*",160-len(msg[i])*5,lon*2*i+lon)
      sleep(0.2)
    if keydown(KEY_BACKSPACE):
      options=True
      new_options=True
      success=False

  while statistic:
    while new_statistic:
      new_statistic=False
      fill_rect(0,0,320,222,interface)
      draw_string("'clear'",250,0)
      for i in range(5):
        draw_string(str(stats[i])+2*" ",10,i*34+18)
      draw_string(str(int(stats[1]/stats[0]*100 if stats[0]!=0 else 0))+"%",10,188)
      if langage==1:
        draw_string(" balles tirées",40,18)
        draw_string(" cibles atteintes",40,52)
        draw_string(" de vie de régénérée",40,86)
        draw_string(" balles encaissées",40,120)
        draw_string(" ennemis tués",40,154)
        draw_string(" de précision de tirs",40,188)
      if langage==2:
        draw_string(" bullets fired",40,18)
        draw_string(" targets hit",40,52)
        draw_string(" life regenerated",40,86)
        draw_string(" bullets taken",40,120)
        draw_string(" enemies killed",40,154)
        draw_string(" shooting accuracy",40,188)
      sleep(0.2)
    if keydown(KEY_BACKSPACE):
      options=True
      new_options=True
      statistic=False

  while game:
    while new_game:
      new_game=False
      fill_rect(0,0,320,222,noir)
      draw_string("'paste'",125,101)
    if keydown(KEY_TOOLBOX):
      options=True
      new_options=True
      game=False

fill_rect(0,0,320,222,(0,)*3)
if langage==1:draw_string("Merci d'avoir joué!",65,102)
if langage==2:draw_string("Thanks for playing!",65,102)
