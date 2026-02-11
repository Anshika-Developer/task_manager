# 📝 Task Manager – Django Web Application

  
This is a Task Manager project built using Django and Django REST Framework.

This will help to Track the Task and there status.

---

## Features

### Web Features
- Create a new task
- Update existing task
- Delete task
- Filter by Status (Pending / Completed)
- Filter by Priority (Low / Medium / High)
- Task statistics (Total / Completed / Pending)

### API Features
- GET all tasks
- POST new task
- PUT update task
- DELETE task

---

## 🛠 Tech Stack

- Python 3
- Django
- Django REST Framework
- SQLite
- Gunicorn
- Nginx
- AWS EC2 (Ubuntu)

---


## ⚙️ Run Project Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Anshika-Developer/task_manager.git
cd task_manager
```

### 2️⃣ Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have requirements.txt, install manually:

```bash
pip install django djangorestframework gunicorn
```

### 4️⃣ Apply migrations

```bash
python manage.py migrate
```

### 5️⃣ Run development server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---
## Production URL

```commandline
http://13.235.18.129

```
## API Endpoints

Base URL:

```
http://13.235.18.129/api/tasks/
```

| Method | Endpoint | Description |
|--------|----------|------------|
| GET | /api/tasks/ | Get all tasks |
| POST | /api/tasks/ | Create task |
| PUT | /api/tasks/<id>/ | Update task |
| DELETE | /api/tasks/<id>/ | Delete task |

---

## 🌍 Production Deployment (AWS EC2)

This project is deployed on AWS EC2 using:

- Gunicorn as WSGI server
- Nginx as reverse proxy
- Systemd service for managing Gunicorn

Gunicorn runs using a Unix socket and Nginx forwards HTTP traffic (port 80) to Gunicorn.

Security Group allows:
- Port 22 (SSH)
- Port 80 (HTTP)
- Port 443 (HTTPS)

---

## 👩‍💻 Author

Anshika Gupta  
Python Developer  

