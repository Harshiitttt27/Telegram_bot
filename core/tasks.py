from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task()
def send_welcome_email(username, email):
    subject = 'Welcome to the Telegram Bot!'
    message = f'Hi {username}, thanks for using our bot.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return f"Email sent to {email}"
    except Exception as e:
        return f"Failed to send email: {str(e)}"
