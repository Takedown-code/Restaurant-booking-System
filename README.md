# Restaurant Booking System

A full-stack web application built with **Django** and **SQLite** that allows restaurant owners and customers to manage table bookings. The system includes a user-friendly interface to view, create, update, and cancel reservations.

---

## 📌 Features

- 📅 View all bookings with customer name, table, and time  
- 📝 Create a new booking with responsive forms  
- 🔁 Update or delete existing bookings  
- 🍽 Manage tables and menu items via Django admin panel  
- ✅ Status system to track active vs cancelled bookings  
- 💻 Clean, mobile-friendly layout with Bootstrap 5  
- 📆 Uses HTML5 `datetime-local` input for smooth date/time selection  

---

## 🛠️ Tech Stack

| Layer     | Tech                          |
|-----------|-------------------------------|
| Backend   | Python, Django                |
| Database  | SQLite (relational database)  |
| Frontend  | HTML, CSS, Bootstrap          |
| Styling   | Custom CSS + Bootstrap CDN    |
| Hosting   | Render.com                    |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Takedown-code/Restaurant-booking-System.git
cd restaurant-booking-system
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

## 🌍 Deployment

This project is deployed on **Render**.  
Live URL: `https://restaurant-booking-system-ukt9.onrender.com`  
Start command (for Render settings):
```
python manage.py migrate && gunicorn config.wsgi:application
```

---

## 🗂️ Project Structure

```
restaurant-booking-system/
├── bookings/                  # Main Django app
│   ├── migrations/            # Database migrations
│   ├── static/                # Static files (CSS, JS)
│   ├── templates/bookings/    # HTML templates
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config/                    # Project configuration (settings, urls, wsgi)
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management utility
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## ✅ Requirements Checklist

- [x] Relational Database with models and foreign key relationships  
- [x] CRUD Functionality for bookings  
- [x] User Interface with custom CSS and structured layout  
- [x] Main navigation and mobile-friendly design  
- [x] README and proper attribution  
- [x] Version Control with Git & GitHub  
- [x] Deployment-ready (Render-compatible)  

---

## 📝 Attribution

- Built with Django: https://www.djangoproject.com/  
- Bootstrap 5 via CDN: https://getbootstrap.com/  
- Icons and emojis are used under open web usage  
- **Assisted by ChatGPT** for project structure and debugging guidance

---

## 💡 Future Improvements

- User authentication (customer logins)  
- Email confirmations for bookings  
- Availability calendar and time slot limits  
