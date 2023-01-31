from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from bots_commands import *

app = ApplicationBuilder().token("5852812651:AAGAGM30H-1vB1XF5A6FdmvqqTH0C4ovyFw").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("calc", calc_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sub", sub_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("div", div_command))
app.add_handler(CommandHandler("exp", exp_command))

print('server start')
app.run_polling()
