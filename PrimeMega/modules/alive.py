import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from PrimeMega.events import register
from PrimeMega import telethn as tbot


PHOTO = "https://telegra.ph/file/6a6521ee7dc443c28e351.jpg"

@register(pattern=("/alive"))
async def awake(event):
  PRIME = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), It's Zenzu Robot.** \n\n"
  PRIME += "π‘ **I'm Working Properly** \n\n"
  PRIME += f"π **My Master : [Lord](https://t.me/zenzuzu2)** \n\n"
  PRIME += f"β­ **Groups : [Zenzu Support](https://t.me/ZenzuRobotSupport)** \n\n"
  PRIME += f"β‘ **Channel : [My Channel](https://t.me/zenzu_shop)** \n\n"
  PRIME += f"π **Library Version :** `{telever}` \n\n"
  PRIME += f"π **Telethon Version :** `{tlhver}` \n\n"
  PRIME += f"π **Pyrogram Version :** `{pyrover}` \n\n"
  PRIME += "**Thanks For Adding Me Here β€οΈ**"
  BUTTON = [[Button.url("Help", "https://t.me/ZenzuRobot?start=help"), Button.url("Supportβ", "https://t.me/ZenzuRobotSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PRIME,  buttons=BUTTON)
