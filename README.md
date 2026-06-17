TeamNext ERP

A web-based ERP (Enterprise Resource Planning) system built using Django and SQLite, designed to manage organizational workflows, employees, and tasks in a centralized platform.

🚀 Features
User authentication (Login / Logout)
Employee management system
Task & project tracking
Admin dashboard (Django Admin)
CRUD operations using Django ORM
Lightweight SQLite database
🛠️ Tech Stack
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap
Database: SQLite3
Version Control: Git
📁 Project Structure
teamnext_erp/
│── manage.py
│── db.sqlite3
│
├── teamnext_erp/
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py / wsgi.py
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│
└── static/
⚙️ Getting Started
1. Clone the repository
git clone https://github.com/your-username/teamnext-erp.git
cd teamnext-erp
2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Apply migrations
python manage.py migrate
5. Run the server
python manage.py runserver
