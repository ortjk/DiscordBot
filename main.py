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
                    await message.channel.send(f"{message.author.mention} The sum is {float(split_message[1]) + float(split_message[3])}")

                elif split_message[2] == '-':
                    await message.channel.send(f"{message.author.mention} The sum is {float(split_message[1]) - float(split_message[3])}")

                elif split_message[2] == 'x' or split_message[2] == '*':
                    await message.channel.send(f"{message.author.mention} The sum is {float(split_message[1]) * float(split_message[3])}")

                elif split_message[2] == '/':
                    await message.channel.send(f"{message.author.mention} The sum is {float(split_message[1]) / float(split_message[3])}")

            except:
                await message.channel.send(f"{message.author.mention} Invalid operators within '{split_message[1]} {split_message[2]} {split_message[3]}'")

        elif message.content.startswith('$quote'):
            with open('discordBot_quotes.txt', 'r') as file:
                n = random.randint(0, 99)
                all_quotes = file.read().split('\n')
                await message.channel.send(all_quotes[n])

        elif message.content.startswith('$kick'):
            split_message = message.content.split(' ', 1)
            try:
                print(message.mentions)
            except:
                await message.channel.send(f"{message.author.mention} Invalid syntax within '{message.content}'. Syntax should be '$kick <mention user>")

        elif message.content.startswith('$ban'):
            split_message = message.content.split(' ', 1)
            try:
                print(message.mentions)
            except:
                await message.channel.send(f"{message.author.mention} Invalid syntax within '{message.content}'. Syntax should be '$ban <mention user>")

        elif message.content.startswith('$giverole'):
            try:
                print(message.mentions)
                print(message.role_mentions)
            except:
                await message.channel.send(f"{message.author.mention} Invalid syntax within '{message.content}'. Syntax should be '$giverole <mention user> <mention role>")

        elif message.content.startswith('$help'):
            await message.channel.send("""$whatis <number> <operator> <number>: Returns the result of the input mathematical equation
            $quote: Return a random quote from a list of 100
            $kick <mention user> <reason>: Kicks the mentioned user and sends them the reason
            $ban <mention user> <reason>: Bans the mentioned user and sends them the reason
            $giverole <mention user> <mention role>: Gives the mentioned user the mentioned role""")

        elif message.content.startswith('badword' or 'swearword' or 'notokword'):
            await message.delete()
            await message.channel.send(f"{message.author.mention} said a bad word. The message has been deleted.")


client = MyClient()
client.run('ODYyNDM1Mzg1Njg1MzExNDk4.YOYTiw.srwvyy_4tVk-v0YMUwDU8kUZpuA')
