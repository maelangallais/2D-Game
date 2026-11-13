#Créé le 09 Septembre 2025

from kandinsky import fill_rect as fr,draw_string as ds,get_pixel as gp
from ion import keydown as kd
from random import randint as rd,uniform as uf,choice as ch

str1="0001111000;0111331110;1113333111;3113333113;3311331133;3311111133;3166666613;1644444461;0442442440;0444444440;0044444400;0655665560;0555445550;4555445554;4551111554;4551111554;0011111100;0011001100;0077007700;0777007770"
minion=[[0,0,8,8,8,8,8,8,0,0],[0,8,8,8,8,8,8,8,8,0],[8,8,10,10,8,8,10,10,8,8],[2,10,2,1,10,10,2,1,10,2],[2,10,1,1,10,10,1,1,10,2],[8,8,10,10,8,8,10,10,8,8],[8,8,8,8,8,8,8,8,8,8],[8,8,2,8,8,8,8,2,8,8],[8,8,8,2,2,2,2,8,8,8],[9,8,8,8,8,8,8,8,8,9],[8,9,9,9,9,9,9,9,9,8],[8,8,9,9,9,9,9,9,8,8],[8,8,9,9,9,9,9,9,8,8],[8,8,9,9,9,9,9,9,8,8],[8,9,9,9,9,9,9,9,9,8],[2,9,9,9,9,9,9,9,9,2],[2,9,9,9,9,9,9,9,9,2],[0,0,2,2,0,0,2,2,0,0],[0,0,2,2,0,0,2,2,0,0],[0,2,2,2,0,0,2,2,2,0]]
str2="00000001111000000000;00000111111110000000;00001111111111100000;00011111111111110000;00011111111111111000;00111111111111111100;00111111111111111100;00111111111111111110;01111111111111111110;01111111111111111110;01111111111111111111;01111111111111111111;01111111111111111111;11111111111111111111;11111111111111111111;11111111111111111111;11111111111111111111;01111111111111111110;01111111111111111110;00011111111111111100"
str3="000001111111110;011111122222211;111122222222221;001111122222211;000000111111110"
str4="00400;04540;45554;04540;00400"
str5="00100;01010;10001"
def decode(char):
 rows=char.split(';')
 return[[int(c)for c in row]for row in rows]
toad,rocher,projectile,touche,fleche=decode(str1),decode(str2),decode(str3),decode(str4),decode(str5)
del decode,str1,str2,str3,str4,str5

black,wh=(0,)*3,(255,)*3
re,gr,bl=(255,0,0),(0,203,0),(0,0,255)

herbe=(148,255,99)
route,ligne=(123,125,123),(255,219,90)
chemin=(66,40,8)
caillou=(99,101,99)
cave=(123,105,74)
balle1,balle2=(0,0,255),(0,0,150)
touche1,touche2=(255,90,0),(255,200,0)
balle_enemi1,balle_enemi2=(255,0,0),(150,0,0)
p_c=[wh,black,(255,32,41),(255,203,140),(16,32,148),(247,105,41),(99,56,0),(255,255,0),bl,(123,125,123)]
passage_secret=(0,4,0)

pos_d=[[-50,-50,420,322,herbe],[135,-50,50,322,route],[158,-44,4,310,ligne],[180,86,240,50,route],[162,109,252,4,ligne],[420,101,300,20,chemin],[465,81,40,60,chemin],
[720,86,50,50,cave],[770,0,370,222,cave]]
pos_c=[[10,91,2],[475,101,1],[900,10,3],[800,170,2],[1040,165,1],[1060,175,1],[1045,195,1]]

game,new=True,True
x,y,m,t=0,0,20,2
grand=True
bm=[50,50,-50,-820]
KEY=[52,12,17,16]

difficulty=2
nd=difficulty

e_l=[[40,70],[60,100],[80,120],[100,150],[130,170]]
pp=[[160-5*t,111-10*t,t,100,0]]
#pp=[[160-5*t+20,111-10*t,t,100,0],[1090,91,2]]
#for i in range(1,len(pp)):pp[i].append(rd(e_l[nd][0]//10,e_l[nd][1]//10)*10),pp[i].append(0)
#for i in range(1,len(pp)):
# if nd>2:
#  for i1 in range(nd-2):
#   pp.append([pp[i][0],pp[i][1]+20+(-2*(i1+1)+3)*60,1,rd(e_l[nd][0]//10,e_l[nd][1]//10)*10,0])
perso,ennemi=toad,minion

#à renouveler lors d'un changement de taille!
pp_b=[[[0 for _ in range(len((ennemi if i else perso)[0])*pp[i][2])]for _ in range(len(ennemi if i else perso)*pp[i][2])]for i in range(len(pp))]

add,sub=lambda a,b:a+b,lambda a,b:a-b
inf,sup=lambda a,b:a<=b,lambda a,b:a>=b
dst=lambda x1,y1,x2,y2:((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))**.5

def draw_p(x,y,t,l,idx):
 for a in range(len(l)):
  for b in range(len(l[0])):
   for c in range(t):
    for d in range(t):
     pp_b[idx][a*t+c][b*t+d]=gp(x+b*t+d,y+a*t+c)
   for i in range(1,10):
    if l[a][b]==i:fr(x+b*t,y+a*t,t,t,p_c[i-1])
def draw_b(x,y,t,l):
 for a in range(len(l)):
  for b in range(len(l[0])):
   fr(x+b,y+a,1,1,l[a][b])
def draw_o(cx,cy,t,l):
 for a in range(len(l)):
  for b in range(len(l[0])):
   if l[a][b]==1:fr(cx+b*t,cy+a*t,t,t,caillou)
   elif l[a][b]==4:fr(cx+b*t,cy+a*t,t,t,touche1)
   elif l[a][b]==5:fr(cx+b*t,cy+a*t,t,t,touche2)
def draw_d():
 fr(0,0,320,222,black)
 for ox,oy,w,h,c in pos_d:fr(ox+x,oy+y,w,h,c)
 for i in range(len(pos_c)):draw_o(pos_c[i][0]+x,pos_c[i][1]+y,pos_c[i][2],rocher)

def move(v,nb):
 global new,x,y,op
 ox,oy=160-5*t,111-10*t
 ppx,ppy=pp[0][0],pp[0][1]
 [d,dd,p,s],ok,[c1,c2,c3]=[x,ppx,20,ox]if v in[0,3]else[y,ppy,10,oy],0,[add,sub,inf]if v in[0,1]else[sub,add,sup]
#Système de ré-actualisation lorsque le
#joueur est sur le point de sortir de l'écran
# """
 [pppx,pppy]=[c2(dd,m),ppy]if v in[0,3]else[ppx,c2(dd,m)]
 if pppx<0 or pppx>320-10*t or pppy<0 or pppy>222-20*t:
  x-=pppx-ox;y-=pppy-oy
  d=x if v in[0,3]else y
  pp[0][0]=ox;pp[0][1]=oy;dd=s
  draw_d()
  nb=+1
  new=True
 else:
  for i in range(p*t):
   mx,my=[-m,i,i,10*t+m-1],[i,-m,20*t+m-1,i]
   if not gp(ppx+mx[v],ppy+my[v])in[black,caillou]:ok+=1
  if ok==p*t:
   dd=c2(dd,m)
   if nb==0:draw_b(pp[0][0],pp[0][1],t,pp_b[0])
   nb=+1
   new=True
# """
#Système avec ré-actualisation lors de l'écart
#d'un certain seuil du centre de l'écran
 """
 for i in range(p*t):
  mx,my=[-m,i,i,10*t+m-1],[i,-m,20*t+m-1,i]
  if not gp(ppx+mx[v],ppy+my[v])in[black,caillou]:ok+=1
 if ok==p*t:
  [pppx,pppy]=[c2(dd,m),ppy]if v in[0,3]else[ppx,c2(dd,m)]
  if dst(pppx,pppy,ox,oy)>70:
   x-=pppx-ox;y-=pppy-oy
   d=x if v in[0,3]else y
   pp[0][0]=ox;pp[0][1]=oy;dd=s
   draw_d()
  else:
   dd=c2(dd,m)
   if nb==0:draw_b(pp[0][0],pp[0][1],t,pp_b[0])
  nb=+1
  new=True
# """
 [x,y,pp[0][0],pp[0][1]]=[d,y,dd,pp[0][1]]if v in[0,3]else[x,d,pp[0][0],dd]
 return nb

draw_d()
while game:
 if new:
  new=False
  if len(pp)>0:
   for i,[dx,dy,t,vie,e]in enumerate(pp):
    [dx,dy,l]=[dx-x,dy-y,perso]if i==0 else[dx,dy,ennemi]
    if vie>0:draw_p(dx+x,dy+y,t,l,i)
    if i>0:ds(str(vie),dx+x,dy-20+y)
  ds(str(x)+","+str(y),20,0)
  ds(str(pp[0][0])+","+str(pp[0][1]),20,22)
 n=0
 for i in range(4):
  if kd(i):n=move(i,n)
