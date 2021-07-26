import discord
import logging
import random

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Bot is online.")

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('$whatis'):
            split_message = message.content.split(' ')
            try:
                if split_message[2] == '+':
                    await message.channel.send(f"The sum is {float(split_message[1]) + float(split_message[3])}")

                elif split_message[2] == '-':
                    await message.channel.send(f"The sum is {float(split_message[1]) - float(split_message[3])}")

                elif split_message[2] == 'x' or split_message[2] == '*':
                    await message.channel.send(f"The sum is {float(split_message[1]) * float(split_message[3])}")

                elif split_message[2] == '/':
                    await message.channel.send(f"The sum is {float(split_message[1]) / float(split_message[3])}")

            except:
                await message.channel.send(f"Invalid operators within '{split_message[1]} {split_message[2]} {split_message[3]}'")

        elif message.content.startswith('$quote'):
            with open('discordBot_quotes.txt', 'r') as file:
                n = random.randint(0, 99)
                all_quotes = file.read().split('\n')
                await message.channel.send(all_quotes[n])





client = MyClient()
client.run('ODYyNDM1Mzg1Njg1MzExNDk4.YOYTiw.srwvyy_4tVk-v0YMUwDU8kUZpuA')
