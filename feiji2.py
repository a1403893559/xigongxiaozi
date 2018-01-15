import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERP_FIRE_EVENT = pygame.USEREVENT + 1
ENEMY = pygame.USEREVENT + 1 
#ENEMY_FIRE_EVENT = pygame.USEREVENT + 1
class GameSprite(pygame.sprite.Sprite):

	def __init__(self,image_name,speed=1):
		super().__init__()
		self.image = pygame.image.load(image_name)  #加载图像
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.y += self.speed


class Backgroup(GameSprite):
	def update(self):

		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height



class Hero(GameSprite):
	def __init__(self):
		super().__init__('/home/jiu/桌面/__pycache__/资源/images/me_destroy_3.png',0)

		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
		self.bullets = pygame.sprite.Group()
	def update(self):

		self.rect.x += self.speed
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right


	def fire(self):
		bullet = Bullet()
		bullet.rect.bottom = self.rect.y - 20
		bullet.rect.centerx = self.rect.centerx
		self.bullets.add(bullet)

class Enemy(GameSprite):
	def __init__(self):
		
		
		super().__init__('/home/jiu/桌面/__pycache__/资源/images/enemy2.png')
		#d = [a,b,c]




		a = '/home/jiu/桌面/__pycache__/资源/images/enemy3_down1.png'
		b = '/home/jiu/桌面/__pycache__/资源/images/enemy2.png'
		c = '/home/jiu/桌面/__pycache__/资源/images/enemy1.png'

		d = random.randint(1,4)
		if d == 1:
					
			super().__init__(a)
		elif d == 2:
			
			super().__init__(b)
		elif d == 3:	
	
			super().__init__(c)
		else:
			
			super().__init__(a)
		self.speed = random.randint(1,3)
		self.rect.bottom = 0

		self.bullets1 = pygame.sprite.Group()

		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)
		self.kill()


	def fire1(self):
		bullet1 = EnemyBullet()
		bullet1.rect.y = self.rect.bottom + 20
		bullet1.rect.centerx = self.rect.centerx
		self.bullets1.add(bullet1)



	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			self.kill()
	
	def __del__(self):
		print("%s飞机死了啦"%self.rect)


class Bullet(GameSprite):

	def __init__(self):
		super().__init__('/home/jiu/桌面/__pycache__/资源/images/bullet1.png',-5)

	def update(self):
		super().update()
		if self.rect.y <= 0:
			self.kill()
	def __del__(self):
		print("没了")



class EnemyBullet(GameSprite):
	def __init__(self):
		super().__init__('/home/jiu/桌面/__pycache__/资源/images/bullet1.png',5)
	def update(self):
		super().update()
		if self.rect.y >= 700:
			self.kill()
	def __del__(self):
		print("子弹消失了")
