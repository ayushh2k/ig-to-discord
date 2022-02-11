import os
from discord.ext import tasks, commands
from instagramconnector import get_instagram_html,webhook,get_last_publication_url
import json


class MonitorInstagram(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.startMonitor.start()

    def cog_unload(self):
        self.startMonitor.cancel()


    @tasks.loop(seconds=float(os.environ.get('TIME_INTERVAL') or 600))
    async def startMonitor(self):
        print('Querying Instagram for new data')
        for user in self.bot.user_data:
          print(user)
          query_instagram(self, user)

def query_instagram(self, user):
  try:
      INSTAGRAM_USERNAME = user
      html = get_instagram_html(INSTAGRAM_USERNAME)
      if(self.bot.user_data[user] == get_last_publication_url(html)):
          print("No new image to post in discord.")
      else:
          self.bot.user_data[user] = get_last_publication_url(html)
          with open('users.json', 'r') as f:
                    ps = json.load(f)
          ps[f'{user}'] = get_last_publication_url(html)
          with open('users.json', 'w') as f:
                        json.dump(ps,f,indent=4)
          print("New image to post in discord.")
          webhook(os.environ.get("WEBHOOK_URL"),
                  get_instagram_html(INSTAGRAM_USERNAME))
  except Exception as e:
      print(e)

def setup(bot):
    bot.add_cog(MonitorInstagram(bot))

