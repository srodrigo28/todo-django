## Python Django
> * Orientação: Portal Felipe Rocha

### Como criar um projeto Django

> * Linux / macOS
python3 -m venv venv
source venv/bin/activate

> * Windows
python -m venv venv
.\venv\Scripts\activate

### * Cria a tabela
```
python manage.py migrate
```

### Criar um usuário
```
python manage.py createsuperuser
```

### Rodar o projeto
```
python manage.py runserver
```