import os
import asyncio
import random
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReactionTypeEmoji
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from multiprocessing import Process, set_start_method

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

load_dotenv()

# Load env variables
EMOJI_LIST = os.getenv("EMOJI_LIST", "").split(",")
RANDOM_LEVEL = int(os.getenv("RANDOM_LEVEL", 5))
BOT_TOKENS = os.getenv("BOT_TOKENS", "").split(",")


def get_random_reaction():
    return [ReactionTypeEmoji(emoji=random.choice(EMOJI_LIST))]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    name = chat.first_name if chat.type == "private" else chat.title
    keyboard = [
        [
            InlineKeyboardButton("➕ Add to Channel ➕", url=f"https://t.me/{context.bot.username}?startchannel=botstart"),
            InlineKeyboardButton("➕ Add to Group ➕", url=f"https://t.me/{context.bot.username}?startgroup=botstart")
        ]
    ]
    await update.message.reply_text(
        f"Hello {name}! 🤖 I'm {context.bot.username} and I’m ready to react!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def delayed_react(context, chat_id, message_id):
    try:
        delay = random.uniform(1, RANDOM_LEVEL)
        await asyncio.sleep(delay)
        emoji = random.choice(EMOJI_LIST)

        await context.bot.set_message_reaction(
            chat_id=chat_id,
            message_id=message_id,
            reaction=[ReactionTypeEmoji(emoji=emoji)]
        )
        logger.info(f"{context.bot.username} reacted with {emoji} after {delay:.2f}s delay")
    except Exception as e:
        logger.error(f"{context.bot.username} failed to react: {e}")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    if not message:
        return

    if message.chat.type in ["channel", "group", "supergroup"]:
        # 50% chance this bot won't react at all (adjust as needed)
        if random.random() < 0.05:
            logger.info(f"{context.bot.username} skipped reacting to message {message.message_id}")
            return

        # schedule reaction without blocking
        asyncio.create_task(delayed_react(context, message.chat_id, message.message_id))


def run_bot(token):
    app = Application.builder().token(token.strip()).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_message))
    app.run_polling()


async def main():
    if not BOT_TOKENS or not any(t.strip() for t in BOT_TOKENS):
        print("⚠ No bot tokens found in .env (BOT_TOKENS). Add them as comma separated values.")
        return

    processes = []
    for token in BOT_TOKENS:
        if token.strip():
            p = Process(target=run_bot, args=(token,))
            p.start()
            processes.append(p)

    for p in processes:
        p.join()


if __name__ == "__main__":
    set_start_method("spawn")  # ensures a fresh event loop in each process
    asyncio.run(main())
