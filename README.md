# Web-приложение для определения шаблона формы

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python)
![MongoDB](https://img.shields.io/badge/MongoDB-v6-green?logo=mongodb)
![Docker](https://img.shields.io/badge/Docker-20.10-blue?style=flat&logo=docker)
![beanie](https://img.shields.io/pypi/v/beanie?label=beanie&logo=pypi)
![fastapi](https://img.shields.io/pypi/v/fastapi?label=fastapi&logo=fastapi)
 ![motor](https://img.shields.io/pypi/v/motor?label=motor&logo=pypi)

## Описание
Это приложение на FastAPI, которое получает на вход JSON-данные полей формы и определяет, под какой шаблон формы они подходят, основываясь на именах полей и типах их значений. Шаблоны форм хранятся в MongoDB и описываются как словарь полей с указанием их типов (email, phone, date, text). Если подходящего шаблона не находится, приложение типизирует поля "на лету" и возвращает их типы.

Проект развернут по адресу:  https://ecom.sycorax.tech

Основные моменты:

- Поддерживаемые типы полей: email, phone, date, text.
- Валидация данных:
Порядок проверки типа: date → phone → email → text.
- Хранение шаблонов в базе данных:
- Используется MongoDB, доступ к ней осуществляется через Beanie (ODM для MongoDB).
- Docker и docker-compose:
Приложение и база данных запускаются через Docker.


### Структура проекта
```
project/
├── app/
│   ├── main.py                    # Точка входа в приложение FastAPI
│   ├── core/
│   │   ├── config.py              # Конфигурация приложения (настройки базы данных и других параметров)
│   ├── db/
│   │   ├── database.py            # Логика подключения к базе данных (MongoDB)
│   ├── models/
│   │   ├── form_template.py       # Описание модели FormTemplate для MongoDB
│   ├── schemas/
│   │   ├── form_template.py       # Схемы для FormTemplate (входные/выходные данные)
│   ├── routes/
│   │   ├── form.py                # API-эндпоинты для работы с формами
│   ├── utils/
│   │   ├── validation.py          # Функции для проверки типов данных (email, phone, date)
│   │   ├── deps.py                # Вспомогательные зависимости (например, для FastAPI)
├── scripts/
│   ├── init_db.py                 # Скрипт для инициализации базы данных
|   ├── test_requests.sh               # Пример тестовых запросов к API
├── docker-compose.yml             # Настройка Docker для работы с приложением и базой данных
├── Dockerfile                     # Описание Docker-образа приложения
├── requirements.txt               # Список зависимостей Python
├── README.md                      # Документация проекта
```

### Эндпоинты
- POST /get_form
Принимает в теле запроса JSON-объект с произвольным набором полей и их значений. Определяет шаблон на основе типов значений. Если подходящий шаблон найден — возвращает {"template_name": "<название_шаблона>"}.
Если подходящего шаблона нет — возвращает словарь полей с определёнными на лету типами.
- GET /templates
Возвращает список всех шаблонов, хранящихся в базе данных.
### Пример структуры шаблона в базе:
```
{
    "name": "MyForm",
    "fields": {
        "user_name": "text",
        "lead_email": "email",
        "order_date": "date"
    }
}
```

### Запуск проекта
1. Клонируйте репозиторий
```
git clone https://github.com/maksorli/form-matcher.git
cd project
```
2. Запустите сборку и запуск контейнеров:
```
docker-compose up -d --build
```
## Локальное Тестирование
1. С помощью Swagger UI по адресу http://localhost:8000/docs
2. С помощью скрипта. Запустите скрипт:
```
./scripts/test_requests.sh
```

## Тестирование на web

1. С помощью Swagger UI по адресу https://ecom.sycorax.tech/docs
2. С помощью скрипта. Запустите скрипт:
```
./scripts/test_requests.prod.sh
```
