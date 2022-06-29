import pygame
pygame.init()
from events import keyboard
from colors import *
from units import Tank



def main():
	display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)              # создаем окно во весь экран
	pygame.display.set_caption('Tanks v4.0')                                  # прописываем название окна

	display_width, display_height = pygame.display.get_surface().get_size()   # поучаем ширину и высоту экрана

	tank = Tank(
		x           = int(display_width / 2), 
		y           = int(display_height / 2),           
		vector      = [0, -1],
		head_vector = [0, -1],                   
		body_path   = 'assets/body-t44.png',
		head_path   = 'assets/head-t44.png',
		speed       = 50,
		reloading   = 1,
		display     = display
	)

	while True:
		display.fill(DARKPALEGOLDENROD)										  # задаем фон окна                                                 

		for event in pygame.event.get():                                      # получаем текущие события из event
			if event.type == pygame.QUIT:									  # если событие равно клику на кнопку закрытия, останавливаемся
				return 'Stop'			

		if not keyboard(pygame.key.get_pressed(), tank):                      # при нажатии на ESC тоже закрываем приложение
			return ''


		tank.draw()

		for bullet in tank.bullets:
			if pygame.time.get_ticks() - bullet.time < tank.bullet_fly_length:
				bullet.draw()
			else:
				bullet.hit(bullet)


		pygame.display.update()												  # обновляем экран для сохранения изменений





if __name__ == '__main__':
	main()