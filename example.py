import discord
from discord.ext import commands
import shii


class Bot(commands.Bot):
  def __init__(self, *args, **kwargs):
   super().__init__(command_prefix=['!'], sync_commands=True, intents=discord.Intents.all(), case_insensitive=True)

  async def on_ready(self):
    print(f"Logged in as {self.user}")
    await self.tree.sync()

    '''기본 모듈 설정(지정되지 않는 경우 기본값으로 리턴'''
    shii.no_study_return_text('?')
    shii.study_return_text('네! 알았어요!')

intents = discord.Intents.all()
bot = Bot(intents=intents)


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if message.content.startswith('example '):
    message1 = message.content[4:]
    re = shii.study_say(message1)
    await message.channel.send(re)


'''키드 학습 커멘드'''
@bot.command()
async def study_keyword(ctx, keyword: str, description: str):
  user = ctx.author.name
  re = shii.study(keyword, description, user)
  await ctx.send(re)


'''키워드 삭제 커멘드'''
@bot.command()
async def delete_keyword(ctx, keyword: str):
  re = shii.del_study(keyword)
  await ctx.send(re)


bot.run('example')
