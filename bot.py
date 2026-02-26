import discord
import json
import os
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

load_dotenv()

# ========== FLASK WEB SERVER (for UptimeRobot) ==========

app = Flask('')

@app.route('/')
def home():
    return "🤖 Bot #0085 is alive and running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ========== DISCORD BOT SETUP ==========

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)

# Load cards
with open('cards.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

# Channel ID
ALLOWED_CARD_CHANNEL = 1472210421930004574  # #td-cards

# ========== COLOR MAPPINGS ==========

I_COLORS = {
    # Line 2 (0x006098)
    **dict.fromkeys(range(1, 13), 0x006098),      # I-1~12
    
    # Line 4 (0x008E9C)
    **dict.fromkeys(range(13, 20), 0x008E9C),     # I-13~19
    
    # Line 5 (0xA6217F)
    **dict.fromkeys(range(20, 26), 0xA6217F),     # I-20~25
    
    # Line 6 (0xD29700)
    **dict.fromkeys(range(26, 29), 0xD29700),     # I-26~28
    
    # Line 7 (0xF6C582)
    29: 0xF6C582, 30: 0xF6C582,                    # I-29~30
    
    # Line 8 (0x009B6B)
    31: 0x009B6B, 32: 0x009B6B,                    # I-31~32
    
    # Line 9 (0x8FC31F)
    33: 0x8FC31F, 34: 0x8FC31F,                    # I-33~34
    
    # Line 10 (0x009BC0)
    35: 0x009BC0, 36: 0x009BC0,                    # I-35~36
    
    # Line 11 (0xED796B)
    37: 0xED796B,                                   # I-37
    
    # Line 13 (0xF9E700)
    38: 0xF9E700,                                   # I-38
    
    # Line 14 (0xD5A7A1)
    39: 0xD5A7A1,                                   # I-39
    
    # Line 15 (0x5B2C68)
    40: 0x5B2C68,                                   # I-40 💜
    
    # Line 16 (0x76A32E)
    41: 0x76A32E,                                   # I-41
    
    # Line 17 (0x00A9A9)
    42: 0x00A9A9,                                   # I-42
    
    # Line 19 (0xD6ABC1)
    43: 0xD6ABC1,                                   # I-43
    
    # Pink (0xE25A50)
    44: 0xE25A50, 45: 0xE25A50,                    # I-44~45
    
    # Teal (0x007EAC)
    46: 0x007EAC, 47: 0x007EAC,                    # I-46~47
    
    # Black (0x000000)
    48: 0x000000,                                   # I-48
    
    # Line 3 (0xCE093D)
    49: 0xCE093D, 50: 0xCE093D, 51: 0xCE093D, 52: 0xCE093D,
    53: 0xCE093D, 54: 0xCE093D, 55: 0xCE093D, 56: 0xCE093D,
    
    # Line 12 (0xBD6F16)
    57: 0xBD6F16,                                   # I-57
    
    # Line 18 (0x776CB1)
    69: 0x776CB1,                                   # I-69
}

II_COLORS = {
    # Line 2 (0x006098)
    58: 0x006098, 59: 0x006098,                    # II-58~59
    
    # Line 3 (0xCE093D)
    60: 0xCE093D, 61: 0xCE093D,                    # II-60~61
    
    # Line 4 (0x008E9C)
    62: 0x008E9C,                                   # II-62
    
    # Line 6 (0xD29700)
    63: 0xD29700, 64: 0xD29700, 65: 0xD29700,      # II-63~65
    
    # Line 8 (0x009B6B)
    66: 0x009B6B,                                   # II-66
    
    # Line 11 (0xED796B)
    67: 0xED796B,                                   # II-67
    
    # Line 12 (0xBD6F16)
    68: 0xBD6F16,                                   # II-68
    
    # Line 24 (0xE40077)
    70: 0xE40077,                                   # II-70
    
    # Line 7 (0xF6C582)
    71: 0xF6C582,                                   # II-71
}

S_COLORS = {
    'S-1': 0x6D9A45,
    'S-2': 0xB9271C, 'S-3': 0xB9271C,
    'S-4': 0x4F707B, 'S-5': 0x4F707B,
    'S-6': 0x000000, 'S-7': 0x000000,
    'S-8': 0x9df771, 'S-9': 0x9df771, 'S-10': 0x9df771,
    'S-11': 0x000000, 'S-12': 0x000000,
    'S-13': 0xE2A23F,
}

X_COLOR = 0xf1c40f

def get_card_color(card_type, number):
    card_type = card_type.upper()
    card_id = f"{card_type}-{number}"
    
    if card_type == 'I' and number in I_COLORS:
        return I_COLORS[number]
    elif card_type == 'II' and number in II_COLORS:
        return II_COLORS[number]
    elif card_id in S_COLORS:
        return S_COLORS[card_id]
    elif card_type == 'X':
        return X_COLOR
    return 0x95a5a6  # Default gray

# ========== BOT READY MESSAGE ==========

@bot.event
async def on_ready():
    print(f"✅ Bot #0085 is online!!!")
    print(f"📚 Loaded {len(cards)} cards")
    print(f"🎨 Color mappings: I={len(I_COLORS)}, II={len(II_COLORS)}, S={len(S_COLORS)}")
    await bot.change_presence(activity=discord.Game(name="/card I 1"))

# ========== ERROR HANDLER ==========

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(description="❌ Command not found. Try `/help`", color=0xFF0000)
        await ctx.respond(embed=embed, ephemeral=True)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="❌ Missing argument. Check `/help`", color=0xFF0000)
        await ctx.respond(embed=embed, ephemeral=True)
    else:
        embed = discord.Embed(description=f"❌ Error: {str(error)}", color=0xFF0000)
        await ctx.respond(embed=embed, ephemeral=True)
        print(f"Error: {error}")

# ========== CHANNEL CHECK ==========

def is_allowed_card_channel(ctx):
    return ctx.channel.id == ALLOWED_CARD_CHANNEL

# ========== COMMANDS ==========

@bot.slash_command(name="card", description="Show a TD card")
async def card(ctx, card_type: str, number: int):
    if not is_allowed_card_channel(ctx):
        embed = discord.Embed(description="❌ Use #td-cards for card commands", color=0xFF0000)
        await ctx.respond(embed=embed, ephemeral=True)
        return
    
    card_id = f"{card_type.upper()}-{number}"
    
    if card_id not in cards:
        await ctx.respond(f"❌ Card `{card_id}` not found!", ephemeral=True)
        return
    
    color = get_card_color(card_type, number)
    embed = discord.Embed(description=cards[card_id], color=color)
    await ctx.respond(embed=embed, ephemeral=True)

@bot.slash_command(name="rules", description="TD Card Game rules")
async def rules(ctx):
    if not is_allowed_card_channel(ctx):
        embed = discord.Embed(description="❌ Use #td-cards for rules", color=0xFF0000)
        await ctx.respond(embed=embed, ephemeral=True)
        return
    
    embed = discord.Embed(title="📜 TD Card Game Rules", color=0x3498db)
    embed.add_field(name="🎨 Same Color", value="Left ÷ Right matches", inline=False)
    embed.add_field(name="🔢 Same Small Number", value="Right number matches", inline=False)
    embed.add_field(name="🔢 Same Big Number", value="Left number matches", inline=False)
    embed.add_field(name="📝 Can't play?", value="Draw one card", inline=True)
    embed.add_field(name="🏆 Win", value="Play all your cards", inline=True)
    await ctx.respond(embed=embed, ephemeral=True)

@bot.slash_command(name="about", description="About TD Card Game")
async def about(ctx):
    if not is_allowed_card_channel(ctx):
        embed = discord.Embed(description="❌ Use #td-cards for about", color=0xFF0000)
        await ctx.respond(embed=embed, ephemeral=True)
        return
    
    embed = discord.Embed(title="ℹ️ About TD Card Game", color=0x2ecc71)
    embed.add_field(name="📅 Version", value="6.1", inline=True)
    embed.add_field(name="🎴 Total Cards", value="85", inline=True)
    await ctx.respond(embed=embed, ephemeral=True)

@bot.slash_command(name="help", description="Show all commands")
async def help_command(ctx):
    if not is_allowed_card_channel(ctx):
        embed = discord.Embed(description="❌ Use #td-cards for help", color=0xFF0000)
        await ctx.respond(embed=embed, ephemeral=True)
        return
    
    embed = discord.Embed(
        title="🤖 TD Bot Commands",
        description="Here's everything I can do:",
        color=0x6D9A45
    )
    embed.add_field(
        name="🎴 Card Commands",
        value="`/card [type] [number]` - Show any card\n`/rules` - Game rules\n`/about` - Game info",
        inline=False
    )
    embed.set_footer(text="TD Bot — Card commands only • All responses ephemeral")
    
    await ctx.respond(embed=embed, ephemeral=True)

# ========== RUN ==========

if __name__ == "__main__":
    # Start the web server (for UptimeRobot)
    keep_alive()
    
    # Start the bot
    token = os.getenv('DISCORD_TOKEN_TD')
    if not token:
        print("❌ ERROR: DISCORD_TOKEN_TD not found in environment variables")
        print("Add it in Replit Secrets (Tools → Secrets)")
    else:
        print("🚀 Starting Bot #0085 with web server...")
        bot.run(token)
