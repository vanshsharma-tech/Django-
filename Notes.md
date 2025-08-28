# 🐍 Django Notes

A quick reference guide for learning **Django Framework**.

---

## 🔹 Introduction to Django
- **Django** is a high-level Python Web Framework.
- Helps in rapid development and clean, pragmatic design.
- Built on the **MVT (Model-View-Template)** architecture.

---

## 🔹 Why Django?
- Fast development.
- Secure (protects from SQL Injection, CSRF, XSS).
- Scalable and reliable.
- Built-in Admin Panel.
- Large community support.

---

## 🔹 Django Architecture (MVT)
1. **Model** – Handles database (ORM - Object Relational Mapping).
2. **View** – Contains business logic, interacts with Model & Template.
3. **Template** – Handles presentation layer (HTML, CSS, JS).

---

## 🔹 Django Project Setup (with uv)

### 1. Install uv
```bash
pip install uv
# OR on Linux/Mac
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Create Virtual Environment
```bash
uv venv
```

Activate it:
- **Linux/Mac**:  
  ```bash
  source .venv/bin/activate
  ```
- **Windows (PowerShell)**:  
  ```bash
  .venv\Scripts\activate
  ```

### 3. Install Django
```bash
uv pip install django
```

### 4. Create Django Project
```bash
django-admin startproject projectname
cd projectname
```

### 5. Run Development Server
```bash
python manage.py runserver
```

### 6. Create App
```bash
python manage.py startapp appname
```

---

## 🔹 Django Project Structure
```
projectname/
    manage.py
    projectname/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    appname/
        models.py
        views.py
        urls.py
        templates/
        static/
```

---

## 🔹 URLs and Views
- In **urls.py** (project level):
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appname.urls')),
]
```

- In **appname/urls.py**:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

- In **views.py**:
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```

---

## 🔹 Templates
- Create a folder **templates/** inside app.
- Example `home.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Django App</title>
</head>
<body>
    <h1>Welcome to Django 🚀</h1>
</body>
</html>
```

- Render template in `views.py`:
```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

---

## 🔹 Models and Database
- In **models.py**:
```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
```

- Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

- Register model in **admin.py**:
```python
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

---

## 🔹 Django Admin
- Create superuser:
```bash
python manage.py createsuperuser
```

- Access at: `http://127.0.0.1:8000/admin/`

---

## 🔹 Static Files
- Add in `settings.py`:
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
```

- Use in template:
```html
{% load static %}
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

---

## 🔹 Forms
- Django provides `forms.py` for handling forms.
```python
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
```

---

## 🔹 Django ORM Queries
```python
# Create
student = Student.objects.create(name="Vansh", age=21, email="test@email.com")

# Read
students = Student.objects.all()

# Filter
Student.objects.filter(age__gte=18)

# Update
student.age = 22
student.save()

# Delete
student.delete()
```

---

## 🔹 Adding Tailwind CSS in Django

There are two common ways to use Tailwind in Django:

### ✅ Method 1: Using `django-tailwind` package
1. Install package:
   ```bash
   uv pip install django-tailwind
   uv pip install django-browser-reload
   ```

2. Add to `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...,
       "tailwind",
       "theme",   # your theme app
       "django_browser_reload",
   ]

   TAILWIND_APP_NAME = "theme"
   ```

3. Create a Tailwind app:
   ```bash
   python manage.py tailwind init theme
   ```

4. Install Node.js dependencies:
   ```bash
   cd theme
   npm install
   ```

5. Run Tailwind in development:
   ```bash
   python manage.py tailwind start
   ```

6. Add middleware in `settings.py`:
   ```python
   MIDDLEWARE = [
       ...,
       "django_browser_reload.middleware.BrowserReloadMiddleware",
   ]
   ```

7. Add URL for browser reload in **urls.py**:
   ```python
   from django.urls import path, include

   urlpatterns = [
       ...,
       path("__reload__/", include("django_browser_reload.urls")),
   ]
   ```

---

### ⚡ Method 2: Using Tailwind CLI
1. Install Tailwind CLI globally (via npm):
   ```bash
   npm install -D tailwindcss
   npx tailwindcss init
   ```

2. Configure `tailwind.config.js`:
   ```js
   module.exports = {
     content: [
       "./templates/**/*.{html,js}",
       "./**/templates/**/*.{html,js}",
     ],
     theme: {
       extend: {},
     },
     plugins: [],
   }
   ```

3. Create input CSS `static/src/input.css`:
   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

4. Run Tailwind build:
   ```bash
   npx tailwindcss -i ./static/src/input.css -o ./static/css/style.css --watch
   ```

5. Load in template:
   ```html
   {% load static %}
   <link href="{% static 'css/style.css' %}" rel="stylesheet">
   ```

---

👉 Example usage:
```html
<h1 class="text-3xl font-bold text-blue-500">Hello Django + Tailwind 🚀</h1>
```

---

## 🔹 Important Commands
```bash
python manage.py runserver       # Run server
python manage.py startapp app    # Create new app
python manage.py makemigrations  # Create migrations
python manage.py migrate         # Apply migrations
python manage.py createsuperuser # Create admin user
```

---

## 📌 Summary
- Django follows **MVT architecture**.
- Provides built-in admin, ORM, and security features.
- Tailwind can be integrated via **django-tailwind** or **Tailwind CLI**.
- Ideal for rapid development of secure and scalable applications.
