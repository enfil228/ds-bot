import discord
from discord.ext import commands, tasks
from datetime import datetime
import pytz

TOKEN = 'fff'
CHANNEL_ID = '1273376272768303218'  # Укажите ID канала, куда будет отправлено сообщение
MESSAGE = '<@706547063738990613> пруфыыыыы'
SCHEDULE_TIME = '20:00'  # Укажите время в формате HH:MM

bot = commands.Bot(command_prefix='!')

@tasks.loop(seconds=60)  # Проверка каждую минуту
async def send_message():
    now = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%H:%M')
    if now == SCHEDULE_TIME:
        channel = bot.get_channel(int(CHANNEL_ID))
        await channel.send(MESSAGE)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    send_message.start()  # Запуск задачи

bot.run(TOKEN)
