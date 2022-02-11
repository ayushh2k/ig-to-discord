# ig-to-discord
This  bot will take Instagram posts and repost them into a discord channel using discord webhooks.
Modified from [Fernando](https://github.com/fernandod1/Instagram-to-discord).
# Requirements:
* Python3
* requests
* re
* discord.py
# Deployment:

Set environment variables in .env
* TIME_INTERVAL is in seconds.
* WEBHOOK_URL can be found on discord server->channel settings-> integrations.
* TOKEN can be found on discord developer portal.

# Usage:
* Use `,add (ig username(s))` to add accounts or you can just add them to `users.json` in this format 
```
{
    "username":"",
    "username2":""
} 
```
* Use `,remove (ig username(s))` to remove accounts. 
* Use `,list` to show the stored accounts list.

# Screenshots:
![image](https://cdn.discordapp.com/attachments/923207353896153124/941650635722457098/unknown.png)
