import pygame
import time
import random

pygame.init()

crashSound = pygame.mixer.Sound("crashsound.wav")

width = 800
height = 600

black = (0,0,0)
white = (255,255,255)
bright_red = (255,0,0)
red = (200,0,0)
green = (0,200,0)
bright_green = (0,255,0)
blue = (0,0,255)

block_color = (53,115,255)

car_width = 73

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("A bit Racey")
clock = pygame.time.Clock()

carimg = pygame.image.load("car2.png")
gameIcon = pygame.image.load("car2.png")

pygame.display.set_icon(gameIcon)

pause = False
#crash = True

def things_dodged(count):
	font = pygame.font.SysFont("comicsansms", 25)
	text = font.render("Dodged: " + str(count), True, black)
	screen.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(screen, color, [thingx, thingy, thingw, thingh])

def car(x,y):
	screen.blit(carimg, (x,y))

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

# def message_display(text):
# 	largeText = pygame.font.Font("freesansbold.ttf", 115)
# 	TextSurf, TextRect = text_objects(text, largeText)
# 	TextRect.center = ((width/2), (height/2))
# 	screen.blit(TextSurf, TextRect)

# 	pygame.display.update()
# 	time.sleep(2)
# 	game_loop()

def crash():
	pygame.mixer.Sound.play(crashSound)
	pygame.mixer.music.stop()

	largeText = pygame.font.SysFont("comicsansms", 115)
	TextSurf, TextRect = text_objects("Paused", largeText)
	TextRect.center = ((width/2),(height/2))
	screen.blit(TextSurf, TextRect)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		screen.fill(white)

		button("Play Again", 150,450,100,50,green,bright_green,game_loop)
		button("Quit", 550,450,100,50,red,bright_red,quitgame)

		pygame.display.update()
		clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(screen, ac, (x,y,w,h))
		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(screen, ic, (x,y,w,h))

	smallText = pygame.font.SysFont("comicsansms", 20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ((x+(w/2)), (y+(h/2)))
	screen.blit(textSurf, textRect)

def quitgame():
	pygame.quit()
	quit()

def unpause():
	global pause
	pygame.mixer.music.unpause()
	pause = False

def paused():
	pygame.mixer.music.pause()

	largeText = pygame.font.SysFont("comicsansms", 115)
	TextSurf, TextRect = text_objects("Paused", largeText)
	TextRect.center = ((width/2),(height/2))
	screen.blit(TextSurf, TextRect)

	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()


		screen.fill(white)

		button("Continue", 150,450,100,50,green,bright_green,unpause)
		button("Quit", 550,450,100,50,red,bright_red,quitgame)

		pygame.display.update()
		clock.tick(15)

def game_intro():
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		screen.fill(white)
		largeText = pygame.font.SysFont("comicsansms", 115)
		TextSurf, TextRect = text_objects("A bit Racey", largeText)
		TextRect.center = ((width/2), (height/2))
		screen.blit(TextSurf, TextRect)

		button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
		button("QUIT", 550, 450, 100, 50, red, bright_red, quitgame)

		pygame.display.update()
		clock.tick(15)

def game_loop():
	global pause

	pygame.mixer.music.load("jazz.wav")
	pygame.mixer.music.play(-1)

	x = (width * 0.45)
	y = (height * 0.8)
	x_change = 0

	thing_startx = random.randrange(0, width)
	thing_starty = -600
	thing_speed = 7
	thing_width = 100
	thing_height = 100

	thingCount = 1

	dodged = 0

	gameExit = False

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				if event.key == pygame.K_RIGHT:
					x_change = 5
				if event.key == pygame.K_p:
					pause = True
					paused()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change
		screen.fill(white)

		things(thing_startx, thing_starty, thing_width, thing_height, block_color)
		thing_starty += thing_speed
		car(x,y)
		things_dodged(dodged)

		if x > width - car_width or x < 0:
			crash()

		if thing_starty > height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0, width)
			dodged += 1
			thing_speed += 1
			thing_width += (dodged * 1.2)

		if y < thing_starty + thing_height:
			print('y crossover')

			if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
				print('x crossover')
				crash()

		pygame.display.update()
		clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()