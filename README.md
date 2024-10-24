# Django REST API Docker

## Запуск проекта

1. Сборка образа:
```bash
docker build -t my-django-app .

2. Запуск контейнера:
docker run -d -p 8000:8000 my-django-app

3. Открыть в браузере:
http://localhost:8000