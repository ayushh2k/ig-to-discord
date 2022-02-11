from discord.ext import commands
import discord
from io import BytesIO
import json


class MonitorCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Add an instagram username
    @commands.command()
    @commands.is_owner()
    async def add(self, ctx, *args):
        for arg in args:
             self.bot.user_data[f'{arg}'] = ""
        await ctx.send(f'Added account(s): `{str(args)[1:-2]}`')
        await ctx.send(getDictionary(self))
        with open('users.json', 'r') as f:
                    ps = json.load(f)
        print(ps)
        for arg in args:
            ps[f'{arg}'] = ""
            with open('users.json', 'w') as f:
                        json.dump(ps,f,indent=4)

    # Remove an instagram username
    @commands.command()
    @commands.is_owner()
    async def remove(self, ctx, *args):
        for arg in args:
            try:
                self.bot.user_data.pop(arg)
                await ctx.send(f'Removed user `{str(arg)}`')
                with open('users.json', 'r') as f:
                     p = json.load(f)
                p.pop(arg)

                with open('users.json', 'w') as f:
                    json.dump(p, f, indent=4)
            except Exception as e:
                print(e)
                await ctx.send(f'Failed to remove user {arg}')
        await ctx.send(getDictionary(self))

    # Query List of instagram username
    @commands.command(aliases=['list'])
    async def accountslist(self, ctx):
        member_names = list(self.bot.user_data.keys())
        as_bytes = map(str.encode, member_names)
        content = b"\n".join(as_bytes)
        await ctx.send("Accounts List", file=discord.File(BytesIO(content), "accounts.txt"))


def getDictionary(self):
    l = list(self.bot.user_data.keys())
    return f'Current accounts list: `{str(l)[1:-1]}`'


def setup(bot):
    bot.add_cog(MonitorCommands(bot))
