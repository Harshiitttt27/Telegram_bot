from django.core.management.base import BaseCommand
from telegram.ext import ApplicationBuilder, CommandHandler
from core.models import TelegramUser
from django.conf import settings
from asgiref.sync import sync_to_async


from core.tasks import send_welcome_email


@sync_to_async
def save_user_and_email(username):
    TelegramUser.objects.get_or_create(username=username)
    send_welcome_email.delay(username, 'test@example.com')  # Replace with actual email 

async def start(update, context):
    username = update.effective_user.username
    print(f"Received /start from: {username}")
    if username:
        await save_user_and_email(username)
        await update.message.reply_text(f"Hi {username}, you are registered!")
    else:
        await update.message.reply_text("No username found.")


class Command(BaseCommand):
    help = 'Run the Telegram bot and listen for /start'

    def handle(self, *args, **kwargs):
        print(" Telegram Bot is polling...")

        app = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.run_polling()
