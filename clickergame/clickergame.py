from types import DynamicClassAttribute
import pygame
import random
import time
import os
import pygame.font 
from pygame.constants import MOUSEMOTION
from pygame.display import set_mode
from pygame.surface import Surface
from module import Game_tick
# initialize pygame
pygame.init()
pygame.display.init()
pygame.event.set_allowed([MOUSEMOTION])
# Form screen
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# get the default size
x, y = win.get_size()
win = pygame.display.set_mode((x,y),pygame.RESIZABLE)
font = pygame.font.Font('freesansbold.ttf', round(x/40))
gigmentalupgrade = 10000
gigmdron = 0
gigoreupgrade = 100000
gigodron = 0
openmenu = False
moneyinbank = 0.00
click_upgradecost = 5
banklvl = 0
fetchmulti = 2
posx,posy =0,0
bankupgrade = 2000
bulletspawny,bulletspawnx = x/2,y/2
droneupgrade = 1
drone = 0
oremulti = 1
ore = 0
collect = 0
dataupgrade = 200
oreupgrade = 5
money = 0.00
closetab =0
#money = 999999999990.00#testing
dronetype = 0
stealmulti = 1
multi  = 1
steal = 0
research = 0
stealupgrade = 500
metalmulti = 1

class dronestab (pygame.sprite.Sprite):
   def __init__(self):#create
      pygame.sprite.Sprite.__init__(self)
      global x,y,posx,posy,drone,droneupgrade
      self.image = pygame.Surface((x*.9, y*.9))#4x4 pixel square not lmao
      self.image.fill((200,200,200))
      self.rect = self.image.get_rect()
      self.rect.x =x*.05
      self.rect.y = y*0.05

   def update(self):
      global posx,posy,x,y,openmenu,closetab
      Text = font.render("drones+", 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.45,y*.1)
      win.blit(Text,TextRect.center)
      Text = font.render("X", 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.85,self.rect.y+self.rect.y/4)
      win.blit(Text,TextRect.center)
      #win.blit((),())#make red box
      posx,posy = pygame.mouse.get_pos()
      if posx >= self.rect.x+x*.8 and posx <= self.rect.x+x*.9 and posy <= self.rect.y+y*.1 and posy >= self.rect.y:
         openmenu = False
         closetab = 2
         self.kill()
         posx,posy = 0,0

class gigametal(pygame.sprite.Sprite):
   def __init__(self):#create
      pygame.sprite.Sprite.__init__(self)
      global x,y,posx,posy,gigmentalupgrade,droneupgrade
      self.image = pygame.Surface((x/6, y/8))#4x4 pixel square not lmao
      self.image.fill((100,100,100))
      self.rect = self.image.get_rect()
      self.rect.x = x/12
      self.rect.y = y/6*2

   def update(self):
      global posx,posy,x,y,money,collect,gigmentalupgrade,gigmdron,dronetype
      Text = font.render("£{0}".format(gigmentalupgrade), 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.1,y/2.5)
      win.blit(Text,TextRect.center)
      Text = font.render("Giga metal", 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.1,y/2.8)
      win.blit(Text,TextRect.center)
      posx,posy = pygame.mouse.get_pos()
      if openmenu == False:
         self.kill()
      if posx >= self.rect.x and posx <= self.rect.x + x/6 and posy <= self.rect.y+y/8 and posy >= self.rect.y and gigmentalupgrade <= money:
         money -=gigmentalupgrade
         gigmdron+=1
         gigmentalupgrade = gigmentalupgrade * 20
         dronetype = 5
         Metaldrone = metaldrone()
         drones.add(Metaldrone)
         all_sprites.add(Metaldrone)

class gigaore(pygame.sprite.Sprite):
   def __init__(self):#create
      pygame.sprite.Sprite.__init__(self)
      global x,y,posx,posy,gigmentalupgrade,droneupgrade
      self.image = pygame.Surface((x/6, y/8))#4x4 pixel square not lmao
      self.image.fill((100,100,100))
      self.rect = self.image.get_rect()
      self.rect.x = x/12
      self.rect.y = y/6*3

   def update(self):
      global posx,posy,x,y,money,gigoreupgrade,gigodron,dronetype
      Text = font.render("£{0}".format(gigoreupgrade), 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.1,y/5.4*3)
      win.blit(Text,TextRect.center)
      Text = font.render("Giga ore", 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.1,y/6*3)
      win.blit(Text,TextRect.center)
      posx,posy = pygame.mouse.get_pos()
      if openmenu == False:
         self.kill()
      if posx >= self.rect.x and posx <= self.rect.x + x/6 and posy <= self.rect.y+y/8 and posy >= self.rect.y and gigoreupgrade <= money:
         money -=gigoreupgrade
         gigodron+=1
         gigoreupgrade = gigoreupgrade * 20
         dronetype = -1
         Metaldrone = metaldrone()
         drones.add(Metaldrone)
         all_sprites.add(Metaldrone)

class graph(pygame.sprite.Sprite):
   def __init__(self):#create
      pygame.sprite.Sprite.__init__(self)
      global x,y,intrest,move
      self.image = pygame.Surface((x/6, y/4))#4x4 pixel square not lmao
      self.image.fill((100,100,100))
      self.rect = self.image.get_rect()
      self.rect.x = x/120
      self.rect.y = y/2+y/9
      intrest = y*.77
      self.change = [0,0]
      self.timer = 0
      move = False



   def update(self):
      global x,y,moneyinbank,intrest,move,bankintrest
      Text = font.render("value", 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x/30,y/2+y/8)
      win.blit(Text,TextRect.center)
      self.timer +=1
      if self.timer == 10:
         if intrest <= y*.7:
            intrest = y*.7
         elif intrest >= y*.85:
            intrest = y*.85
         intrest -= x/1000000*self.change[0]
         if self.change[1] == 0:
            self.change = [random.randint(-1000,1000),random.randint(10,100)]
            bankintrest = self.change[0]
         self.change[1] -=1
         move = True
         self.timer = 0
         Bar = bar()
         all_sprites.add(Bar)
      else:
         move = False

class bar(pygame.sprite.Sprite):
   def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      global x,y,intrest,bankintrest
      self.image = pygame.Surface((x/500,x/500))
      if bankintrest == 0 or research < 26:
         self.image.fill((255,255,0))
      elif bankintrest > 0:
         self.image.fill((0,255,0))
      else:
         self.image.fill((255,0,0))
      self.rect = self.image.get_rect()
      self.rect.x = x/6
      self.rect.y = intrest
   def update(self):
      if move == True:
         self.rect.x-=x/1000
      
      if self.rect.x < x/100:
         self.kill()


class Bullet(pygame.sprite.Sprite):#
                def __init__(self):#create
                    pygame.sprite.Sprite.__init__(self)
                    global x,y,bulletspawnx,bulletspawny
                    self.colour = random.randint(0,50)
                    self.image = pygame.Surface((10, 10))#4x4 pixel square
                    self.image.fill((self.colour+random.randint(10,50),self.colour+random.randint(10,50),self.colour+random.randint(10,50)))#colours it
                    self.rect = self.image.get_rect()#creates a rectange around it
                    self.rect.x = bulletspawnx
                    self.rect.y = bulletspawny
                    self.timer=1
                    self.rand = random.randint(0,20)
                    self.speedx = random.randint(-36,36)/1800*y
                    self.speedy = random.randint(-36,36)/1800*y
                    if self.speedy > 13 and self.speedx > 17:
                            self.speedy -=4
                            self.speedx -=4
                    elif self.speedy < -13 and self.speedx < -17:
                            self.speedy +=4
                            self.speedx +=4

                def update(self):
                    self.timer+=1
                    self.rect.centery += self.speedy
                    self.rect.centerx += self.speedx
                    self.speedy += self.timer*0.1
                    if self.speedx > 0:
                       self.speedx -= self.timer*0.01*self.rand
                    elif self.speedx < 0:
                       self.speedx += self.timer*0.01*self.rand
                    if self.timer +random.randint(1,300) >=300:#if it goes of screen
                       self.kill()

class Dronestation(pygame.sprite.Sprite):
   def __init__(self):#create
      pygame.sprite.Sprite.__init__(self)
      global x,y,posx,posy,drone,droneupgrade
      self.image = pygame.Surface((x/6, y/8))#4x4 pixel square not lmao
      self.image.fill((100,100,100))
      self.rect = self.image.get_rect()
      self.rect.x = x-x/6
      self.rect.y = 20

   def update(self):
      global posx,posy,x,y,money,droneupgrade,drone,dronetype
      Text = font.render("£{0}".format(droneupgrade), 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.84,y/10)
      win.blit(Text,TextRect.center)
      Text = font.render("metal drones", 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.84,y/20)
      win.blit(Text,TextRect.center)
      posx,posy = pygame.mouse.get_pos()
      if posx > x-x/6 and posy < y/8 and droneupgrade <= money and openmenu == False:
         money -=droneupgrade
         drone+=1
         droneupgrade = droneupgrade * 2
         dronetype = 0
         Metaldrone = metaldrone()
         all_sprites.add(Metaldrone)
         drones.add(Metaldrone)

class bank(pygame.sprite.Sprite):
   def __init__(self):#create
      pygame.sprite.Sprite.__init__(self)
      global x,y,posx,posy,bankupgrade,banklvl
      self.image = pygame.Surface((x/6, y/4))
      self.image.fill((100,100,100))
      self.rect = self.image.get_rect()
      self.rect.x = 10
      self.rect.y = y/6*2
      self.moneyinbank = 0
      self.timer = 0

   def update(self):
      global posx,posy,x,y,money,bankupgrade,banklvl,moneyinbank
      self.timer +=1
      moneyinbank = round(moneyinbank)
      if self.timer == 10 and bankintrest != 0:
         moneyinbank= round(moneyinbank*((0.0001*banklvl*bankintrest/25)+1))
         self.timer = 0
      Text = font.render("£{0}".format(bankupgrade), 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*0.005+10,y/2.5)
      win.blit(Text,TextRect.center)
      if banklvl == 0:
         Text = font.render("unlock bank", 1,(0,0,0))
         TextRect = Text.get_rect()
         TextRect.center = (x*0.005+3,y/2.8)
         win.blit(Text,TextRect.center)
      else:
         Text = font.render("upgrade bank", 1,(0,0,0))
         TextRect = Text.get_rect()
         TextRect.center = (x*0.005+3,y/2.8)
         win.blit(Text,TextRect.center)
         Text = font.render("invest", 1,(0,0,0))
         TextRect = Text.get_rect()
         TextRect.center = (x*0.005+10,y/2.2)
         win.blit(Text,TextRect.center)
         Text = font.render("draw", 1,(0,0,0))
         TextRect = Text.get_rect()
         TextRect.center = (x*0.1,y/2.2)
         win.blit(Text,TextRect.center)
         Text = font.render("£{0}".format(moneyinbank), 1,(0,0,0))
         TextRect = Text.get_rect()
         TextRect.center = (x*0.006,y/2)
         win.blit(Text,TextRect.center)
      posx,posy = pygame.mouse.get_pos()
      
      if posx >= self.rect.x and posx <= self.rect.x + x/6 and posy <= self.rect.y+y/8 and posy >= self.rect.y and bankupgrade <= money and openmenu == False:
         money -=bankupgrade
         banklvl +=1
         bankupgrade =bankupgrade*10
      elif posx >= self.rect.x and posx <= self.rect.x + x/12 and posy <= self.rect.y+y/4 and posy >= self.rect.y+y/8 and banklvl >0 and openmenu == False:
         if money/banklvl <= 300:
            moneyinbank += money
            money = 0
         else:
            moneyinbank += money*0.10
            money = money*0.9
         self.timer = 0
      elif posx >= self.rect.x+x/12 and posx <= self.rect.x + x/6 and posy <= self.rect.y+y/4 and posy >= self.rect.y+y/8 and banklvl >0  and openmenu == False:
         money += moneyinbank
         moneyinbank = 0



class selldata(pygame.sprite.Sprite):
   def __init__(self):#create
      pygame.sprite.Sprite.__init__(self)
      global x,y,posx,posy,drone,droneupgrade
      self.image = pygame.Surface((x/6, y/8))#4x4 pixel square not lmao
      self.image.fill((100,100,100))
      self.rect = self.image.get_rect()
      self.rect.x = x-x/6
      self.rect.y = y/6*2

   def update(self):
      global posx,posy,x,y,money,collect,dataupgrade,dronetype
      Text = font.render("£{0}".format(dataupgrade), 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.84,y/2.5)
      win.blit(Text,TextRect.center)
      Text = font.render("fetch data", 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.84,y/2.8)
      win.blit(Text,TextRect.center)
      posx,posy = pygame.mouse.get_pos()
      if posx >= self.rect.x and posx <= self.rect.x + x/6 and posy <= self.rect.y+y/8 and posy >= self.rect.y and dataupgrade <= money and openmenu == False:
         money -=dataupgrade
         collect+=1
         dataupgrade = dataupgrade * 2
         dronetype = 2
         Metaldrone = metaldrone()
         all_sprites.add(Metaldrone)



class betterdrones (pygame.sprite.Sprite):
   def __init__(self):#create
      pygame.sprite.Sprite.__init__(self)
      global x,y,posx,posy,drone,droneupgrade
      self.image = pygame.Surface((x/6, y/8))#4x4 pixel square not lmao
      self.image.fill((100,100,100))
      self.rect = self.image.get_rect()
      self.rect.x = x-x/6
      self.rect.y = y-y/8

   def update(self):
      global posx,posy,x,y,openmenu
      Text = font.render("drones+", 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.84,y-y/16)
      win.blit(Text,TextRect.center)
      posx,posy = pygame.mouse.get_pos()
      if posx >= self.rect.x and posx <= self.rect.x + x/6 and posy <= self.rect.y+y/8 and posy >= self.rect.y and openmenu == False:
         openmenu = True
         Dronestab =dronestab()
         all_sprites.add(Dronestab)
         drones.add(Dronestab)
         dronestabgroup.add(Dronestab)
         gigmet= gigametal()
         all_sprites.add(gigmet)
         drones.add(gigmet)
         dronestabgroup.add(gigmet)
         Gigaore = gigaore()
         drones.add(Gigaore)
         dronestabgroup.add(Gigaore)

class save(pygame.sprite.Sprite):
   def __init__(self):#create
      pygame.sprite.Sprite.__init__(self)
      global x,y,posx,posy,drone,droneupgrade
      self.image = pygame.Surface((x/6, y/8))#4x4 pixel square not lmao
      self.image.fill((100,100,100))
      self.rect = self.image.get_rect()
      self.rect.x = 10
      self.rect.y = y-y/8
      self.timer = 0

   def update(self):
      global posx,posy,x,y,money,steal,ore,multi,research,collect,steal,drone,gigodron,gigmdron
      if self.timer == 0:
         Text = font.render("SAVE", 1,(0,0,0))
      else:
         self.timer-=1
         Text = font.render("SAVED",1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (self.rect.x+x/25,y-y/14)
      win.blit(Text,TextRect.center)
      posx,posy = pygame.mouse.get_pos()
      if posx >= self.rect.x and posx <= self.rect.x + y/6 and posy <= self.rect.y+y/8 and posy >= self.rect.y  and openmenu == False or research>15 and random.randint(0,500) == 0 or research > 13 and random.randint(0,1000) == 0:
         self.timer = 20
         #delete file
         if os.path.exists("savefile.txt"):
            os.remove("savefile.txt")
         #create new file
         data = [round(money+moneyinbank),multi,research,drone,ore,collect,steal,banklvl,gigmdron,gigodron]
         file  = open("savefile.txt", "a")
         for i in range(10):
            word = str(data[i])+"\n"
            file.writelines(word)
         file.close()


class stealdata(pygame.sprite.Sprite):
   def __init__(self):#create
      pygame.sprite.Sprite.__init__(self)
      global x,y,posx,posy,drone,droneupgrade
      self.image = pygame.Surface((x/6, y/8))#4x4 pixel square not lmao
      self.image.fill((100,100,100))
      self.rect = self.image.get_rect()
      self.rect.x = x-x/6
      self.rect.y = y/2

   def update(self):
      global posx,posy,x,y,money,steal,stealupgrade,dronetype
      Text = font.render("£{0}".format(stealupgrade), 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.84,y/2+y/20)
      win.blit(Text,TextRect.center)
      Text = font.render("steal data", 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.84,y/2)
      win.blit(Text,TextRect.center)
      posx,posy = pygame.mouse.get_pos()
      if posx >= self.rect.x and posx <= self.rect.x + y/6 and posy <= self.rect.y+y/8 and posy >= self.rect.y and stealupgrade <= money and openmenu == False:
         money -=stealupgrade
         steal+=1
         stealupgrade = stealupgrade * 10
         dronetype = 3
         Metaldrone = metaldrone()
         all_sprites.add(Metaldrone)

class oremine(pygame.sprite.Sprite):
   def __init__(self):#create
      pygame.sprite.Sprite.__init__(self)
      global x,y,posx,posy,drone,droneupgrade
      self.image = pygame.Surface((x/6, y/8))#fix this
      self.image.fill((100,100,100))
      self.rect = self.image.get_rect()
      self.rect.x = x-x/6
      self.rect.y = 40+y/8

   def update(self):
      global posx,posy,x,y,money,oreupgrade,ore,dronetype
      Text = font.render("£{0}".format(oreupgrade), 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.84,y/4.2)
      win.blit(Text,TextRect.center)
      Text = font.render("ore drones", 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.84,y/5.2)
      win.blit(Text,TextRect.center)
      posx,posy = pygame.mouse.get_pos()
      if posx > x-x/6 and posy < y/8*2+20 and posy > y/8+20 and oreupgrade <= money and openmenu == False:
         money -=oreupgrade
         ore+=1
         oreupgrade = oreupgrade * 10
         dronetype = 1
         Metaldrone = metaldrone()
         all_sprites.add(Metaldrone)
         drones.add(Metaldrone)
         dronetype = True



class upgradebutton(pygame.sprite.Sprite):
   def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      global money,x,y,research
      self.image = pygame.Surface((x/6, y/8))#fix this
      self.image.fill((100,100,100))
      self.rect = self.image.get_rect()
      self.rect.x = x/2-x/12
      self.rect.y = y*.6

   def update(self):
      global posx,posy,x,y,money,research,metalmulti,oremulti,fetchmulti,stealmulti
      if research == 0:
         self.cost = 1
         self.text = "unlock research"
      elif research == 1:
         self.cost = 5
         self.text = "metal x2 money"
      elif research == 2:
         self.cost = 20
         metalmulti = 2
         self.text = "ore x2 speed"
      elif research == 3:
         self.cost = 100
         self.text = "x2 collect speed"
      elif research == 4:
         self.text = "x4 metal money"
         metalmulti = 4
         self.cost = 200
      elif research == 5:
         self.cost = 450
         self.text = "20% faster drones"
      elif research == 6:
         self.cost = 1000
         self.text = "x2 ore money"
      elif research == 7:
         self.cost = 1100
         self.text = "20% faster return"
      elif research == 8:
         self.cost = 2000
         self.text = "upgrade reaserch"
      elif research == 9:
         self.cost = 2100
         self.text ="randomly money"
      elif research == 10:
         self.cost = 4000
         self.text = "more random money"
      elif research == 11:
         self.cost = 7500
         self.text = "more random cash"
      elif research ==12:
         self.cost = 2500
         self.text = "x4 ore money"
      elif research == 13:
         self.cost = 10000
         self.text = "autosave"
      elif research == 14:
         self.cost = 12500
         self.text = "upgrade research"
      elif research == 15:
         self.cost = 15000
         self.text = "autosave+"
      elif research == 16:
         self.cost = 8000
         self.text = "10x metal money"
      elif research == 17:
         self.cost = 25000
         self.text = "10x ore money"
      elif research == 18:
         self.cost  = 20000
         self.text  = "25x metal money"
      elif research == 19:
         self.cost = 40000
         self.text = "2x fetch money"
      elif research == 20:
         self.cost = 50000
         self.text = "2x steal money"
      elif research == 21:
         self.cost = 100000
         self.text = "4x fetch money"
      elif research == 22:
         self.cost = 100001
         self.text = "upgrade research"
      elif research == 23:
         self.cost = 250000
         self.text = "10x fetch money"
      elif research == 24:
         self.cost = 750000
         self.text = "5x steal money"
      elif research == 25:
         self.text = "upgrade graph"
         self.cost = 100000
      elif research == 26:
         self.cost = 225000
         self.text = "25x ore money"
      elif research == 27:
         self.text = "50x metal money"
         self.cost = 500000
      elif research == 28:
         self.cost = 1000000
         self.text = "10x steal money"
      elif research == 29:
         self.text = "25x fetch money"
         self.cost = 750000
      elif research== 30:
         self.text = "100x metal money"
         self.cost = 250000
      else:
         self.text = "Fully upgraded"
         self.cost = 0
         #ore multi
      if research > 26:
         oremulti = 25
      elif research > 17:
         oremulti = 10
      elif research > 12:
         oremulti = 4
      elif research > 6:
         oremulti = 2
      #metal multi
      if research > 30:
         metalmulti = 100
      elif research >27:
         metalmulti = 50
      elif research > 18:
         metalmulti = 25
      elif research > 16:
         metalmulti = 10
      elif research > 4:
         metalmulti = 4
      elif research > 2:
         metalmulti = 2
      #fetch multi
      if research > 28:
         fetchmulti = 25
      elif research > 23:
         fetchmulti = 10
      elif research > 21:
         fetchmulti = 4
      elif research > 19:
         fetchmulti = 2
      #steal multi
      if research > 29:
         stealmulti = 10
      elif research > 23:
         stealmulti = 5
      elif research > 20:
         stealmulti = 2
      Font = pygame.font.Font('freesansbold.ttf', round(x/60))
      Text = font.render("£{0}".format(self.cost), 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.43,y*.65)
      win.blit(Text,TextRect.center)
      Text = Font.render(self.text, 1,(0,0,0))
      TextRect = Text.get_rect()
      TextRect.center = (x*.43,y*.6)
      win.blit(Text,TextRect.center)
      posx,posy = pygame.mouse.get_pos()
      if posx >= self.rect.x and posx <= self.rect.x + x/6 and posy >= self.rect.y and posy <= self.rect.y+y/8 and self.cost <= money and self.cost != 0  and openmenu == False:
         research+=1
         money -= self.cost




class metaldrone(pygame.sprite.Sprite):
   def __init__(self):#create
      pygame.sprite.Sprite.__init__(self)
      global x,y,posx,posy,drone,droneupgrade,money,dronetype
      if dronetype == 0:
         self.image = pygame.Surface((x/100, x/100))
      elif dronetype == 2 or dronetype == 3:
         self.image = pygame.Surface((x/50,y/100))
      elif dronetype == 5:
         self.image = pygame.Surface((x/35,x/35))
      elif dronetype == -1:
         self.image = pygame.Surface((x/25,x/25))
      else:
         self.image = pygame.Surface((x/50,x/50))
      self.colour = droneupgrade
      self.dronetype = dronetype
      self.timer = 0
      if self.colour > 255:
         self.colour = 255
      self.collect = 0.00
      if dronetype <= 1:
         self.image.fill((self.colour,0,0))
      elif dronetype == 2:
         self.image.fill((0,self.colour,0))
      else:
         self.image.fill((0,0,self.colour))
      self.rect = self.image.get_rect()
      self.rect.x = x-x/6
      if self.dronetype == 1 and research < 3:
         self.speed = x/1000
         self.rect.y = random.randint(0,round(y/8))+ y/8+20
      elif self.dronetype <= 1 and self.dronetype != 0:
         self.speed=x/500
         self.rect.y = random.randint(0,round(y/8))+ y/8+20
      elif self.dronetype >= 2 and self.dronetype != 5:
         self.rect.y = random.randint(20,20 +round(y/8))+y/(5.2-self.dronetype)
      else:
         self.speed = x/500
         self.rect.y = random.randint(20,20 +round(y/8))


   def update(self):
      global money,bulletspawnx,bulletspawny,multi,metalmulti,research,x,y,oremulti
      if self.dronetype <= 1 and research >= 3:
         self.speed = x/500
      if research >= 5 and self.dronetype <= 1 or self.dronetype == 5:
         self.speed = x/400
      elif self.dronetype == 2 and self.rect.x == 0 or self.dronetype == 3 and self.rect.x == 0:
         self.rect.x = -x/100
      elif self.dronetype == 2 or self.dronetype == 3:
         self.speed = x/self.rect.x
         self.image.fill((0,self.colour,0))
      self.colour=drone*10
      if self.colour > 255:
         self.colour = 255
      if self.dronetype <= 1 and self.dronetype != 5: 
        self.image.fill((0,self.colour/2,self.colour))
      elif self.dronetype == 3:
         pygame.draw.rect(win, (0,self.colour,0), (self.rect.centerx,self.rect.centery-x/200, x/100, y/50))
      elif self.dronetype == 2 or self.dronetype == 3:
         self.image.fill((0,self.colour,0))
      else:
         self.image.fill((self.colour,0,0))
      if self.collect < 5 and self.rect.x < x/7 and self.dronetype != 2 and self.dronetype != 3 or self.collect < 5 and self.rect.x < -x/50:
         self.collect += random.randint(1,20)*0.001
         if research > 3:
            self.collect += random.randint(1,20)*0.001
         self.timer+=1
         if self.timer == 10 and self.rect.x > 0 and self.dronetype <= 1 or self.timer == 10 and self.rect.x > 0 and self.dronetype == 5 :
            bulletspawnx,bulletspawny = self.rect.x,self.rect.y
            metal = Bullet()
            all_sprites.add(metal)
            self.timer = 0
      elif self.rect.x >x-x/6:
         self.rect.x = x-x/6
         if self.dronetype == 0:#metal
            self.collect = 0
            money += multi*metalmulti
         elif self.dronetype == 2:#fetch
            self.collect = -20
            money += 50*multi*fetchmulti
         elif self.dronetype == 3:#steal
            self.collect = -100
            money += 500*multi*stealmulti
         elif self.dronetype == 5:#gigametal
            self.collect = -20
            money += 30*multi*metalmulti
         elif self.dronetype == -1:#giga ore
            money+=40*multi*oremulti
            self.collect = -40
         else:#ore
            self.collect = -10
            money += 25*multi*oremulti
      elif self.collect >0 and research > 7:
         self.rect.x += x/400
      elif self.collect > 0:
         self.rect.x += x/500
      else:
         self.rect.x -= self.speed
drones = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
dronestabgroup = pygame.sprite.Group()
droneSta = Dronestation()
metal = Bullet()
Oremine =oremine()
Stealdata = stealdata()
Selldata =selldata()
Metaldrone = metaldrone()
researchbutton=  upgradebutton()
savebutton = save()
Bank =bank()
better = betterdrones()
Graph=graph()
all_sprites.add(Graph)
all_sprites.add(better)
all_sprites.add(Bank)
all_sprites.add(savebutton)
all_sprites.add(researchbutton)
all_sprites.add(Stealdata)
all_sprites.add(Selldata)
all_sprites.add(droneSta)
all_sprites.add(Oremine)

#savefile

if os.path.exists("savefile.txt"):
   data = []
   file1 = open('savefile.txt', 'r')
   Lines = file1.readlines()
 
   count = 0
   for line in Lines:
    count += 1
    data.append(int(line.strip()))
   print(data)
   money =data[0]
   multi = data[1]
   research = data[2]
   for i in range(multi):
      click_upgradecost = click_upgradecost*10
   click_upgradecost= click_upgradecost/10
   drone = data[3]
   for i in range(drone-1):
      dronetype = 0
      Metaldrone = metaldrone()
      all_sprites.add(Metaldrone)
      drones.add(Metaldrone)
      droneupgrade = droneupgrade*2
   ore = data[4]
   for i in range(ore-1):
      dronetype = 1
      Metaldrone = metaldrone()
      drones.add(Metaldrone)
      all_sprites.add(Metaldrone)
      oreupgrade = oreupgrade*10
   collect = data[5]
   for i in range(collect-1):
      dronetype = 2
      Metaldrone = metaldrone()
      all_sprites.add(Metaldrone)
      dataupgrade = dataupgrade*2
   steal = data[6]
   for i in range(steal-1):
      dronetype = 3
      Metaldrone = metaldrone()
      all_sprites.add(Metaldrone)
      stealupgrade = stealupgrade*10
   banklvl=data[7]#bank
   for i in range(banklvl):
      bankupgrade=bankupgrade*10
   gigmdron = data[8]
   for i in range(gigmdron):
      dronetype = 5
      Metaldrone = metaldrone()
      drones.add(Metaldrone)
      all_sprites.add(Metaldrone)
      gigmentalupgrade = gigmentalupgrade*20
   gigodron = data[9]
   for i in range(gigodron):
      dronetype = -1
      Metaldrone = metaldrone()
      drones.add(Metaldrone)
      all_sprites.add(Metaldrone)
      gigoreupgrade = gigoreupgrade*20

      

   file1.close()
   #data = [money,multi,research,drone,ore,collect,steal]

run = True
dostuff = False

while True:
   click_upgradecost = int(click_upgradecost)
   Game_tick(.03)
   win.fill((255,255,255))
   if research >= 11 and random.randint(1,250) == 250:
      money += 150
   elif research == 10 and random.randint(0,500)== 500:
      money += 100
   elif research == 9 and random.randint(0,1000) == 1000:
       money += 100
   for event in pygame.event.get():
      if event.type == pygame.MOUSEMOTION:
         posx,posy = pygame.mouse.get_pos()
      else:
         posx,posy =x/2,y/2
   if posx <= x/7 and posy <= y/3.5 and openmenu == False:
      money += 0.01*multi
      bulletspawnx,bulletspawny = posx,posy
      metal = Bullet()
      all_sprites.add(metal)
      posx,posy = x/2,y/2
   elif posx >= x/3*1.25 and posx <= x/3*1.25+x/6 and posy >= y/5*3.9 and posy <= y/5*3.9 + y/8 and money >= click_upgradecost  and openmenu == False:
      money -=click_upgradecost
      click_upgradecost *= 10
      multi += 1
      dostuff = True
   

   if dostuff == True:
      pygame.draw.rect(win, (255, 255, 0), (x/3*1.25,y/5*3.9 , x/6, y/8))
      pygame.display.update()
      time.sleep(0.2)
   dostuff = False
   if openmenu == False:
      all_sprites.draw(win)
      all_sprites.update()
      text = font.render('UPGRADE', 0, (0,0,0))
      pygame.draw.rect(win, (55, 55, 55), (x/3*1.25,y/5*3.9 , x/6, y/8))
      win.blit(text,(x/2.3,y/5*4))
      text = font.render("£{0}".format(click_upgradecost), 0, (0,0,0))
      win.blit(text,(x/2.3,y/5*4.2))
      text = font.render('    Mine', 0, (0,0,0))
      pygame.draw.rect(win, (55, 55, 55), (20,20 , x/7, y/3.5))
   else:
      dronestabgroup.draw(win)
      drones.update()
   win.blit(text,(x/54,y/7))
   money = round(money, 2)
   Text = font.render("£{0}".format(money), 1,(0,0,0))
   TextRect = Text.get_rect()
   TextRect.center = (x-x*2/3,y/2)
   win.blit(Text,TextRect.center)
   pygame.display.flip()
   closetab -=1
   if closetab == 0:
      time.sleep(1)
      closetab = False