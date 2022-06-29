from pygame import K_ESCAPE, K_w, K_s, K_a, K_d, K_UP, K_DOWN, K_RIGHT, K_LEFT, K_SPACE


def keyboard(keys, tank):

	if keys[K_ESCAPE]:
		return False

	elif keys[K_w]:
		tank.movement([0, -1])
	elif keys[K_s]:
		tank.movement([0, 1])
	elif keys[K_a]:
		tank.movement([-1, 0])
	elif keys[K_d]:
		tank.movement([1, 0])

	if keys[K_UP]:
		tank.head_rotation([0, -1])
	elif keys[K_DOWN]:
		tank.head_rotation([0, 1])
	elif keys[K_RIGHT]:
		tank.head_rotation([1, 0])
	elif keys[K_LEFT]:
		tank.head_rotation([-1, 0])

	if keys[K_SPACE]:
		tank.shot()

	return True