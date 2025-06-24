# 🎓 Django Student Management System (CRUD + Auth)

This is a Django-based Student Management System that allows users to **Create, Read, Update, and Delete (CRUD)** student records. It also includes **user authentication** using Django's built-in auth system. The project uses **MySQL** as the database and includes two Django apps for modular functionality.

---

## 🚀 Features

- ✅ User registration, login, and logout
- ✅ Add new student records
- ✅ View all students
- ✅ Edit student details
- ✅ Delete student records
- ✅ Authentication-protected views
- ✅ Clean Django templates

---

## 🛠️ Tech Stack

- **Framework:** Django (Python)
- **Database:** MySQL
- **Frontend:** HTML5, CSS3 (Django Templates)
- **Auth:** Django built-in authentication

---

## 📁 Project Structure
```
django-student-crud-auth/
│
├── .venv/                # Python virtual environment (excluded from Git)
│
├── student/              # The Django project folder
│   ├── __init__.py
│   ├── settings.py       # Global settings like apps, middleware, DB, etc.
│   ├── urls.py           # Root URL configurations
│   ├── wsgi.py           # For WSGI deployment
│
├── stu_info/                 # First Django app (e.g., 'students')
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── auth_stu/                 # Second Django app (e.g., 'accounts' for auth)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── templates/            # Shared HTML templates for all apps
│   ├── base.html
│   └── (app-specific templates)
│
├── manage.py             # Django command-line utility
│
├── requirements.txt      # All required Python packages
│
├── .gitignore            # Files and folders Git should ignore
│
└── README.md             # Project documentation
```
