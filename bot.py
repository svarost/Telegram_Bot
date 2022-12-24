import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import *
# from controllers import *



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    app = ApplicationBuilder().token("5714842386:AAHw96gypiuk4F26Rg87VSWiD--scNVx_vM").build()

    app.add_handler(CommandHandler('start', help_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler("hi", hi_command))
    app.add_handler(CommandHandler("time", time_command))
    app.add_handler(CommandHandler("sum", sum_command))
    app.add_handler(CommandHandler("choice_action", choice_action))
    app.add_handler(CommandHandler("1", add_list))
    app.add_handler(CommandHandler("2", full_list))
    
    app.run_polling()