import discord
from bot_logic import gen_pass
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$прив'):
        await message.channel.send("вечер в хату!")
    elif message.content.startswith('$как дела?'):
        await message.channel.send("Всё кайфово")
    elif message.content.startswith('$мне грустно'):
        await message.channel.send("Вот посмотри: https://www.youtube.com/watch?v=mIYoasoNa5M")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(12))
    else:
        await message.channel.send(message.content)

client.run("MTE0NzgyOTYwMTY3MDgxMTcyOA.G14usP.iGCO9lB5OfrRizZkBxLCZlS8avg9U0GfUcOt2U")
