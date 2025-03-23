from time import sleep

import time


def track_time(function):
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        print(end_time - start_time)

    return wrapper


@track_time  # сам все функции из cook отправляет в track_time
def cook():  # функция, запускающая готовку заказа пользователя
    sleep(10)
    print('готовим')

cook()