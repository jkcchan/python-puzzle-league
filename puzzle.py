import pygame
from pygame.locals import *
import math
import random

pygame.init()
width, height = 501, 501
screen = pygame.display.set_mode((width, height))

cursor = pygame.image.load('cursor.png')
clock = pygame.time.Clock()
blue = pygame.image.load('blue.png')
green = pygame.image.load('green.png')
purple = pygame.image.load('purple.png')
red = pygame.image.load('red.png')
yellow = pygame.image.load('yellow.png')
# mouse = pygame.image.load('resources/images/arrow.png')
keys = [False, False, False, False]
cursorpos = [0,0]
blocks = [blue, green, purple, red, yellow]
blocksdrawn = False

class Block(object):
	def __init__(self, x, y):
		self.color = blocks[random.randint(0,4)]
		self.position = [50*x,50*y]
# if(blocksdrawn is False):
# 	for x in range(0,9):
# 		currentblock[x] = Block()
# 		currentblock[x].position = [50*x,0]
# 	blocksdrawn = True
currentblock = [x for x in range(0,6)]
for x in range (0,6):
	currentblock[x]= [y for y in range(0,10)]
	for y in range(0,10):
		currentblock[x][y]=Block(x,y)

while 1:

	# for x in range(width/grass.get_width()+1):
	# 	for y in range(height/grass.get_height()+1):
	# 		screen.blit(grass,(x*100, y*100))
	screen.fill(0)

	for x in range(0,6):
		for y in range(0,10):
			screen.blit(currentblock[x][y].color,currentblock[x][y].position)
	screen.blit(cursor,cursorpos)
	# for bullet in arrows:
	# 	index=0
	# 	velx=math.cos(bullet[0])*10
	# 	vely=math.sin(bullet[0])*10
	# 	bullet[1]+=velx
	# 	bullet[2]+=vely
	# 	if bullet[1]<-64 or bullet[1]>500 or bullet[2]<-64 or bullet[2]>500:
	# 		arrows.pop(index)
	# 	index+=1
	# 	for projectile in arrows:
	# 		arrow1=pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
	# 		screen.blit(arrow1, (projectile[1], projectile[2]))
	# if badtimer==0:
	# 	badguys.append([500, random.randint(50,500)])
	# 	badtimer=100-(badtimer1*2)
	# 	if badtimer1>=35:
	# 		badtimer1-35
	# 	else:
	# 		badtimer1+=5
	# index=0
	# for badguy in badguys:
	# 	if badguy[0]<-64:
	# 		badguys.pop(index)
	# 	badguy[0]-=7
	# 	index+=1
	# for badguy in badguys:
	# 	screen.blit(badguyimg, badguy)
	# screen.blit(mouse, mousepos)
	# badtimer-=1
	pygame.display.flip()
	clock.tick(30)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type == pygame.KEYDOWN:
			if event.key == K_w:
				keys[0] = True
			elif event.key == K_a:
				keys[1] = True
			elif event.key == K_s:
				keys[2] = True
			elif event.key == K_d:
				keys[3] = True
		if event.type == pygame.KEYUP:
			if event.key == K_w:
				keys[0] = False
			elif event.key == K_a:
				keys[1] = False
			elif  event.key == K_s:
				keys[2] = False
			elif event.key == K_d:
				keys[3] = False
	if keys[0]:
		cursorpos[1]-=50
		keys[0]=False
	elif  keys[2]:
		cursorpos[1]+=50
		keys[2]=False
	elif keys[1]:
		cursorpos[0]-=50
		keys[1]=False
	elif keys[3]:
		cursorpos[0]+=50
		keys[3]=False
