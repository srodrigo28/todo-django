# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate

# Django create project
> * Instalando django

```
python -m pip install django
```

```
django-admin startproject todo_project .
```

> * Tarefas
```
python manage.py startapp tarefas
```

> * Rodando migrate
```
python manage.py migrate
```

> * Rodar aplicação
```
python manage.py runserver
```

> * URL Inicial
```
http://127.0.0.1:8000/
```