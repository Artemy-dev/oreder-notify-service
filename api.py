from fastapi import FastAPI
from faststream.rabbit.fastapi import RabbitRouter  # Импортируем RabbitRouter для работы с RabbitMQ через FastStream

app = FastAPI()          # Создаём экземпляр приложения FastAPI
router = RabbitRouter()  # Создаём объект RabbitRouter для подключения к брокеру сообщений RabbitMQ

@router.post("/order")   # Обработчик POST-запроса по адресу "/order"
async def new_order(name: str):
    await router.broker.publish(         # Публикуем сообщение с именем заказа в брокер RabbitMQ
        f"Новый заказ {name}",
        queue="orders"                   # Указываем очередь, куда отправляем сообщение
    )
    return {"status": "ok"}              # Возвращаем ответ клиенту в формате JSON

app.include_router(router)               # Подключаем RabbitRouter к нашему FastAPI-приложению