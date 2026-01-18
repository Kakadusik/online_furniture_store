# Онлайн магазин мебели по урокам Python Hub Studio

Веб-приложение для заказа мебели онлайн на Django.  

## Установка  

1. **Клонировать репозиторий**  
   ```bash
   git clone https://github.com/kakadusik/online_furniture_store.git
   cd online_furniture_store

2. **Создать виртуальное окружение**
    ```bash
    python -m venv venv
   
    # Для Windows:
    venv\Scripts\activate

    # Для Linux/macOS:
    source venv/bin/activate

3. **Установить зависимости**
    ```bash
    pip install -r requirements.txt

4. **Запуск проекта**

    ```bash
   #Применить миграции
   python manage.py migrate

   #Создать суперпользователя (если нужно)
   python manage.py createsuperuser

   #Запустить сервер
   python manage.py runserver

   #После этого сайт будет доступен по адресу: http://127.0.0.1:8000
