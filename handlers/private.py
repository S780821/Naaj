from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**ʜᴇʏ, I'm {bn} 🎵 
        Ꮖ ᎪᎷ ᎪᎠᏙᎪΝᏟᎬᎠ ᎷႮՏᏆᏟ ᏢᏞᎪᎽᎬᎡ ᏴϴͲ ᎡႮΝ ϴΝ ϴᏔΝ ՏᎬᎡᏙᎬᎡ! ᎷϴᎡᎬ ҒᎪՏͲᎬᎡ , Νϴ ᏞᏀ , ᎪᏞᏞ ҒᎡᎬᎬ ᎪΝᎠ ᏆΝᏟᏞႮᎠᎬᎠ ᎷϴᎡᎬ ᏟϴᎷᎷᎪΝᎠՏ ᏆΝ ᏆͲ.**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 𝙰𝚍𝚍 𝙼𝚎 𝚝𝚘 𝙶𝚛𝚘𝚞𝚙 ", url="https://t.me/CrystalMusicRobot?startgroup=new")
                  ],[
                    InlineKeyboardButton(
                        "💬 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 ", url="https://t.me/crystalbots"
                    ),
                    InlineKeyboardButton(
                        "👥 𝙶𝚛𝚘𝚞𝚙", url="https://t.me/Chatting_officials"
                    )
                ],[ 
                    InlineKeyboardButton(
                        " Term & Condition ", url="https://t.me/crystalbots/14"
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
                        "Channel ", url="https://t.me/crystalbots")
                ]
            ]
        )
   )


