# import authentication as bot_auth
# import info_chat as ic
# import message as msg
# import asyncio

# ## dotenv
# bot_token = "6372410602:AAG7dd74ZkstDsOErcOQtoRHOqD4YgsBJpM"
# admin_id = "1331000174"

# asyncio.run(bot_auth.authentication_bot(bot_token))

# while(1):
#     temp_id = asyncio.run(ic.get_id_last_message_chat(bot_token))

#     if (temp_id == admin_id):
#         temp_message = "Mensagem recebida"
#         msg.send_message(admin_id, temp_message)

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import message as msg

bot_token = "6372410602:AAG7dd74ZkstDsOErcOQtoRHOqD4YgsBJpM"
admin_id = "1331000174"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(bot_token).build()

    start_handler = CommandHandler('status', msg.status_command())
    application.add_handler(start_handler)

    application.run_polling()