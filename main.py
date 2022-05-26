from email.mime import image
from turtle import title
import discord
from  discord.ext import commands
from datetime import date, datetime, timedelta

#client = discord.Client()

bot = commands.Bot(command_prefix='!', help_command=None)

# wrapper / decorator

message_lastseen = datetime.now()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def test(ctx, *, par):    
    await ctx.channel.send("You typed {0}".format(par))

@bot.command()
async def help(ctx):
    emBed = discord.Embed(title="Tutorial Bot help", description="All available bot commands", color=0x42f5a7)
    # help
    emBed.add_field(name="help", value="Get help command", inline=False)
    # test
    emBed.add_field(name="test", value="Respond message that you've send", inline=False)
    # send
    emBed.add_field(name="send", value="Send hello message to user", inline=False)
    
    emBed.set_thumbnail(url='https://cms.kapook.com/uploads/tag/3/thumb_2773_573302db2d68e.jpg')
    #emBed.set_footer(text='test footer', icon_url='')
    await ctx.channel.send(embed=emBed)

@bot.command()
async def send(ctx):
    await ctx.channel.send("Hello")

@bot.event
async def on_message(message):
    global message_lastseen

    if message.content == '!user':
        await message.channel.send(str(message.author.name) + ' Hello')
    elif message.content == '!logout':
        await bot.logout()
    elif message.content == 'ขนาดนั้นเลย':
        await message.channel.send("ขนาดนั้นเเหละ")
    elif message.content == 'เหนื่อยว่ะพรี่เท่ง':
        await message.channel.send("เรื่องของมึง " + str(message.author.name))
    elif message.content == 'บอทเก๊' or message.content == 'kak' or message.content == 'บอทกาก':
        await message.channel.send("1-1ไหมสึด " + str(message.author.name))
    elif message.content == 'พรี่เท่ง' and datetime.now() >= message_lastseen:
        message_lastseen = datetime.now() + timedelta(seconds=5)
        await message.channel.send(str(bot.user.name) + "มาเเล้วคร๊าบ ว่าไง " + str(message.author.name))
    elif message.content == 'พวกเราก็อบลินเถิดเทิง':
        await message.channel.send("""
ถ้าเธอยอมรับขยับเข้าใกล้
ทั้งกายทั้งใจยกให้เธอหมด
เธอจะบี้เธอจะบดเธอจะกดเธอจะขี่
เอาเถอะคนดีให้บี้ให้บด
จะขยี้จะขย้ำจะขยำจะขยี้
เอาให้เต็มที่ขยี้ให้เลือดหยด
รักเธอคนเดียวไม่ได้เกี่ยวข้องใคร
แม้ลมหายใจให้เธอจนหมด
ภูเขาขวางหน้าหน้าผาขวางกั้น
กำแพงสิบชั้นพี่ก็ดันไปพบ
จะเป็นจะตายจะร้ายจะดี
จะลองดูซีอย่างนี้เรียกสด
ใครจะขวางใครจะกั้นพี่จะฟันพี่จะฝ่า
พี่จะแหวกพสุธาเพื่อจะมาแหกกด""")
    await bot.process_commands(message)
    
bot.run('OTc5MDg5ODY3Nzg1MDExMjAw.GQno5N.wihdcwuguawgNV5GL-IsH0j4_lZyCrDSKLrpWI')