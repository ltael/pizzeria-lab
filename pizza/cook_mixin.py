
import asyncio

class CookMixin:
    async def cook(self):
        print('Готовим Вашу пиццу.')
        await asyncio.sleep(1)


    def finish_cook(self):
        print('Ваша пицца готова.')