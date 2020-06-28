#SNAKE GAME IN PYTHON WITH DIFFERENT MODES 
#BY KRISHNA RAMCHANDANI
#
import  pygame
import random
x=pygame.init()
#Colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)
yellow=(255,255,0)

#Creating Window
speed=5
screen_width=900
screen_height=600
screen_caption="Snake Game"

gameWindow=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption(screen_caption)
pygame.display.update()
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,45)

def text_screen(text,color,x,y):
	screen_text=font.render(text,True,color)
	gameWindow.blit(screen_text,[x,y])
#Creating Game loop

def plot_snake(gameWindow,black1,snk_list,Snake_size1):
	for x,y in snk_list:
		pygame.draw.ellipse(gameWindow,black1,[x,y,Snake_size1,Snake_size1],5) #,Snake_size1,Snake_size1

def welcome():
	gameWindow.fill(white)
	#pygame.draw.lines(gameWindow, black,False,[(100,100), (150,200), (200,100)],10)
	pygame.display.flip()
	exit_game=False
	while not exit_game:
		gameWindow.fill(white)
		text_screen("Welcome To Snake Game ",black,175,175)


		text_screen("Press 1 to Play Easy Mode!",black,175,220)
		text_screen("Press 2 to Play Medium Mode!", black, 175,265)
		text_screen("Press 3 to Play Difficult Mode!",black,175,310)
		text_screen("Tip:Eat Green for More Score", green, 175, 420)
		text_screen("and Avoid Red", red, 175, 450)
		for event in pygame.event.get():
			#print(event)
			if event.type==pygame.QUIT:
				exit_game=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_1:
					easymode()
				if event.key==pygame.K_2:
					mediummode()
				if event.key==pygame.K_3:
					hardmode()
				
		pygame.display.update()
		clock.tick(60)
def easymode():
	# Game specific Variable
	exit_game = False
	game_over = False
	score = 0
	Snake_x = 45
	Snake_y = 55
	speed = 5
	Snake_size = 20
	velocity_x = 0
	velocity_y = 0
	fps = 30  # means frame per secound
	food_x = random.randint(0, screen_width / 2)
	food_y = random.randint(0, screen_height / 2)

	#enemy_x = random.randint(0, screen_width / 2)
	#enemy_y = random.randint(0, screen_height / 2)

	#pygame.draw.line(gameWindow,black,(0,0),(0,600),50)
	# photo=PhotoImage(file="left.png")

	snk_length = 1
	snk_list = []
	#with open("highscore.txt", "r") as f:
	#	highscore = f.read()

	while not exit_game:
		if game_over:

			#with open("highscore.txt", "w") as f:
			#	f.write(str(highscore))
			gameWindow.fill(white)

			text_screen("Game Over! Press Enter To Continue ", red, 100, 200)
			text_screen("Your Final Score: " + str(score), black, 200, 255)
			for event in pygame.event.get():
				# print(event)
				if event.type == pygame.QUIT:
					exit_game = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						welcome()

		else:

			for event in pygame.event.get():
				# print(event)
				if event.type == pygame.QUIT:
					exit_game = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						velocity_x = speed
						velocity_y = 0
					if event.key == pygame.K_LEFT:
						velocity_x = -speed
						velocity_y = 0
					if event.key == pygame.K_UP:
						velocity_y = -speed
						velocity_x = 0
					if event.key == pygame.K_DOWN:
						velocity_y = speed
						velocity_x = 0
					#if event.key == pygame.K_q:
						#score += 10

			Snake_x += velocity_x
			Snake_y += velocity_y

			if abs(food_x - Snake_x) < 10 and abs(food_y - Snake_y) < 10:
				score = score + 10
				# speed += 1
				# print("score=",score)

				food_x = random.randint(0, screen_width / 2)
				food_y = random.randint(0, screen_height / 2)
				snk_length += 2
				speed = speed + 1
				#enemy_x = random.randint(0, screen_width / 2)
				#enemy_y = random.randint(0, screen_height / 2)

			# if score>int(highscore):
			# highscore=score
			# gameWindow.image.load('left.png')

			gameWindow.fill(white)
			text_screen("Score: " + str(score) , red, 550, 10)  #    + "  High Score:" + str(highscore)
			pygame.draw.rect(gameWindow, green, [food_x, food_y, Snake_size, Snake_size])
			#pygame.draw.rect(gameWindow, red, [enemy_x, enemy_y, Snake_size, Snake_size])

			# pygame.draw.rect(gameWindow, black, [enemy_x, enemy_y, Snake_size, Snake_size])
			# pygame.draw.rect(gameWindow, black, [enemy_x, enemy_y, Snake_size, Snake_size])
			# pygame.draw.rect(gameWindow, black, [enemy_x, enemy_y, Snake_size, Snake_size])

			head = []
			head.append(Snake_x)
			head.append(Snake_y)
			snk_list.append(head)
			# print(snk_list)
			if len(snk_list) > snk_length:
				del snk_list[0]
			#if abs(enemy_x - Snake_x) < 10 and abs(enemy_y - Snake_y) < 10:
				#game_over = True
			if head in snk_list[:-1]:
				game_over = True
			# pygame.draw.rect(gameWindow,black,[Snake_x,Snake_y,Snake_size,Snake_size])
			if (Snake_x < 0) or (Snake_y < 0) or (Snake_x > screen_width) or (Snake_y > screen_height):
				game_over = True
			plot_snake(gameWindow, black, snk_list, Snake_size)
		pygame.display.update()
		clock.tick(fps)

	pygame.quit()
	quit()

def mediummode():
	# Game specific Variable
	exit_game=False
	game_over=False
	score=0
	Snake_x=45
	Snake_y=55
	speed=5
	Snake_size=20
	velocity_x=0
	velocity_y=0
	fps=30 #means frame per secound
	food_x=random.randint(0,screen_width/2)
	food_y=random.randint(0,screen_height/2)

	enemy_x=random.randint(0,screen_width/2)
	enemy_y=random.randint(0,screen_height/2)

	enemy1_x=random.randint(0,screen_width/2)
	enemy1_y=random.randint(0,screen_height/2)
	#photo=PhotoImage(file="left.png")

	snk_length=1
	snk_list=[]
	#with open("highscore.txt","r") as f:
	#	highscore=f.read()

	while not exit_game:
		if game_over:

			#with open("highscore.txt","w") as f:
			#	f.write(str(highscore))
			gameWindow.fill(white)
			
			text_screen("Game Over! Press Enter To Continue ",red,100,200)
			text_screen("Your Final Score: " + str(score), black, 200, 255)
			for event in pygame.event.get():
				#print(event)
				if event.type==pygame.QUIT:
					exit_game=True
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_RETURN:
						welcome()
				
		else:

			for event in pygame.event.get():
				#print(event)
				if event.type==pygame.QUIT:
					exit_game=True
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_RIGHT:
						velocity_x=speed
						velocity_y=0
					if event.key==pygame.K_LEFT:
						velocity_x=-speed
						velocity_y=0
					if event.key==pygame.K_UP:
						velocity_y=-speed
						velocity_x=0
					if event.key==pygame.K_DOWN:
						velocity_y=speed
						velocity_x=0
					if event.key==pygame.K_q:
						score +=10
						
			Snake_x +=velocity_x
			Snake_y +=velocity_y

			if abs(food_x - Snake_x)<10 and abs(food_y - Snake_y)<10:
				score=score+10
				#speed += 1
				#print("score=",score)
				
				food_x=random.randint(0,screen_width/2)
				food_y=random.randint(0,screen_height/2)
				snk_length +=2
				speed=speed+1
				enemy_x=random.randint(0,screen_width/2)
				enemy_y=random.randint(0,screen_height/2)
				enemy1_x=random.randint(0,screen_width/2)
				enemy1_y=random.randint(0,screen_height/2)


				#if score>int(highscore):
					#highscore=score
			#gameWindow.image.load('left.png')

			gameWindow.fill(white)
			text_screen("Score: "+ str(score) ,red,550,10) # +"  High Score:"+ str(highscore)
			pygame.draw.rect(gameWindow,green,[food_x,food_y,Snake_size,Snake_size])
			pygame.draw.rect(gameWindow,red, [enemy_x, enemy_y, Snake_size, Snake_size])
			pygame.draw.rect(gameWindow,red,[enemy1_x,enemy1_y,Snake_size,Snake_size])
			#pygame.draw.rect(gameWindow, black, [enemy_x, enemy_y, Snake_size, Snake_size])
			#pygame.draw.rect(gameWindow, black, [enemy_x, enemy_y, Snake_size, Snake_size])
			#pygame.draw.rect(gameWindow, black, [enemy_x, enemy_y, Snake_size, Snake_size])

			head=[]
			head.append(Snake_x)
			head.append(Snake_y)
			snk_list.append(head)
			#print(snk_list)
			if len(snk_list)>snk_length:
				del snk_list[0]
			if abs(enemy_x - Snake_x)<10 and abs(enemy_y - Snake_y)<10:
				game_over=True
			if abs(enemy1_x - Snake_x)<10 and abs(enemy1_y - Snake_y)<10:
				game_over=True
			if head in snk_list[ :-1]:
				game_over=True
			#pygame.draw.rect(gameWindow,black,[Snake_x,Snake_y,Snake_size,Snake_size])
			if (Snake_x<0) or (Snake_y<0) or (Snake_x>screen_width) or (Snake_y>screen_height):
				game_over=True		
			plot_snake(gameWindow,black,snk_list,Snake_size)
		pygame.display.update()
		clock.tick(fps)

	pygame.quit()
	quit()


def hardmode():
	# Game specific Variable
	exit_game = False
	game_over = False
	score = 0
	Snake_x = 45
	Snake_y = 55
	speed = 5
	Snake_size = 20
	velocity_x = 0
	velocity_y = 0
	fps = 30  # means frame per secound
	food_x = random.randint(0, screen_width / 2)
	food_y = random.randint(0, screen_height / 2)

	enemy_x = random.randint(0, screen_width / 2)
	enemy_y = random.randint(0, screen_height / 2)

	enemy1_x = random.randint(0, screen_width / 2)
	enemy1_y = random.randint(0, screen_height / 2)

	enemy2_x = random.randint(0, screen_width / 2)
	enemy2_y = random.randint(0, screen_height / 2)

	enemy3_x = random.randint(0, screen_width / 2)
	enemy3_y = random.randint(0, screen_height / 2)
	# photo=PhotoImage(file="left.png")

	snk_length = 1
	snk_list = []
	#with open("highscore.txt", "r") as f:
	#	highscore = f.read()

	while not exit_game:
		if game_over:

			#with open("highscore.txt", "w") as f:
			#	f.write(str(highscore))
			gameWindow.fill(white)

			text_screen("Game Over! Press Enter To Continue ", red, 100, 200)
			text_screen("Your Final Score: " + str(score), black, 200, 255)
			for event in pygame.event.get():
				# print(event)
				if event.type == pygame.QUIT:
					exit_game = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						welcome()

		else:

			for event in pygame.event.get():
				# print(event)
				if event.type == pygame.QUIT:
					exit_game = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						velocity_x = speed
						velocity_y = 0
					if event.key == pygame.K_LEFT:
						velocity_x = -speed
						velocity_y = 0
					if event.key == pygame.K_UP:
						velocity_y = -speed
						velocity_x = 0
					if event.key == pygame.K_DOWN:
						velocity_y = speed
						velocity_x = 0
					if event.key == pygame.K_q:
						score += 10

			Snake_x += velocity_x
			Snake_y += velocity_y

			if abs(food_x - Snake_x) < 10 and abs(food_y - Snake_y) < 10:
				score = score + 10
				# speed += 1
				# print("score=",score)

				food_x = random.randint(0, screen_width / 2)
				food_y = random.randint(0, screen_height / 2)
				snk_length += 2
				speed = speed + 1
				enemy_x = random.randint(0, screen_width / 2)
				enemy_y = random.randint(0, screen_height / 2)
				enemy1_x = random.randint(0, screen_width / 2)
				enemy1_y = random.randint(0, screen_height / 2)
				enemy2_x = random.randint(0, screen_width / 2)
				enemy2_y = random.randint(0, screen_height / 2)
				enemy3_x = random.randint(0, screen_width / 2)
				enemy3_y = random.randint(0, screen_height / 2)
			# if score>int(highscore):
			# highscore=score
			# gameWindow.image.load('left.png')

			gameWindow.fill(white)
			text_screen("Score: " + str(score) , red, 550, 10)   #  + "  High Score:" + str(highscore)
			pygame.draw.rect(gameWindow, green, [food_x, food_y, Snake_size, Snake_size])
			pygame.draw.rect(gameWindow, red, [enemy_x, enemy_y, Snake_size, Snake_size])
			pygame.draw.rect(gameWindow, red, [enemy1_x, enemy1_y, Snake_size, Snake_size])
			pygame.draw.rect(gameWindow, red, [enemy2_x, enemy2_y, Snake_size, Snake_size])
			pygame.draw.rect(gameWindow, red, [enemy3_x, enemy3_y, Snake_size, Snake_size])
			# pygame.draw.rect(gameWindow, black, [enemy_x, enemy_y, Snake_size, Snake_size])
			# pygame.draw.rect(gameWindow, black, [enemy_x, enemy_y, Snake_size, Snake_size])
			# pygame.draw.rect(gameWindow, black, [enemy_x, enemy_y, Snake_size, Snake_size])

			head = []
			head.append(Snake_x)
			head.append(Snake_y)
			snk_list.append(head)
			# print(snk_list)
			if len(snk_list) > snk_length:
				del snk_list[0]
			if abs(enemy_x - Snake_x) < 10 and abs(enemy_y - Snake_y) < 10:
				game_over = True
			if abs(enemy1_x - Snake_x) < 10 and abs(enemy1_y - Snake_y) < 10:
				game_over = True
			if abs(enemy2_x - Snake_x) < 10 and abs(enemy2_y - Snake_y) < 10:
				game_over = True
			if abs(enemy3_x - Snake_x) < 10 and abs(enemy3_y - Snake_y) < 10:
				game_over = True
			if head in snk_list[:-1]:
				game_over = True
			# pygame.draw.rect(gameWindow,black,[Snake_x,Snake_y,Snake_size,Snake_size])
			if (Snake_x < 0) or (Snake_y < 0) or (Snake_x > screen_width) or (Snake_y > screen_height):
				game_over = True
			plot_snake(gameWindow, black, snk_list, Snake_size)
		pygame.display.update()
		clock.tick(fps)

	pygame.quit()
	quit()

welcome()
