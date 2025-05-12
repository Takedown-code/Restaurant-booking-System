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

---

## 🛠️ Tech Stack

| Layer     | Tech                          |
|-----------|-------------------------------|
| Backend   | Python, Django                |
| Database  | SQLite (relational database)  |
| Frontend  | HTML, CSS, Bootstrap          |
| Styling   | Custom CSS + Bootstrap CDN    |
| Hosting   | Localhost or Render.com       |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/restaurant-booking-system.git
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
pip install django
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

## 🗂️ Project Structure

```
restaurant_booking/
├── bookings/              # Main app (views, models, forms, templates)
│   ├── templates/bookings/
│   ├── static/bookings/css/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
├── config/                # Project settings
├── db.sqlite3             # Local database
├── manage.py              # Django management script
├── README.md              # Project info
└── .gitignore             # Ignored files
```

---

## ✅ Requirements Checklist

- [x] Relational Database with models and foreign key relationships  
- [x] CRUD Functionality for bookings  
- [x] User Interface with custom CSS and structured layout  
- [x] Main navigation and mobile-friendly design  
- [x] README and proper attribution  
- [x] Version Control with Git & GitHub  
- [x] Deployment-ready (can be hosted on Render)  

---

## 📝 Attribution

- Built with Django: https://www.djangoproject.com/  
- Bootstrap 5 via CDN: https://getbootstrap.com/  
- Icons and emojis are used under open web usage  
- **Assisted by AI** (ChatGPT) for project structure guidance and problem solving

---

## 💡 Future Improvements

- User authentication (customer logins)  
- Email confirmations for bookings  
- Availability calendar and time slot limits  

---
