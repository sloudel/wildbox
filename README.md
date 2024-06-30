# Пример проекта с использованием Django REST framework

## Для запуска необходимо:
### Создать `.env` файл в корне репозитория с переменными:
| Имя параметра             | Описание параметра                                                               |
|---------------------------|---------------------------------------------------------------------------|
| DJANGO_SETTINGS_MODULE    | Путь до settings.py                                                       |
| DJANGO_SECRET_KEY         | Секретный ключ                                                            |
| POSTGRES_DB               | Название базы данных в PostgreSQL.                                        |
| POSTGRES_USER             | Имя пользователя в БД                                                     |
| POSTGRES_PASSWORD         | Пароль пользователя в БД.                                                 |
| SUBDOMAIN_NAME            | Имя поддомена, где будет размещен проект.                                 |
| DOMAIN_NAME               | Имя домена, где будет размещен проект.                                    |
### Создать volume для хранения данных в БД: `docker volume create postgres_data`
### Заупстить Docker: `docker compose up -d`
### Выполнить миграции БД: `docker exec -it backend bash`, а затем `python3 manage.py migrate`

## API
| Метод              | Интерфейс            | Описание интерфейса                                                            |
|--------------------|---------------------------|---------------------------------------------------------------------------|
| POST   | /auth/register    | Регистрация нового пользователя                                                   |
| POST   | /auth/login         | Вход в систему с логином и паролем, в ответ получаем токен для доступа к остальным endpoint`ам.                                         |
| POST   | /auth/logout               | Передаем токен, выводим его из эксплуатации.                             |
| GET    | /url_checker/             | Получить список всех ссылок и результатов их проверки.                                                     |
| POST   | /url_checker/         | Создать новую ссылку в БД.                                                 |
| PUT    | /url_checker/URL_OBJECT_ID            | Изменить существующую ссылку (и/или результат проверки) в БД по идентификатору.                                 |
| DELETE | /url_checker/URL_OBJECT_ID               | Удалить ссылку и результатт проверки из БД по идентификатору.                                    |

## TODO
[] - Тесты
[] - Массовое создание/изменение Url в БД
[] - Выполнять регулярные задачи в параллельном режиме и контроллировать результат исп. Celery