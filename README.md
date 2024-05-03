# Тестовое задание Student Labs 2024
Тестовое задание на проверку знаний в облости разработки Telegram Bots

## Описание
Проект написан с использованием таких инструментов, как:
- SqlAlchemy (Для подключения и работы с базой данных PostgreSQL)
- Aiogram 

## Запуск проектов
1. Добавьте в environment данные переменные
```python
DB_HOST=<hostname вашей базы данных PostgreSQL>
DB_PORT=<port базы данных PostgreSQL>
DB_USER=<пользователь базы данных PostgreSQL>
DB_PASS=<пароль пользователя базы данных>
DB_NAME=<название базы данных PostgreSQL>
TOKEN=<token бота Telegram>
```
2. Установите зависимости
```bash
poetry install
```
3. Запустите проект
``` bash
poetry run python3 src/main.py
```

## Авторы
Божко Даниил Константинович - backend разработчик.
