import os
from discord.ext import commands
import json

def main():
    bot = commands.Bot(command_prefix=',')
    with open('users.json', 'r') as f:
      ps = json.load(f)
    bot.user_data = {}
    if len(bot.user_data)==0:
      bot.user_data=ps
    print(bot.user_data)
    bot.load_extension("monitorcommands")
    bot.load_extension("monitorinstagram")
    @bot.command()
    @commands.is_owner()
    async def reload(ctx):
        try:
            bot.unload_extension("monitorcommands")
            bot.unload_extension("monitorinstagram")
            bot.load_extension("monitorinstagram")
            bot.load_extension("monitorcommands")
            await ctx.send(f"Reloaded the extensions")
        except Exception as e:
                print(e)
                await ctx.send(e)
    bot.run(os.getenv('TOKEN'))

print(os.environ.get('IG_USERNAME'))
if __name__ == "__main__":
    if os.environ.get('IG_USERNAME') != None and os.environ.get(
            'WEBHOOK_URL') != None:
        while True:
            main()
    else:
        print('There was an error!')
