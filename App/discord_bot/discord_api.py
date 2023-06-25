from dotenv import load_dotenv
import discord
import os
from App.chat_gpt.openai import chatgpt_response

load_dotenv()

discord_token = os.getenv('DISC_TOKEN')

class Client(discord.Client):
    async def on_ready(self):
        print("Successfully logged in as: ", self.user)

    async def on_message(self, message):
        #print(message.content)
        if message.author == self.user:
            return

        command = None
        user_message = None

        if message.content.startswith("/chatgpt"):
            command = message.content.split(' ')[0]
            user_message = message.content.replace("/chatgpt", '')
            #print(command, user_message)

        if command == '/chatgpt':
            bot_response = chatgpt_response(user_message)
            print(bot_response)
            await message.channel.send(bot_response)
        
intents = discord.Intents.default()
intents.message_content = True
client = Client(intents=intents)