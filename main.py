import os
import discord
from discord.ext import commands
from discord import app_commands
from server import keep_alive
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

    try:
        deleted = await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"Deleted {len(deleted)} messages.", ephemeral=True)
    except discord.Forbidden:
        await interaction.response.send_message("I don't have permission to delete messages.", ephemeral=True)
    except discord.HTTPException as e:
        await interaction.response.send_message(f"An error occurred: {e.text}", ephemeral=True)

@bot.tree.command(name="ping", description="Check the bot's latency.")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Ping: {bot.latency * 1000}ms", ephemeral=True)

keep_alive()

# Replace TOKEN with your bot token
try:
    bot.run(TOKEN)
except discord.HTTPException as e:
    print(f"An error occurred: {e.text}")
