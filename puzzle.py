import pygame
from pygame.locals import *
import math
import random

pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))

cursor1 = pygame.image.load('cursor.png')
cursor2 = pygame.image.load('cursor2.png')
cursor = pygame.image.load('cursor.png')
clock = pygame.time.Clock()
blue = pygame.image.load('blue.png')
green = pygame.image.load('green.png')
purple = pygame.image.load('purple.png')
red = pygame.image.load('red.png')
yellow = pygame.image.load('yellow.png')
empty = pygame.image.load('empty.png')
# mouse = pygame.image.load('resources/images/arrow.png')
keys = [False, False, False, False]
cursorpos = [0,0]
blocks = [blue, green, purple, red, yellow, empty, empty, empty, empty, empty]
blocksdrawn = False
spacetrigger = False
blockcount = 0

class Block(object):
	def __init__(self, x, y):
		self.color = blocks[random.randint(0,9)]
		self.position = [50*x,50*y]

def checkPositionOverflow_x(direction):
	if cursorpos[0]+50*direction>=0 and cursorpos[0]+50*direction<250:
		return True
	else:
		return False
def checkPositionOverflow_y(direction):
	if cursorpos[1]+50*direction>=0 and cursorpos[1]+50*direction<500:
		return True
	else:
		return False
def switchBlocks(indeces):

	block_x = indeces[0]
	block_y = indeces[1]
	temp=currentblock[block_x+1][block_y].color
	currentblock[block_x+1][block_y].color = currentblock[block_x][block_y].color
	currentblock[block_x][block_y].color = temp

currentblock = [x for x in range(0,6)]
for x in range (0,6):
	currentblock[x]= [y for y in range(0,10)]
	for y in range(0,10):
		currentblock[x][y]=Block(x,y)
def redraw():
	for x in range(0,6):
		for y in range(0,10):
			screen.blit(currentblock[x][y].color,currentblock[x][y].position)
font = pygame.font.Font(None, 36)
text = font.render('asdf',1,(255,255,255))
def writePosition():
	font = pygame.font.Font(None, 36)
	text = font.render(str(cursorpos[0]%50)+" "+str(cursorpos[1]%50), 1, (255,255,255))
	screen.blit(text,[500,0])

def getBlock():
	for x in range(0,6):
		for y in range(0,10):
			if currentblock[x][y].position == cursorpos:
				return [x,y]

def drawCursor():
	if int(pygame.time.get_ticks())%1000 <500:
		cursor = cursor1
	else:
		cursor = cursor2
	screen.blit(cursor,cursorpos)
while 1:

	screen.fill(0)
	screen.blit(text,[300,0])

	redraw()
 	drawCursor()
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
			elif event.key==K_SPACE:
				spacetrigger = True
	if keys[0]:
		if checkPositionOverflow_y(-1):
			cursorpos[1]-=50
		keys[0]=False
	elif  keys[2]:
		if checkPositionOverflow_y(1):
			cursorpos[1]+=50
		keys[2]=False
	elif keys[1]:
		if checkPositionOverflow_x(-1):
			cursorpos[0]-=50
		keys[1]=False
	elif keys[3]:
		if checkPositionOverflow_x(1):
			cursorpos[0]+=50
		keys[3]=False
	elif spacetrigger:
		xy = getBlock()
		switchBlocks(xy)
		spacetrigger = False

