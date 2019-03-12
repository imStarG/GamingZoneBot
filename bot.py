import discord
import youtube_dl
from discord.ext import commands
import asyncio
from itertools import cycle

TOKEN = 'NTU0MDMxNzAyNDc4MTU5ODcy.D2WtwQ.y9Se_GJ-l63eMtLwMAPGuPashWI'

client = commands.Bot(command_prefix = '.')
status = ['תכתוב .help', '!הירשמו לפורום שלנו', 'GamingZone.co.il']



async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(3)

players = {}

@client.event
async def on_ready():
    print('Running.')

@client.command()
async def hello():
    await client.say('Hello!')

@client.command()
async def say(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('ההודעות נמחקו.')


@client.command()
async def ipsurf():
    await client.say('__**Surf IP**__                                                                             ```Surf - 185.185.134.225:27500```')


@client.command()
async def ipjail():
    await client.say('__**JailBreak IP**__                                                                             ```JailBreak - 185.185.134.225:27600```')


@client.command()
async def ipfun():
    await client.say('__**Fun IP**__                                                                             ```Fun - 185.185.134.225:27700```')


@client.command()
async def ipretakes():
    await client.say('__**Retakes IP**__                                                                             ```Retakes#1 - 185.185.134.225:27800      Retakes#2 - 185.185.134.225:27900      Retakes#3 - 185.185.134.225:28000```')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    await client.say('אני בא!')

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    await client.say('ביי הלכתי...')

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()
    await client.say('יאללה אני מתחיל לנגן את השיר!')

@client.command(pass_context=True)
async def skip(ctx):
    id = ctx.message.server.id
    players[id].stop()
    await client.say('...גם ככה חרא שיר')


@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()
    await client.say('ממשיך!')

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].pause()
    await client.say('עוצר!')


@client.command()
async def admin():
    await client.say('רוצים להגיש בקשה לאדמין? היכנסו לקישור __▼**כאן למטה**▼__ ותגישו בקשה                                                                                                                                                                            https://www.gamingzone.co.il/index.php?/application/form/1-%D7%93%D7%A8%D7%95%D7%A9%D7%99%D7%9D-csgo/')



@client.command()
async def forum():
    await client.say('__**הירשמו לפורום שלנו!**__                                                                                                                                                                                                         https://www.gamingzone.co.il')



@client.command()
async def rules():
    await client.say('תקרא בצאנל של החוקים מה אני עבד שלך')








client.loop.create_task(change_status())
client.run(TOKEN)
