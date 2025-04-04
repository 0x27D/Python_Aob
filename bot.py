import discord
from discord.ext import commands
import requests
import re
import html

TOKEN = 'MTM1MzYzNjYyNzMxODE4MTkwOA.GGhJp0.oXOZOtuK4Eisxg2nkd1gSpHUvUiCayLoFL_Qt4'
GUILD_ID = 1353585819029602315  # ID server (nếu bạn muốn hạn chế)
ALLOWED_CHANNELS = [1353585819029602315]  # ID các kênh bot được dùng

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot đã đăng nhập với tên: {bot.user}')

@bot.command()
async def fl(ctx, username: str = None):
    if ctx.channel.id not in ALLOWED_CHANNELS:
        await ctx.send("❌ Bạn không thể sử dụng bot ở kênh này.")
        return

    if username is None:
        await ctx.send("⚠️ Vui lòng nhập username TikTok. Ví dụ: `/fl bacgau`")
        return

    # Lấy thông tin TikTok
    try:
        response2 = requests.get(f"https://offvn.x10.mx/php/tiktok.php?id={username}", timeout=60, verify=False)
        data_api = response2.json()
    except:
        await ctx.send("❌ Lỗi khi lấy thông tin TikTok.")
        return

    if "data" not in data_api or "user_id" not in data_api["data"]:
        await ctx.send("❌ Không tìm thấy tài khoản người dùng.")
        return

    info = data_api["data"]

    # Gọi API tăng follow
    try:
        response1 = requests.get(f"https://nvp310107.x10.mx/fl.php?username={username}", timeout=60, verify=False)
        data1 = response1.json()

        if not data1.get("success", False):
            msg = data1.get("message", "")
            wait_time = re.search(r'(\d+)\s*giây', msg)
            if wait_time:
                await ctx.send(f"⚠️ Vui lòng chờ {wait_time.group(1)} giây trước khi thử lại!\nhttps://www.tiktok.com/@{username}")
                return
    except:
        await ctx.send("❌ Lỗi kết nối API tăng follow.")
        return

    # Gửi kết quả
    embed = discord.Embed(
        title=f"✅ Tăng Follow Thành Công cho @{username}",
        description=f"🔹 Nickname: `{html.escape(info.get('nickname', 'N/A'))}`\n"
                    f"🔹 UID: `{info.get('user_id', 'N/A')}`\n"
                    f"🔹 Follower ban đầu: `{info.get('followers', 'N/A')}`\n"
                    f"[🔗 Xem TikTok](https://www.tiktok.com/@{username})",
        color=0x00ff00
    )
    embed.set_footer(text=f"Yêu cầu bởi: {ctx.author}")
    await ctx.send(embed=embed)

bot.run(TOKEN)
