import pygame
from pygame.locals import *
import math
import random

pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))

cursor1 = pygame.image.load('src/cursor.png')
cursor2 = pygame.image.load('src/cursor2.png')
cursor = pygame.image.load('src/cursor.png')
clock = pygame.time.Clock()
blue = pygame.image.load('src/blue.png')
green = pygame.image.load('src/green.png')
purple = pygame.image.load('src/purple.png')
red = pygame.image.load('src/red.png')
yellow = pygame.image.load('src/yellow.png')
empty = pygame.image.load('src/empty.png')
# mouse = pygame.image.load('resources/images/arrow.png')
keys = [False, False, False, False]
cursorpos = [0,0]
blocks = [blue, green, purple, red, yellow, empty, empty]
blocksdrawn = False
spacetrigger = False
blockcount = 0
currentblock = [x for x in range(0,6)]
score=0

class Block(object):
	def __init__(self, x, y):
		self.color = blocks[random.randint(0,len(blocks)-1)]
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

def createBlocks():
	
	for x in range (0,6):
		currentblock[x]= [y for y in range(0,10)]
		for y in range(0,10):
			currentblock[x][y]=Block(x,y)
def redraw():
	implementGravity()
	for x in range(0,6):
		for y in range(0,10):
			screen.blit(currentblock[x][y].color,currentblock[x][y].position)
font = pygame.font.Font(None, 36)
def writePosition(pos):
	text = font.render(str(pos[0]/50)+" "+str(pos[1]/50), 1, (255,255,255))
	screen.blit(text,[400,0])
def writeScore(score):
	text = font.render(str(score), 1, (255,255,255))
	screen.blit(text,[400,100])
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
def implementGravity():
	for y in range(0,9):
		for x in range(0,6):
			if currentblock[x][y+1]:
				if currentblock[x][y+1].color==empty and currentblock[x][y].color!=empty:
					currentblock[x][y+1].color = currentblock[x][y].color
					currentblock[x][y].color = empty
def horizontalCheck(score):
	for y in range(0,10):
		counter_x=0
		for x in range(0,6):
			if x==5:
				if counter_x>=2:
					for n in range(0,counter_x+1):
						currentblock[x-n][y].color=empty
				counter_x=0
				break
				return
			if currentblock[x][y].color!=empty and currentblock[x][y].color==currentblock[x+1][y].color:
				counter_x+=1				
			else:
				if counter_x>=2:
					score+=counter_x
					for n in range(0,counter_x+1):
						currentblock[x-n][y].color=empty
				counter_x=0
def verticalCheck(score):
	for x in range(0,6):
		counter_y=0
		for y in range(0,10):
			if y==9:
				if counter_y>=2:
					for n in range(0,counter_y+1):
						currentblock[x][y-n].color=empty
				counter=0
				break
				return
			if currentblock[x][y].color!=empty and currentblock[x][y].color==currentblock[x][y+1].color:
				counter_y+=1				
			else:
				if counter_y>=2:
					score+=counter_y
					for n in range(0,counter_y+1):
						currentblock[x][y-n].color=empty
				counter_y=0
def addNewRow():
	for x in range(0,6):
		currentblock[x].pop(0)
		currentblock[x].append(Block(x,9))
	redraw()

createBlocks()
initchecked = False	
while 1:
	screen.fill(0)
	redraw()
 	drawCursor()
 	horizontalCheck(score)
 	verticalCheck(score)
 	writePosition(cursorpos)
 	writeScore(score)
	pygame.display.flip()
	clock.tick(20)
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
			elif event.key==K_r:
				createBlocks()
			elif event.key==K_e:
				addNewRow()

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

