# Restaurant Booking System

A full-stack web application built with **Django** and **SQLite** that allows restaurant owners and customers to manage table bookings. The system includes a user-friendly interface to view, create, update, and cancel reservations.

---

## 📌 Features

* 📅 View all bookings with customer name, table, and time
* 📝 Create a new booking with responsive forms
* 🔁 Update or delete existing bookings
* 🍽 Manage tables and menu items via Django admin panel
* ✅ Status system to track active vs cancelled bookings
* 💻 Clean, mobile-friendly layout with Bootstrap 5
* 📆 Uses HTML5 `datetime-local` input for smooth date/time selection

---

## 🛠️ Tech Stack

| Layer    | Tech                         |
| -------- | ---------------------------- |
| Backend  | Python, Django               |
| Database | SQLite (relational database) |
| Frontend | HTML, CSS, Bootstrap         |
| Styling  | Custom CSS + Bootstrap CDN   |
| Hosting  | Heroku                       |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Takedown-code/Restaurant-booking-System.git
cd Restaurant-booking-System
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations & Create Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://localhost:8000](http://localhost:8000)
Admin panel: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 🌍 Deployment (Heroku)

### 1. Create `.python-version` in project root:

```
3.11
```

### 2. Create `Procfile` in project root:

```
web: gunicorn config.wsgi:application
```

### 3. Update `config/settings.py`:

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1,restaurant-booking-system-code-5eaa10e9c500.herokuapp.com').split(',')
```

### 4. Deploy to Heroku

```bash
heroku login
heroku create your-app-name
heroku config:set DISABLE_COLLECTSTATIC=1 SECRET_KEY='your-secret-key' DEBUG=False
git add .
git commit -m "Prepare Heroku deployment"
git push heroku main
heroku run python manage.py migrate
heroku open
```

Live URL: `https://restaurant-booking-system-code-5eaa10e9c500.herokuapp.com`

---

## 🗂️ Project Structure

```
Restaurant-booking-System/
├── bookings/
│   ├── migrations/
│   ├── static/
│   │   └── bookings/
│   │       └── css/
│   │           └── style.css
│   ├── templates/
│   │   └── bookings/
│   │       ├── booking_confirm_delete.html
│   │       ├── booking_form.html
│   │       └── booking_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
├── .python-version
├── Procfile
└── README.md
```

---

## ✅ Requirements Checklist

* [x] Relational database models with FK relationships
* [x] Full CRUD operations for bookings
* [x] Clean and structured HTML/CSS UI
* [x] Bootstrap 5 styling and mobile-responsiveness
* [x] Django admin panel for management
* [x] Deployment-ready on Heroku
* [x] Comprehensive README

---

## 📝 Attribution

* Built with Django: [https://www.djangoproject.com/](https://www.djangoproject.com/)
* Bootstrap 5 via CDN: [https://getbootstrap.com/](https://getbootstrap.com/)
* Icons and emojis are used under open web usage
* **Assisted by ChatGPT** for guidance

---

## 💡 Future Improvements

* User authentication (customer logins)
* Email confirmations for bookings
* Availability calendar and time-slot limits
