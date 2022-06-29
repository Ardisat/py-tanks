from pygame import image, transform, time
from colors import WHITE


class Tank:

	bullets = []                   # массив со снарядами танка
	ready_to_shot = True           # готов ли танк стрелять (закончилас ли перезарядка)
	bullet_fly_length = 1 * 1000   # время полета снаряда до уничтожения

	def __init__(self, x, y, vector, head_vector, body_path, head_path, speed, reloading, display):

		self.x           = x                             # начальная координата x
		self.y           = y                             # начальная координата y
		self.vector      = vector                        # вектор (направление танка)
		self.head_vector = head_vector                   # вектор (направление башни)

		self.body        = image.load(body_path)         # картинка корпуса
		self.width       = self.body.get_rect().size[0]  # получение ширины картинки
		self.height      = self.body.get_rect().size[1]  # получение высоты картинки
		self.body.set_colorkey(WHITE)				     # удаление белого фона

		self.head        = image.load(head_path)         # картинка башни
		self.head_width  = self.head.get_rect().size[0]
		self.head_height = self.head.get_rect().size[1]
		self.head.set_colorkey(WHITE)

		self.display     = display                       # экран для отрисовки
		self.shot_time = time.get_ticks()                # время совершения выстрела

		self.speed       = speed / 100                   # скорость танка (пиксели)             
		self.reloading   = reloading * 1000              # время перезарядки (мс)



	def draw(self):

		# отрисовка корпуса
		if self.vector == [0, -1] or self.vector == [0, 1]:
			body = transform.rotate(self.body, 0)
			body_x = self.x - (self.width / 2)
			body_y = self.y - (self.height / 2) 

		elif self.vector == [-1, 0] or self.vector == [1, 0]:
			body = transform.rotate(self.body, 90)
			body_x = self.x - (self.height / 2)
			body_y = self.y - (self.width / 2)


		self.display.blit(body,  (body_x, body_y))

		# отрисовка башни
		if self.head_vector == [0, -1]:
			head = transform.rotate(self.head, 0)
			head_x = self.x - (self.head_width / 2)
			head_y = self.y - (self.head_height / 2) - (self.height / 4)

		elif self.head_vector == [-1, 0]:
			head = transform.rotate(self.head, 90)
			head_x = self.x - (self.head_height / 2) - (self.head_width / 2)
			head_y = self.y - (self.head_width / 2)

		elif self.head_vector == [0, 1]:
			head = transform.rotate(self.head, 180)
			head_x = self.x - (self.head_width / 2)
			head_y = self.y - (self.head_height / 2) + (self.height / 4)

		elif self.head_vector == [1, 0]:
			head = transform.rotate(self.head, 270)
			head_x = self.x - (self.head_height / 2) + (self.head_width / 2)
			head_y = self.y - (self.head_width / 2)

		self.display.blit(head, (head_x, head_y))


	def movement(self, vector):
		self.vector = vector                        # сохраняем полученый с клавиатуры вектор

		self.x += self.speed * self.vector[0]       # изменяем x-кординату танка
		self.y += self.speed * self.vector[1]       # изменяем y-кординату танка

		self.draw()                                 # вызваем функцию отрисовки


	def head_rotation(self, vector):
		self.head_vector = vector	                # сохраняем полученый с клавиатуры вектор башни
		self.draw()                                 # вызваем функцию отрисовки


	def shot(self):
		self.current_time = time.get_ticks() 

		if (self.current_time - self.shot_time) > self.reloading:
			self.ready_to_shot = True

		if self.ready_to_shot:                                                  # если закончилась перезарядка
			self.shot_time = time.get_ticks()

			bullet = Bullet(                                                    # создаем новый объект снаряда
				x           = self.x + self.head_width * self.head_vector[0],   # x-координата снаряда
				y           = self.y + self.head_height * self.head_vector[1],  # y-координата снаряда
				vector      = self.head_vector,                                 # вектор полета снаряда
				speed       = 400,                                              # скорость полета снаряда
				bullet_path = 'assets/bullet.png',                              # картинка снаряда
				display     = self.display                                      # экран для отрисовки
			)

			self.bullets.append(bullet)                                         # добавляем объект в список снарядов
			self.ready_to_shot = False




class Bullet:

	def __init__(self, x, y, vector, speed, bullet_path, display):

		self.x       = x                               # начальная координата x
		self.y       = y                               # начальная координата y
		self.vector  = vector                          # вектор (направление полета снаряда)
		self.speed   = speed / 100                     # скорость полета снаряда

		self.bullet  = image.load(bullet_path)         # картинка корпуса
		self.width   = self.bullet.get_rect().size[0]  # получение ширины картинки
		self.height  = self.bullet.get_rect().size[1]  # получение высоты картинки	

		self.display = display                         # экран для отрисовки снаряжа
		self.time    = time.get_ticks()


	def draw(self):

		# отрисовка снаряда
		self.x += self.speed * self.vector[0]              # изменяем x-кординату танка
		self.y += self.speed * self.vector[1]              # изменяем y-кординату танка

		self.display.blit(self.bullet,  (self.x, self.y))  # отрисовываем пулю


	def hit(self, bullet):
		del bullet