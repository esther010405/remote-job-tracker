from telegram import Bot
import asyncio
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN=os.getenv("TOKEN")

async def get_updates():
    bot = Bot(token=TOKEN)

    updates = await bot.get_updates()

    for update in updates:
        print(update.message.chat.id)

asyncio.run(get_updates())