<h1 align="center">Проект YaMDb</h1>

<h4>Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.</h4>

### Стек технологий:
![python version](https://img.shields.io/badge/Python-3.7.9-green)
![django version](https://img.shields.io/badge/Django-3.2-green)
![django rest framework](https://img.shields.io/badge/DjangoRestFramework-3.12.4-green)
![Html](https://img.shields.io/badge/HTML-green)
![CSS](https://img.shields.io/badge/CSS-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-green)

### Запуск проекта в dev-режиме:
1. Склонировать репозиторий:
```
git clone https://github.com/Artem-Bespalov/api_yamdb
```
2. Установить и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
3. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
4. Выполнить миграции:
```
python manage.py migrate
```
5. Запустить сервер:
```
python manage.py runserver
```
### Примеры запросов к API:
* ```api/v1/auth/signup/``` - Регистрация нового пользователя (POST)
* ```api/v1/auth/token/``` - Получение JWT-токена (POST)
* ```api/v1/categories/``` - Получение списка всех категорий (GET)
* ```api/v1/genres/``` - Получение списка всех жанров (GET)
* ```api/v1/titles/``` - Получение списка всех произведений (GET)
* ```api/v1/titles/{title_id}/reviews/``` - Получение списка всех отзывов (GET)
* ```api/v1/titles/{title_id}/reviews/{review_id}/comments/``` - Получение списка всех комментариев к отзыву (GET)
* ```api/v1/users/``` - Получение списка всех пользователей (GET)
* ```api/v1/users/{username}/``` - Получение пользователя по username (GET)
* ```api/v1/users/me/``` - Получение данных своей учетной записи (GET)

### Авторы проекта:
Тимлид: <a href="https://github.com/Artem-Bespalov">Артем Беспалов</a>

<a href="https://github.com/Ekaterishe4ka">Екатерина Богомолова</a>

<a href="https://github.com/BestTpaktop">Данил Аникин</a>





