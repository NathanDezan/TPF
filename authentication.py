import telegram
import info_chat as ic

async def authentication_bot(bot_token):
    bot = telegram.Bot(bot_token)
    async with bot:
        print(await bot.get_me())