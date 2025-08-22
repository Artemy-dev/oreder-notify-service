Схема микросервиса нотификаций (уведомлений):
User -> API (FastAPI, FastStream) -> Брокер (RabbitMQ) -> TG-bot (FastStream, IOgram) -> User

Стек: FastAPI, Aiogram, FastStream, RabbitMQ.

Разворачиваем Docker:
docker run -d --name rabbitmq --hostname rabbitmq -p 15672:15672 -p 5672:5672 rabbitmq:3.10.7-management

RabbitMQ Management
http://localhost:15672/
Username: guest
Password: guest

Проверка работающих контейнеров:
docker ps

Остановка и запуск контейнера:
docker stop rabbitmq
docker start rabbitmq

Установка зависимостей:
pip install fastapi uvicorn faststream
pip install faststream[rabbit]
pip install aiogram
pip install python-dotenv


Запуск API (http://127.0.0.1:8000/docs): 
uvicorn api:app --reload

