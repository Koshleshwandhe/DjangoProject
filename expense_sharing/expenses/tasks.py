# expenses/tasks.py

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_weekly_emails():
    # Logic to send weekly summary emails
    # Use the Django email sending functionality here
    send_mail(
        'Weekly Summary',
        'This is a summary of your expenses for the week.',
        'your_email@example.com',
        ['recipient@example.com'],
        fail_silently=False,
    )
