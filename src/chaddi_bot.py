from loguru import logger
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from util import config, util
from datetime import time
import pytz

import handlers
from domain import jobs

# Get application config
chaddi_config = config.get_config()

# Logger config
logger.add(
    "../logs/chaddi.log",       # chaddi-tg/logs/
    compression="zip",          # Compress the rotated logs
    rotation="12:00"            # New file is created each day at noon
)


def main():
    util.print_title()

    # Create the Updater and pass it your bot's token.
    updater = Updater(chaddi_config["tg_bot_token"], use_context=True)

    job_queue = updater.job_queue

    # Schedule the required timer based jobs
    jobs.schedule_timer_jobs(job_queue)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("hi", handlers.hi.handle))
    dp.add_handler(CommandHandler("about", handlers.about.handle))
    dp.add_handler(CommandHandler("calc", handlers.calc.handle))
    dp.add_handler(CommandHandler("choose", handlers.choose.handle))
    dp.add_handler(CommandHandler("chutiya", handlers.chutiya.handle))
    dp.add_handler(CommandHandler("mom", handlers.mom.handle))
    dp.add_handler(CommandHandler("gamble", handlers.gamble.handle))
    dp.add_handler(CommandHandler("quotes", handlers.quotes.handle))
    dp.add_handler(CommandHandler("quote", handlers.quotes.handle))
    dp.add_handler(CommandHandler("rokda", handlers.rokda.handle))
    dp.add_handler(CommandHandler("superpower", handlers.superpower.handle))
    dp.add_handler(CommandHandler("daan", handlers.daan.handle))
    dp.add_handler(CommandHandler("set", handlers.setter.handle))
    dp.add_handler(CommandHandler("roll", handlers.roll.handle))
    dp.add_handler(CommandHandler("reset", handlers.reset.handle))

    dp.add_handler(MessageHandler(Filters.status_update, handlers.default.status_update))
    dp.add_handler(MessageHandler(Filters.all, handlers.default.all))

    # Log all errors
    dp.add_error_handler(handlers.error.log_error)

    # Start the Bot
    updater.start_polling()

    logger.info("Started Polling...")

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
