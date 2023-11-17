import telegram

async def get_id_last_message_chat(bot_token):
    bot = telegram.Bot(bot_token)
    async with bot:
        temp_id = (await bot.get_updates())[0].message.chat.id
        return temp_id