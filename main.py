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

        elif message.content.startswith('$roulette'):
            # try:
                split_message = message.content.split(' ')
                with open('roulette_profiles.txt', 'r+') as f:
                    all_content = f.read().split('\n')
                    exists = False
                    user_location = 0
                    if ('' in all_content):
                        all_content.remove('')  # Remove extra newline residue.
                    for i in range(0, len(all_content)):
                        all_content[i] += "\n"  # Add back the newline we stripped during split.
                        if all_content[i].startswith(str(message.author.id)):
                            exists = True
                            user_location = i

                    if split_message[1].startswith('bet'):
                        roll = random.randint(0, 36)
                        user_score = all_content[user_location].split(' ')

                        if roll > 18:
                            await message.channel.send("rolled red...")
                            if split_message[3] == 'red':
                                all_content[user_location] = f"{message.author.id} {int(user_score[1]) + int(split_message[2])}\n"
                                await message.channel.send("you win!")
                            else:
                                all_content[user_location] = f"{message.author.id} {int(user_score[1]) - int(split_message[2])}\n"
                                await message.channel.send("you lose!")

                        elif roll > 0:
                            await message.channel.send("rolled black...")
                            if split_message[3] == 'black':
                                all_content[user_location] = f"{message.author.id} {int(user_score[1]) + int(split_message[2])}\n"
                                await message.channel.send("you win!")
                            else:
                                all_content[user_location] = f"{message.author.id} {int(user_score[1]) - int(split_message[2])}\n"
                                await message.channel.send("you lose!")

                        elif roll == 0:
                            await message.channel.send("rolled green...")
                            if split_message[3] == 'green':
                                all_content[user_location] = f"{message.author.id} {int(user_score[1]) + int(split_message[2]) * 34}\n"
                                await message.channel.send("you win!")
                            else:
                                all_content[user_location] = f"{message.author.id} {int(user_score[1]) - int(split_message[2])}\n"
                                await message.channel.send("you lose!")

                    elif split_message[1].startswith('reset'):
                        all_content[user_location] = f"{message.author.id} 100\n"

                    f.seek(0)
                    f.truncate(0)
                    f.writelines(all_content)
            # except:
            #     await message.channel.send(f"{message.author.mention} Invalid syntax within '{message.content}'. Syntax should be '$roulette <bet, reset, or balance> <amount> <colour (red, black, green)>'")

        elif message.content.startswith('$quote'):
            with open('discordBot_quotes.txt', 'r') as file:
                n = random.randint(0, 99)
                all_quotes = file.read().split('\n')
                await message.channel.send(all_quotes[n])

        elif message.content.startswith('$kick'):
            split_message = message.content.split(' ', 1)
            try:
                mentioned_user = client.fetch_user(message.mentions[0].id)
                mentioned_user = await mentioned_user
                await message.guild.kick(mentioned_user, reason=split_message[1])
            except:
                await message.channel.send(f"{message.author.mention} Invalid syntax within '{message.content}'. Syntax should be '$kick <mention user> <reason>'")

        elif message.content.startswith('$ban'):
            split_message = message.content.split(' ', 1)
            try:
                mentioned_user = client.fetch_user(message.mentions[0].id)
                mentioned_user = await mentioned_user
                await message.guild.ban(mentioned_user, reason=split_message[1], delete_message_days=0)
            except:
                await message.channel.send(f"{message.author.mention} Invalid syntax within '{message.content}'. Syntax should be '$ban <mention user> <reason>'")

        elif message.content.startswith('$giverole'):
            try:
                mentioned_member = message.guild.fetch_member(message.mentions[0].id)
                mentioned_member = await mentioned_member
                await mentioned_member.add_roles(message.role_mentions[0])
            except:
                await message.channel.send(f"{message.author.mention} Invalid syntax within '{message.content}'. Syntax should be '$giverole <mention user> <mention role>'")

        elif message.content.startswith('$help'):
            await message.channel.send("""$whatis <number> <operator> <number>: Returns the result of the input mathematical equation
$quote: Return a random quote from a list of 100
$kick <mention user> <reason>: Kicks the mentioned user with the given reason
$ban <mention user> <reason>: Bans the mentioned user with the given reason
$giverole <mention user> <mention role>: Gives the mentioned user the mentioned role""")

        elif message.content.count('badword') != 0 or message.content.count('swearword') != 0 or message.content.count('notokword') != 0:
            await message.delete()
            await message.channel.send(f"{message.author.mention} said a bad word. The message has been deleted.")


client = MyClient()
client.run('insert token')
