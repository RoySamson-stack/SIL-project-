```markdown
# SIL-project

## Overview
A simple Django project to manage customers and orders using a REST API, SMS notifications via Africa's Talking API, and OpenID authentication. This project includes unit tests and CI/CD integration using GitHub Actions.

## Features
- Customer and Order Management
- REST API
- SMS notification using Africa's Talking API
- OpenID Connect (OIDC) for authentication
- Unit testing with CI/CD using GitHub Actions

## Prerequisites
- Python 3.12.3
- Django 4.x
- Africa's Talking API credentials
- Google OpenID Connect credentials

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/SIL-project.git
   cd SIL-project
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your credentials:
   ```ini
   # .env file
   AT_USERNAME=sandbox
   AT_API_KEY=your-africastalking-api-key
   OIDC_RP_CLIENT_ID=your-client-id
   OIDC_RP_CLIENT_SECRET=your-client-secret
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
### Sending SMS
To send an SMS notification, the `send_sms` function is used:
```python
import africastalking

def send_sms(phone_number, message):
    try:
        response = africastalking.SMS.send(message, [phone_number])
        print(f"SMS sent successfully: {response}")
    except Exception as e:
        print(f"Encountered an error while sending: {e}")
```

### Authentication
The project uses OpenID Connect for authentication. Ensure you have the following settings in your `settings.py`:
```python
OIDC_RP_CLIENT_ID = 'your-client-id'
OIDC_RP_CLIENT_SECRET =