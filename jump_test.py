from time import time


def jump(up_speed, jumping=False, gravity=1):
    start_position = [0, 0]
    start_time = time()
    while jumping:
        start_position[1] -= up_speed
        up_speed -= gravity
        print(start_position)
        if start_position[1] == start_position[1]:
            jumping = False
            end_time = time()
            delta_time = end_time - start_time
            print(delta_time)


jump(5, True, 1)
