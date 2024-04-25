import discord
from discord.ext import commands
import shii


class Bot(commands.Bot):
  def __init__(self, *args, **kwargs):
   super().__init__(command_prefix=['!'], sync_commands=True, intents=discord.Intents.all(), case_insensitive=True)

  async def on_ready(self):
    print(f"Logged in as {self.user}")
    await self.tree.sync()
    shii.no_study_return_text('?')
    shii.study_return_text('네! 알았어요!')

intents = discord.Intents.all()
bot = Bot(intents=intents)


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if message.content.startswith('exa '):
    message1 = message.content[4:]
    re = shii.study_say(message1)
    await message.channel.send(re)


@bot.command()
async def test(ctx, keyword: str, description: str):
  user = ctx.author.name
  re = shii.study(keyword, description, user)
  await ctx.send(re)


@bot.command()
async def test2(ctx, keyword: str):
  re = shii.del_study(keyword)
  await ctx.send(re)


bot.run('example')
