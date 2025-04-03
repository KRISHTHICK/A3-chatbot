import discord
from discord.ext import commands

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!')

# Knowledge base for Ollama
ollama_knowledge_base = {
    "what is ollama": "Ollama is a platform for ...",
    "how to use ollama": "To use Ollama, you need to ...",
    "features of ollama": "Ollama offers features such as ...",
    # Add more Q&A pairs here
}

# Event listener for when the bot is ready
@bot.event
async def on_ready():
    print(f'Bot {bot.user} is online!')

# Command to handle user queries
@bot.command(name='ask')
async def ask(ctx, *, query: str):
    query = query.lower()
    if query in ollama_knowledge_base:
        await ctx.send(ollama_knowledge_base[query])
    else:
        await ctx.send("I'm sorry, I don't have an answer for that question about Ollama.")

# Run the bot using your token
bot.run('YOUR_DISCORD_BOT_TOKEN')
