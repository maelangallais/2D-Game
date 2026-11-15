#Cree le 23 Juillet 2023
#319 lignes avant optimisation et 10,6 Ko
#apres 10h et 49m de travail
#211 lignes et 9,04 Ko
#Après ajouts des niveaux de 
#difficulté + amélioration 
#générale du jeu : 
#346 lignes et 12Ko
#Ajout de succès,stats et checkpoints:
#393 lignes et 14Ko
#Idées noms: Crunky
#À suivre :
# - Partie 2 : Histoire, ennemis, combats, inventaire, objets à récolter, nouvelles zones, etc...
from math import cos,sin,radians,sqrt,fabs,floor,atan2,degrees
from kandinsky import fill_rect as fr,draw_string as ds,get_pixel as gp
from ion import keydown as kd
from time import monotonic as mn,sleep as sl
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

n,wh=(0,)*3,(255,)*3
re,gr,bl=(255,0,0),(0,203,0),(0,0,255)

herbe=(148,255,99)
route,ligne=(123,125,123),(255,219,90)
chemin=(66,40,8)
caillou=(99,101,99)
cave=(123,105,74)
balle1,balle2=(0,0,255),(0,0,150)
touche1,touche2=(255,90,0),(255,200,0)
balle_enemi1,balle_enemi2=(255,0,0),(150,0,0)
p_c=[wh,n,(255,32,41),(255,203,140),(16,32,148),(247,105,41),(99,56,0),(255,255,0),bl,(123,125,123)]
passage_secret=(0,4,0)

pos_d=[[-50,-50,420,322,herbe],[135,-50,50,322,route],[158,-44,4,310,ligne],[180,86,240,50,route],[162,109,252,4,ligne],[420,101,300,20,chemin],[465,81,40,60,chemin],
[720,86,50,50,cave],[770,0,370,222,cave]]
pos_c=[[10,91,2],[475,101,1],[900,10,3],[800,170,2],[1040,165,1],[1060,175,1],[1045,195,1]]

game,new=True,True
x,y,m,t=0,0,20,2
grand=True
bm=[50,50,-50,-820]
KEY=[52,12,17,16]
#ok=4 sur numworks et 52 sur pc
#ok,mouvement flèche,changement de taille,options

#langage=1
difficulty=2
nd=difficulty
#stats=[0 for _ in range(5)]
#En succès, on aura pour le moment:
  #kill,schrink
#success=[0 for _ in range(2)]
#sb=[] #Success Buffer (to display them when you unlock them)
#cp=[-660,0,"123456",0]
#cb=[] #Checkpoints Buffer

e_l=[[40,70],[60,100],[80,120],[100,150],[130,170]]
pp=[[160-5*t,111-10*t,t,100,0],[1090,91,2]]
for i in range(1,len(pp)):pp[i].append(rd(e_l[nd][0]//10,e_l[nd][1]//10)*10),pp[i].append(0)
for i in range(1,len(pp)):
 if nd>2:
  for i1 in range(nd-2):
   pp.append([pp[i][0],pp[i][1]+20+(-2*(i1+1)+3)*60,1,rd(e_l[nd][0]//10,e_l[nd][1]//10)*10,0])
perso,ennemi=toad,minion
op,mf=0,True

pos_b,pos_t=[],[]
p_cld=[0,0.5,1,1.5,2.5]
cld=p_cld[nd]
cp=mn()-cld
p_st=[[0,0],[0.1,0.4],[0.3,0.7],[0.5,1],[0.5,2]]
st=mn()-uf(p_st[nd][0],p_st[nd][1])
p_rv=[[10,15],[5,10],[3,7],[1,4],[0,1]]
cld_crv=5
crv=mn()-cld_crv
p_d=[[35,45],[25,35],[15,25],[10,20],[5,15]]

e_cld=[5,3,2,1.5,0.5]
clde=e_cld[nd]
cpe=mn()-clde
e_st=[[1,2],[0.5,1.5],[0.5,1],[0.3,0.7],[0.1,0.3]]
ste=mn()-uf(e_st[nd][0],e_st[nd][1])
e_rv=[[0,0],[0,0],[0,0],[1,4],[3,7]]
e_d=[[5,15],[10,20],[15,25],[25,35],[35,45]]
m_c=[[0,1,0,0,0],[1,1,0,0,0],[1,1,0,1,0],[1,1,1,0,0],[1,1,1,1,1]]

def ent(x):
 if x-floor(x)>.5:return floor(x)+1
 elif x-floor(x)<=.5:return floor(x)
cs,sn=lambda x:round(cos(radians(x)),2),lambda x:round(sin(radians(x)),2)
add,sub=lambda a,b:a+b,lambda a,b:a-b
inf,sup=lambda a,b:a<=b,lambda a,b:a>=b
def draw_p(x,y,t,l):
 for a in range(len(l)):
  for b in range(len(l[0])):
   for i in range(1,10):
    if l[a][b]==i:fr(x+b*t,y+a*t,t,t,p_c[i-1])
def draw_f():
 dx,dy,t=pp[0][0],pp[0][1],pp[0][2]
 xf,yf,c=dx-3 if op==2 else dx+10*t+3 if op==0 else dx+5*t-2,dy-3 if op==1 else dy+20*t+3 if op==3 else dy+10*t-2,n if mf else wh
 [c1,c2]=[sub,add]if op==0 else[add,sub]if op==3 else[add,add]
 for a in range(len(fleche[0])):
  for b in range(len(fleche)):
   [cx,cy]=[a,b]if op in[1,3] else[b,a]
   if fleche[b][a]==1:fr(c1(xf,cx),c2(yf,cy),1,1,c)
def draw_o(cx,cy,t,l):
 for a in range(len(l)):
  for b in range(len(l[0])):
   if l[a][b]==1:fr(cx+b*t,cy+a*t,t,t,caillou)
   elif l[a][b]==4:fr(cx+b*t,cy+a*t,t,t,touche1)
   elif l[a][b]==5:fr(cx+b*t,cy+a*t,t,t,touche2)
def draw_d():
 fr(0,0,320,222,n)
 for ox,oy,w,h,c in pos_d:fr(ox+x,oy+y,w,h,c)
 for i in range(len(pos_c)):draw_o(pos_c[i][0]+x,pos_c[i][1]+y,pos_c[i][2],rocher)
col=[[balle1,balle2],[balle_enemi1,balle_enemi2]]
def draw_b(x,y,t,d,cl,l):
 rad=radians(360-d%360)
 px,py=cos(rad),sin(rad)
 cols,rows=len(l[0]),len(l)
 w,h=cols*t,rows*t
 palette=col[cl]
 corners=((0,0),(w,0),(0,h),(w,h))
 xs=[cx*px-cy*py for cx,cy in corners]
 ys=[cx*py+cy*px for cx,cy in corners]
 min_x,max_x=floor(min(xs)),floor(max(xs))+1
 min_y,max_y=floor(min(ys)),floor(max(ys))+1
 for dy in range(min_y,max_y+1):
  run_col,run_start=0,min_x
  for dx in range(min_x,max_x+1):
   sx,sy=dx*px+dy*py,-dx*py+dy*px
   ix,iy=floor(sx/t),floor(sy/t)
   val=l[iy][ix]if(0<=ix<cols and 0<=iy<rows)else 0
   if val!=run_col:
    if run_col!=0:fr(x+run_start,y+dy,dx-run_start,1,palette[run_col-1])
    run_col,run_start=val,dx
  if run_col!=0:fr(x+run_start,y+dy,max_x+1-run_start,1,palette[run_col-1])
 nx,ny=x+(cols-1)*t*px-(rows-1)*t*py,y+(cols-1)*t*py+(rows-1)*t*px
 return ent(nx),ent(ny)
def c_collision(bx,by,op,pt,i,px,py,t):
 ob=360-op%360
 cx,cy=cs(ob),sn(ob)
 for a in range(15*pt//2):
  for b in range(5*pt//2):
   nx,ny=ent(bx+a*pt*cx-b*pt*cy),ent(by+a*pt*cy+b*pt*cx)
   if gp(nx+x,ny+y)in[caillou]:
    pos_b.remove(pos_b[i])
    pos_t.append((pxo-x-5//2*pt,pyo-y-5//2*pt,2*pt,mn()))
    return 2
   if px<=nx<=px+10*t and py<=ny<=py+20*t:return 1
 return 0
def move(v):
 global new,x,y,op
 [d,dd,p,s],ok,[c1,c2,c3]=[x,pp[0][0],20,160-5*t]if v in[0,3]else[y,pp[0][1],10,111-10*t],0,[add,sub,inf]if v in[0,1]else[sub,add,sup]
 if mf:op=0 if v==3 else 1 if v==1 else 2 if v==0 else 3
 for i in range(p*t):
  mx,my=[-m,i,i,10*t+m-1],[i,-m,20*t+m-1,i]
  if not gp(pp[0][0]+mx[v],pp[0][1]+my[v])in[n,caillou]:ok+=1
 if ok==p*t:
  if c3(d,bm[v]) and dd==s:d=c1(d,m)
  else:dd=c2(dd,m)
  new=True
 [x,y,pp[0][0],pp[0][1]]=[d,y,dd,pp[0][1]]if v in[0,3]else[x,d,pp[0][0],dd]
 #for i in range(len(cp)):
 # if not cp[i][3] and cp[i][0]-40<x+160-(pp[0][0]+5*pp[0][2])<cp[i][0]+40 and cp[i][1]-40<y+111-(pp[0][1]+10*pp[0][2])<cp[i][1]+40:cp[i][3]=1;cb.append([i,mn()])
def change_t(i=0):
 global m,new,grand,t
 dx,dy,t=pp[0][0],pp[0][1],pp[0][2]
 if i==0:
  if gp(dx+10*t+m,dy+10*t)==chemin or gp(dx-m,dy+10*t)==chemin:
   if grand:
    m,pp[0][2],pp[0][0],pp[0][1],new,grand=10,1,dx+5,dy+10,True,False
    #if not succes[1]:success[1]=1;sb.append(["schrink",mn()])
#  elif gp(dx+10*t+m*3,dy+10*t)==route or gp(dx-m*3,dy+10*t)==cave:
#   if not grand:m,pp[0][2],pp[0][0],pp[0][1],new,grand=20,2,160-5*2,111-10*2,True,True
 else:
  if grand:m,pp[0][2],pp[0][0],pp[0][1],new,grand=10,1,dx+5,dy+10,True,False
  else:m,pp[0][2],pp[0][0],pp[0][1],new,grand=20,2,dx-5,dy-10,True,True
  t=pp[0][2]
def c_t():
 global new
 if len(pos_t)>0:
  for tx,ty,tt,temps in pos_t:
   if mn()-temps<1:draw_o(tx-5//2*tt+x,ty-5//2*tt+y,tt,touche)
   else:
    pos_t.remove((tx,ty,tt,temps))
    new=True
def c_b():
 global new,pxo,pyo,st,ste
 if len(pos_b)>0:
  for i,[px,py,pt,ob,c]in enumerate(pos_b):
   new=True
   if 0<px+x<320 and 0<py+y<222:
    px,py=px+int(cos(radians(ob))*12*pt),py-int(sin(radians(ob))*12*pt)
    pos_b[i][0],pos_b[i][1]=px,py
    pxo,pyo=draw_b(px+x,py+y,pt,ob,c,projectile)
   else:pos_b.remove(pos_b[i]);return
   if len(pp)>0:
    for i1,[dx,dy,t,vie,e]in enumerate(pp):
     if i1==0 or c!=0:continue
     collision=c_collision(px,py,ob,pt,i,dx,dy,t)
     if collision==1:
      pos_b.remove(pos_b[i])
      pos_t.append((dx if op==0 else dx+10*t if op==2 else pxo-x-5//2*pt,dy if op==3 else dy+20*t if op==1 else pyo-y-5//2*pt,pt*2,mn()))
      ste=mn()+uf(e_st[nd][0],e_st[nd][1])
      pp[i1][3],pp[i1][4]=vie-rd(p_d[nd][0],p_d[nd][1]),1
      #stats[1]+=1
      #if not success[0]:succes[0]=1;sb.append(["kill",mn()])
      for i2,[x2,y2,t2,v2,e2]in enumerate(pp):
       if e2==0 and sqrt((x2-dx)**2+(y2-dy)**2)<200:pp[i2][4]=1
      if pp[i1][3]<=0:pp.remove(pp[i1])#;stats[4]+=1
      break
     elif collision==2:return
   if len(pp)>1 and c==0 and collision==2:continue
   if c==1 and c_collision(px,py,ob,pt,i,pp[0][0]-x,pp[0][1]-y,pp[0][2])==1:
    pos_b.remove(pos_b[i])
    pos_t.append((px-15*pt,py+5*pt//2,pt*2,mn()))
    st=mn()+uf(p_st[nd][0],p_st[nd][1])
    pp[0][3]-=rd(e_d[nd][0],e_d[nd][1])
    #stats[3]+=1
    if pp[0][3]<=0:lose()
def c_a(dx,dy,t):
 def c_pe(dx,dy):
  dlx,dly,cx=dx-(pp[0][0]-x),dy-(pp[0][1]-y),[0,1,2,3]
  if dlx>=0:cx.remove(0)
  if dlx<=0:cx.remove(2)
  if dly>=0:cx.remove(3)
  if dly<=0:cx.remove(1)
  return ch(cx)*90
 def c_pa(dx,dy,t):
  px,py=pp[0][0]+5*pp[0][2],pp[0][1]+10*pp[0][2]
  dx,dy=dx+5*t,dy+7*t
  ag=degrees(atan2(-(py-y-dy),px-x-dx))
  if ag<0:ag+=360
  return ent(ag)
 if nd==0:ob=rd(0,4)*90
 if nd==1:
  if rd(0,1):ob=c_pe(dx,dy)
  else:ob=rd(0,4)*90
 if nd==2:ob=c_pe(dx,dy)
 if nd==3:
  if rd(0,1):ob=c_pe(dx,dy)
  else:ob=c_pa(dx,dy,t)
 if nd==4:ob=c_pa(dx,dy,t)
 return ob
def c_pos(dx,dy,t):
 e_hm=[[0,0],[0,5],[0,10],[0,15],[15,25]]
 e_vm=[[5,10],[5,15],[5,20],[5,25],[5,35]]
 gm=[[[770,1140],[0,222]]]#game border
 hrng,vrng,thd=100,80,10
 fn=-1
 for i in range(len(gm)):
  if gm[i][0][0] <= dx <= gm[i][0][1] and gm[i][1][0] <= dy <= gm[i][1][1]:fn=i;break
 if fn==-1:return dx,dy
 mnh,mxh=gm[fn][0][0],gm[fn][0][1]-10*t
 mnv,mxv=gm[fn][1][0],gm[fn][1][1]-20*t
 mx=my=0
#Pas de mode hardcore par manque d'espace en RAM
#vaut mieux pas de mode hardcore que pas de jeu...
 if m_c[nd][0]:
#  if m_c[nd][4]:
#   for px,py,pt,ob,c in pos_b:
#    if c!=0 or ob in[0,180]:continue
#    dly=(dy-10*t)-(py-8)
#    if[dly>0 and ob==90]or[dlx<0 and ob==270]:continue
#    dlx=(dx+5*t)-(px+3*pt)
  if m_c[nd][2]and mx==0:
   dlx=(dx+5*t)-(pp[0][0]+5*pp[0][2]-x)
   if fabs(dlx)>hrng+thd:mx=-rd(10,25)if dlx>0 else rd(10,25)
   if fabs(dlx)<hrng-thd:mx=rd(10,25)if dlx>0 else -rd(10,25)
  if mx==0:
   mx=rd(e_hm[nd][0],e_hm[nd][1])
   if rd(0,1):mx=-mx
 if m_c[nd][1]:
#  if m_c[nd][4]:
#   pass
  if m_c[nd][3]and my==0:
   dly=(dy+10*t)-(pp[0][1]+10*pp[0][2]-y)
   if fabs(dly)>vrng+thd:my=-rd(10,25)if dly>0 else rd(10,25)
   if fabs(dly)<vrng-thd:my=rd(10,25)if dly>0 else -rd(10,25)
  if my==0:
   my=rd(e_vm[nd][0],e_vm[nd][1])
   if rd(0,1):my=-my
 tp,ok=10*t if mx>0 else 0,0
 for i in range(20*t):
  if gp(dx+x+tp+mx,dy+y+i)not in[caillou]:ok+=1
 if ok==20*t:dx+=mx
 tp,ok=20*t if my>0 else 0,0
 for i in range(10*t):
  if gp(dx+x+i,dy+y+tp+my)not in[caillou]:ok+=1
 if ok==10*t:dy+=my
 dx,dy=min(max(dx,mnh),mxh),min(max(dy,mnv),mxv)
 return dx,dy
def c_e():
 global cpe,new
 if len(pp)>0:
  for i,[dx,dy,t,vie,e]in enumerate(pp):
   if i>0 and e==1:
    if mn()-cpe>=clde and len(pos_b)<5:
     ob=c_a(dx,dy,t)
     pos_b.append([dx+5*t-5//2*t,dy+8*t+y,t,ob,1])
     cpe,new=mn(),True
    if mn()-ste>=0:
     nx,ny=c_pos(dx,dy,t)
     if nx!=dx or ny!=dy:pp[i][0],pp[i][1],new=nx,ny,True
def lose():
 global game
 game=False
 fr(0,0,320,222,wh),ds("Perdu !",125,102)
 #if langage==1:ds("Perdu !",125,102)
 #if langage==1:ds("Game over !",105,102)
 #Faire en sorte d'aller vers les stats,
 #puis lorsqu'on appuie sur une touche
 #ça revient au menu principal en réinitialisant
 #les stats, les succès, eux, sont persistants
 #sl(3)
def c_v():
 global crv,new
 if len(pp)>0:
  if mn()-crv>=cld_crv:
   for i,[dx,dy,t,vie,e]in enumerate(pp):
    if i==0 and vie<100:
     rva=rd(p_rv[nd][0],p_rv[nd][1])
     if vie>100-rva:
      #stats[2]+=100-pp[0][3]
      pp[0][3]=100
     else:pp[0][3]+=rva#stats[2]+=rva
     new=True
    if i>0 and vie<e_l[nd][0]:
     rva=rd(e_rv[nd][0],e_rv[nd][1])
     if vie>e_l[nd][0]-rva:pp[i][3]=e_l[nd][0]
     else:pp[i][3]+=rva
     new=True
   crv=mn()
#def ds(): #Display Success
# if len(sb)>0:
#  db=[] #Delete Buffer
#  for n,[m,t]in enumerate(sb):
#   msg=""
#   if m=="kill":msg+="Tuer un ennemi"if langage==1 else "Kill an enemy"
#   elif m=="schrink":msg+="Se rapetisser"if langage==1 else "Get smaller"
#   msg+=" !"
#   if langage==1:ds("Succès accompli: ",150,0)
#   if langage==2:ds("Success accomplished: ",100,0)
#   ds(msg,320-len(msg)*10,(n+1)*18)
#   if t-mn()<-5:db.append(sb[n])
#  for i in db:sb.remove(i)
#def dc(): #Display Checkpoints
# if len(cb)>0:
#  for n,[i,t]in enumerate(cb):
#   msg="Cave"if langage==1 else "Cave"
#   msg+=": "+cb[i][2]
#   if langage==1:ds("Point de sauvegarde débloqué",40,0)
#   elif langage==2:ds("Checkpoint unlocked",130,0)
#   ds(msg,320-len(msg),18)
#   if t-mn()<-5:cb.remove(cb[n])

def jeu():
  global game,new,cp,cld,mf
  while game:
    if new:
      new=False
      draw_d()
      if len(pp)>0:
        for i,[dx,dy,t,vie,e]in enumerate(pp):
          [dx,dy,l]=[dx-x,dy-y,perso] if i==0 else [dx,dy,ennemi]
          if vie>0:draw_p(dx+x,dy+y,t,l)
          if i>0:ds(str(vie),dx+x,dy-20+y)
      draw_f(),change_t()
#      ds(str(x),0,0)
      msg="Vie"#if langage==1 else "Life"
      ds(msg,0,204),ds(":"+str(pp[0][3]),len(msg)*10,204),sl(0)
    c_b(),c_e(),c_t(),c_v()#,ds(),dc()
    if kd(KEY[0]) and mn()-st>=0:
      if mn()-cp>=cld:
        cp,new,t=mn(),True,pp[0][2]
        px,py=pp[0][0]+5*t-x-5//2*t,pp[0][1]+8*t-y
        px,py=px+3*t if op==3 else px,py+5*t if op==2 else py
        pos_b.append([px,py,t,op*90,0])
        #stats[0]=+1
    for i in range(4):
      if kd(i) and mn()-st>=0:move(i)
    if kd(KEY[1]):mf,new=False if mf==True else True,True
    if kd(KEY[2]):change_t(1),sl(0.1)
    if kd(KEY[3]):
      ds("manque la partie 1",70,101,re)
#      options,new_options,game=True,True,False
jeu()
