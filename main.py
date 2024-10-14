import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, BotCommand

from src.routers.elixir_sheet_router import elixir_sheet_router
from src.routers.spots_router import spots_router
from src.routers.damage_router import damage_router

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

dp.include_router(elixir_sheet_router)
dp.include_router(spots_router)
dp.include_router(damage_router)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())












# @bot.command()
# @commands.is_owner()
# async def server_info(ctx):
#     guilds = ""
#     for guild in bot.guilds:
#         guilds += f"{guild.name}\n"
#     await ctx.reply(guilds, mention_author=False)
#
#
# @bot.command()
# @commands.guild_only()
# @commands.is_owner()
# async def sync(
#   ctx: Context, guilds: Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
#     if not guilds:
#         if spec == "~":
#             synced = await ctx.bot.tree.sync(guild=ctx.guild)
#         elif spec == "*":
#             ctx.bot.tree.copy_global_to(guild=ctx.guild)
#             synced = await ctx.bot.tree.sync(guild=ctx.guild)
#         elif spec == "^":
#             ctx.bot.tree.clear_commands(guild=ctx.guild)
#             await ctx.bot.tree.sync(guild=ctx.guild)
#             synced = []
#         else:
#             synced = await ctx.bot.tree.sync()
#
#         await ctx.send(
#             f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
#         )
#         return
#
#     ret = 0
#     for guild in guilds:
#         try:
#             await ctx.bot.tree.sync(guild=guild)
#         except discord.HTTPException:
#             pass
#         else:
#             ret += 1
#
#     await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")
#
#
# @bot.event
# async def on_ready():
#     print(f'{bot.user} has awoken')
#     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="you crying"))
#     print("Streaming Amogus")
#
#
# async def load_extensions():
#     for filename in os.listdir("./chestii"):
#         if filename.endswith(".py"):
#             await bot.load_extension(f"chestii.{filename[:-3]}")
#             print(f"{filename[:-3].title()} loaded!")
#
#
# async def amogus():
#     await load_extensions()
#     bot.tree.copy_global_to(guild=discord.Object(id=993818190008287283))
#     await bot.start("ඞ")
#
# asyncio.run(amogus())
#
