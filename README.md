# Django Project

This is a web project built with **Django**, designed as a base for developing scalable web applications.  
It includes an initial configuration, organized structure, and examples to quickly extend functionality.

---

## 🚀 Technologies Used
- [Python 3.x](https://www.python.org/)
- [Django 4.x](https://www.djangoproject.com/)
- SQLite3 (default database)
- HTML, CSS, JavaScript
 
---
 
## 📂 Project Structure
 
Django-Project/
│── app/ # Main Django application
│── mediaFiles/ # User-uploaded files
│── static/ # Static files (CSS, JS, images)
│── templates/ # HTML templates
│── db.sqlite3 # Local database (ignored in production)
│── manage.py # Django management script
│── requirements.txt # Project dependencies


---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/MiguelAntonioRS/Django-Project.git
   cd Django-Project

2. **Create and activate a virtual environment**
  ```bash
  python -m venv venv
  source venv/bin/activate   # On Linux/Mac
  venv\Scripts\activate      # On Windows
 ```
 3. **Install dependencies**
    pip install -r requirements.txt

4. **Apply migrations**
   python manage.py migrate

5. **Run the development server**
   python manage.py runserver

6. **Open your browser and go to:**
   http://127.0.0.1:8000/

## 📌 Features

- Django project boilerplate  
- Organized structure for scalability  
- Static and media file management  
- Easy setup for development  
