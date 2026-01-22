# Мини-система сбора и анализа данных
___
## Установка проекта
```
git clone https://github.com/Y-uri-K/Data-analysis.git
```
# Запуск проекта
## Важно!
1. Создать файл .env по примеру
2. Вставить все переменные
Для генерации REDASH_COOKIE_SECRET и REDASH_SECRET_KEY можно воспользоваться:
```cmd
python -c "import secrets; print(secrets.token_hex(32))"
```

Для первого запуска потребуется:
```cmd
docker compose run --rm redash-server create_db
```
Далее
```cmd
docker compose up
```
### Redash можно найти по пути:
```cmd
http://localhost:5000
```
### Для контроля базы данных pgAgmin:
```cmd
http://localhost:8080
```
# Проект

# PostgreSQL DB 

<img width="1041" height="854" alt="изображение" src="https://github.com/user-attachments/assets/2cf5efc8-ba69-405b-932b-5f0bc8b45b9d" />

# Redash dashboard

<img width="2496" height="872" alt="изображение" src="https://github.com/user-attachments/assets/8273df79-d4db-4178-8745-f6b503cde6ac" />

Генерация данных каждую секунду

Огромное спасибо за лучшие советы по созданию:

### https://github.com/VL1507
