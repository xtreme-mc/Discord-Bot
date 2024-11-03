import os
import discord
from discord.ext import commands
from discord import app_commands
from keep_alive import keep_alive
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.messages = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="clear", description="Clear a specified number of messages.")
@app_commands.describe(amount="The number of messages to delete.")
@app_commands.checks.has_permissions(manage_messages=True)
async def clear(interaction: discord.Interaction, amount: int):
    if amount < 1:
        await interaction.response.send_message("Please specify a positive number of messages to delete.", ephemeral=True)
        return

    deleted = await interaction.channel.purge(limit=amount)
    await interaction.response.send_message(f"Deleted {len(deleted)} messages.", ephemeral=True)

keep_alive()
bot.run(TOKEN)
