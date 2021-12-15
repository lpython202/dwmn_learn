# Обрезка ссылок с помощью Битли

Программа создает короткие ссылки и показывает количество кликов.

### Как установить

Создать файл .env в корне проекта с содержимым TOKEN=(ваш токен).
Получить токен: Регистрируйтесь на Bitly через e-mai. 
По ссылке https://app.bitly.com/settings/apps/   создайте токен (GENERIC ACCESS TOKEN — нужный тип токена)


Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Примеры запуска
```
python3 main.py https://yandex.ru
...
Битлинк https://bit.ly/3pXMhvC


python3 main.py https://bit.ly/3pXMhvC
...
Количество кликов: 0
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
