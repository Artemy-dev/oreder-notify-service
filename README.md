# Order Notify Service – микросервис уведомлений о заказах

## Назначение проекта

**Order Notify Service** — это микросервис для отправки уведомлений о новых заказах в реальном времени через Telegram.

### Возможные сценарии использования

* **Интернет-магазин** — мгновенное уведомление менеджера или владельца о новом заказе.
* **CRM или ERP система** — уведомления о событиях: новых клиентах, оплатах, изменении статуса заказа.
* **Служба доставки** — моментальное оповещение курьера или склада о поступившем заказе.
* **Мониторинг** — быстрые алерты о критических событиях (например, падение сервиса, ошибка обработки).

Благодаря асинхронной архитектуре (FastAPI + RabbitMQ + Aiogram) сервис легко масштабируется и может быть расширен для отправки уведомлений не только в Telegram, но и по email, SMS или push-уведомлениям.

### Архитектура микросервиса уведомлений

**Схема взаимодействия:**<br>
`Пользователь → API (FastAPI + FastStream) → Брокер (RabbitMQ) → Telegram-бот (FastStream + Aiogram) → Пользователь`

### Технологический стек
* **FastAPI** — REST API
* **FastStream** — интеграция с RabbitMQ
* **RabbitMQ** — брокер сообщений
* **Aiogram** — Telegram-бот
* **python-dotenv** — загрузка переменных окружения

---

## Структура проекта
```
order-notify-service/
├── .gitignore
├── .env
├── api.py
├── bot.py
├── README.md
└── requirements.txt
```

### Файл `.env`

Необходим для хранения секретов:

```
TOKEN=токен_вашего_бота
CHAT_ID=id_чата_или_пользователя
```

---

## Развёртывание окружения

### 1. Запуск RabbitMQ через Docker

```bash
docker run -d \
  --name rabbitmq \
  --hostname rabbitmq \
  -p 15672:15672 \
  -p 5672:5672 \
  rabbitmq:3.10.7-management
```

* Панель управления: [http://localhost:15672](http://localhost:15672)
* Данные для входа: `guest / guest`

#### Управление контейнером

```bash
docker ps             # Проверить работающие контейнеры
docker stop rabbitmq  # Остановить контейнер
docker start rabbitmq # Запустить контейнер
```

---

## Зависимости

### 2. Установка напрямую

```bash
pip install fastapi uvicorn faststream
pip install faststream[rabbit]
pip install aiogram
pip install python-dotenv
```

### 3. Или через `requirements.txt`

```bash
pip install -r requirements.txt
```

---

## Запуск сервисов

### 4. API-сервис

```bash
uvicorn api:app --reload
```

Документация API: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 5. Telegram-бот

```bash
python bot.py
```
