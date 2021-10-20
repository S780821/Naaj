from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**ʜᴇʏ, I'm {bn} 🎵

ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ'ꜱ ᴠᴏɪᴄᴇ ᴄᴀʟʟ. ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [𝙸𝚝𝚜 𝚖𝚞𝚜𝚒𝚌](https://t.me/ShubhamMusics).

ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʟᴀʏ ᴍᴜꜱɪᴄ ꜰʀᴇᴇʟʏ!  \n  𝚁𝚞𝚗 𝚘𝚗 𝚘𝚠𝚗 𝚟𝚙𝚜 𝚜𝚎𝚛𝚟𝚎𝚛 𝚝𝚑𝚎 𝚏𝚊𝚜𝚝𝚎𝚜𝚝 𝚜𝚎𝚛𝚟𝚎𝚛!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 𝙰𝚍𝚍 𝙼𝚎 𝚝𝚘 𝙶𝚛𝚘𝚞𝚙 ", url="https://t.me/SwipMusic3_bot?startgroup=new")
                  ],[
                    InlineKeyboardButton(
                        "💬 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 ", url="https://t.me/ShubhamMusics"
                    ),
                    InlineKeyboardButton(
                        "👥 𝙶𝚛𝚘𝚞𝚙", url="https://t.me/Chatting_officials"
                    )
                ],[ 
                    InlineKeyboardButton(
                        " Term & Condition ", url="https://t.me/ShubhamMusics/63"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝙷𝚎𝚕𝚕𝚘 𝚒 𝚊𝚖 𝚛𝚎𝚊𝚍𝚢!  𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚎𝚍 𝚝𝚘 𝚜𝚎𝚛𝚟𝚎𝚛**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝚂𝚘𝚞𝚛𝚌𝚎 𝙲𝚘𝚍𝚎", url="https://github.com/shubham-king/HYPER-MUSIC")
                ]
            ]
        )
   )


