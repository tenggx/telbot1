import logging
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     logging.info("------------- start begin -------------")
#     await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
#     logging.info("------------- start end   -------------")


# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    logging.info(update)
    logging.info(update.effective_chat.title)
    logging.info(update.effective_chat.id)
    await update.message.reply_text(update.message.text)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("------------- caps begin -------------")
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
    logging.info("------------- caps begin -------------")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


if __name__ == '__main__':
    application = ApplicationBuilder().token('6221601248:AAEoCC-VGrNi4EiIWpqawBiL0aaSlu92bUQ').build()

    # start_handler = CommandHandler('start', start)
    # echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    # caps_handler = CommandHandler('caps', caps)

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('caps', caps))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))

    application.run_polling()
