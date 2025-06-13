# Django Internship Assignment

This is a Django-based backend project completed as part of an internship assignment. It includes API development using Django REST Framework, authentication, Celery for background tasks, Redis, and Telegram bot integration.

---
## 🛠 Tech Stack

| Component   | Technology        |
|-------------|------------------|
| Backend     | Django 4.x + DRF |
| Language    | Python 3.11.8     |
| Auth        | Token Authentication |
| Queue       | Celery            |
| Broker      | Redis             |
| Bot         | Telegram Bot API ([@test_9471_bot](https://t.me/test_9471_bot)) |
| Testing     | Postman           |

---

## 🚀 Features

1. **Django Project Setup**
   - DEBUG = False for production mode.
   - Secrets and credentials managed via `.env` file.

2. **API Development**
   - **Public Endpoint**: Open to all users.
   - **Protected Endpoint**: Requires authentication using Django Token Authentication.
   - User registration and login via API and Django admin panel.

3. **Celery Integration**
   - Celery configured with Redis as the broker.
   - Sends an email to the user after successful registration.

4. **Telegram Bot Integration**
   - Telegram bot (`@test_9471_bot`) listens for `/start` command.
   - Stores the user's Telegram username in the database.

---



## Clone the repository 
```bash

git clone https://github.com/Harshiitttt27/Telegram_bot.git
```
## Create virtual env
```bash
 python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
## Set up .env file
Create a .env file in the root directory and include:-

```
SECRET_KEY=your_secret_key
DEBUG=False
TELEGRAM_BOT_TOKEN=your_bot_token
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=your_email@gmail.com
```
# Django settings
SECRET_KEY=your_django_secret_key
DEBUG=False

# Telegram Bot
TELEGRAM_BOT_TOKEN=your_telegram_bot_token

# Email Settings (Gmail SMTP)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_app_password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=your_email@gmail.com

##  Add .env to .gitignore
 This will prevent your private .env file from ever being committed to GitHub.

## Run Migrations
```bash
python manage.py makmigrations
python manage.py migrate
```

##  Start Celery Worker
```bash
celery -A telegram_bot worker --pool=solo --loglevel=info
```

## Start Telegram Bot
```bash
python manage.py run_telegram_bot
```
## Run Server
```bash
python manage.py runserver
```

---

## 🌐 API Endpoints

| Method | Endpoint                               | Access        | Description                                      |
|--------|----------------------------------------|---------------|--------------------------------------------------|
| POST   | `/api/login/`                          | Public        | Get auth token using username/password           |
| GET    | `/api/public/`                         | Public        | Open public endpoint                             |
| GET    | `/api/protected/`                      | Auth Required | Protected endpoint for logged-in users           |
| GET    | `/api/telegram-users/`                 | Public/Auth   | List all Telegram users stored                   |
| GET    | `/api/simulate-start/`                 | Public        | Simulates a Telegram bot `/start` registration   |


## API Testing
 Testing with Postman
Import endpoints manually or create a Postman collection.

Test login and token-based authentication.

Test Telegram endpoints and simulate user registration.

## Telegram Bot
Bot Username: @test_9471_bot

Command: /start

Action: Saves your Telegram username in the backend database.


## Author
### Harshit Sethi
For any details or queries, contact: harrysethi52@gmail.com


## Notes
All secrets are secured via .env

.env is ignored via .gitignore

Focused on production-quality, clean code and modular structure.


