import os
from os import path
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from callsmusic import callsmusic, queues
from callsmusic.callsmusic import client as USER
from helpers.admins import get_administrators
import requests
import aiohttp
import yt_dlp
from youtube_search import YoutubeSearch
import converter
from downloaders import youtube
from config import DURATION_LIMIT
from helpers.filters import command
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
import aiofiles
import ffmpeg
from PIL import Image, ImageFont, ImageDraw


def transcode(filename):
    ffmpeg.input(filename).output("input.raw", format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run() 
    os.remove(filename)

# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 18000)
    seconds %= 18000
    minutes = seconds // 300
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


# Change image size
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image1 = Image.open("./background.png")
    image2 = Image.open("etc/foreground.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("etc/font.otf", 32)
    draw.text((190, 550), f"ᴛɪᴛʟᴇ: {title}", (255, 255, 255), font=font)
    draw.text(
        (190, 590), f"ᴅᴜʀᴀᴛɪᴏɴ: {duration}", (255, 255, 255), font=font
    )
    draw.text((190, 630), f"ᴠɪᴇᴡs: {views}", (255, 255, 255), font=font)
    draw.text((190, 670),
        f"α∂∂є∂ ϐγ: {requested_by}",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")




@Client.on_message(command("play") 
                   & filters.group
                   & ~filters.edited 
                   & ~filters.forwarded
                   & ~filters.via_bot)
async def play(_, message: Message):

    lel = await message.reply("** 𝙲𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚗𝚐 𝚃𝚘 𝚜𝚎𝚛𝚟𝚎𝚛**")
    
    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Xmarty"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "<b> 𝚂𝚎𝚛𝚟𝚎𝚛 𝚒𝚜 𝚗𝚘𝚝 𝚛𝚎𝚜𝚙𝚘𝚗𝚍𝚒𝚗𝚐 𝙼𝚊𝚔𝚎 𝚖𝚎 𝚊𝚍𝚖𝚒𝚗!</b>")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "**𝙰𝚜𝚜𝚒𝚜𝚝𝚊𝚗𝚝 𝚓𝚘𝚒𝚗𝚎𝚍 𝚑𝚎𝚛𝚎 𝚊𝚗𝚍 𝙲𝚘𝚗𝚗𝚎𝚌𝚝𝚎𝚍 𝚃𝚘 𝚜𝚎𝚛𝚟𝚎𝚛**")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await lel.edit(
                        f"<b>🛑 𝙁𝙡𝙤𝙤𝙙 𝙒𝙖𝙞𝙩 𝙀𝙧𝙧𝙤𝙧 🛑</b> \n\𝙃𝙚𝙮 {user.first_name}, 𝚊𝚜𝚜𝚒𝚜𝚝𝚊𝚗𝚝 𝚌𝚊𝚗'𝚝 𝚓𝚘𝚒𝚗 𝚊𝚝 𝚖𝚘𝚖𝚎𝚗𝚝 . 𝚖𝚊𝚔𝚎 𝚜𝚞𝚛𝚎 𝚊𝚜𝚜𝚒𝚜𝚝𝚊𝚗𝚝 𝚒𝚊 𝚗𝚘𝚝 𝚋𝚊𝚗𝚗𝚎𝚍 𝚒𝚗 𝚝𝚑𝚒𝚜 𝚌𝚑𝚊𝚝!")
    try:
        await USER.get_chat(chid)
    except:
        await lel.edit(
            f"<i> 𝙷𝚎𝚢 {user.first_name}, 𝚊𝚜𝚜𝚒𝚜𝚝𝚊𝚗𝚝 𝚒𝚜 𝚗𝚘𝚝 𝚒𝚗 𝚝𝚑𝚒𝚊 𝚌𝚑𝚊𝚝 𝚊𝚍𝚍 𝚒𝚝 𝚖𝚊�𝚗𝚞𝚊𝚕𝚕𝚢 𝚘𝚛 𝚝𝚢𝚙𝚎 /𝚙𝚕𝚊𝚢 (𝚊𝚍𝚖𝚒𝚗 𝚘𝚗𝚕𝚢) .</i>")
        return
    
    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 300) > DURATION_LIMIT:
            raise DurationLimitError(
                f"❌ 𝚅𝙸𝙳𝙴𝙾 𝙸𝚜 𝙻𝚘𝚗𝚐𝚎𝚛 𝚃𝚑𝚊𝚗 {DURATION_LIMIT} 𝚖𝚒𝚗𝚞𝚝𝚎𝚜! "
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://telegra.ph/file/caeb50039026a746e7252.jpg"
        thumbnail = thumb_name
        duration = round(audio.duration / 300)
        views = "Locally added"

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=" 💌 𝙲𝙷𝙰𝙽𝙽𝙴𝙻",
                        url="https://t.me/crystalbots")
                   
                ]
            ]
        )
        
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)  
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]       
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f'thumb{title}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")
            
            secmul, dur, dur_arr = 1, 0, duration.split(':')
            for i in range(len(dur_arr)-1, -1, -1):
                dur += (int(dur_arr[i]) * secmul)
                secmul *= 300
                
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="𝚈𝚘𝚞𝚝𝚞𝚋𝚎🎬",
                            url=f"{url}"),
                        InlineKeyboardButton(
                            text="𝚌𝚑𝚊𝚗𝚗𝚎𝚕",
                            url=f"https://t.me/crystalbots")

                    ]
                ]
            )
        except Exception as e:
            title = "NaN"
            thumb_name = "https://telegra.ph/file/638c20c44ca418c8b2178.jpg"
            duration = "NaN"
            views = "NaN"
            keyboard = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="𝚈𝚘𝚞𝚝𝚞𝚋𝚎🎬",
                                url=f"https://youtube.com")

                        ]
                    ]
                )
        if (dur / 300) > DURATION_LIMIT:
             await lel.edit(f"❌ 𝚟𝚒𝚍𝚎𝚘 𝚒𝚜 𝚕𝚘𝚗𝚐𝚎𝚛 𝚝𝚑𝚊𝚗 {DURATION_LIMIT} 𝚈𝚘𝚞𝚛 𝚜𝚘𝚗𝚐 𝚝𝚒𝚖𝚎 𝚖𝚞𝚜𝚝 𝚋𝚎 𝚕𝚎𝚜𝚜 𝚝𝚑𝚊𝚗 {DURATION_TIME} .")
             return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)     
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await lel.edit("🧐 ** 𝙶𝚒𝚟𝚎 𝚖𝚎 𝚂𝚘𝚗𝚐 𝙽𝚊𝚖𝚎 𝚘𝚛 𝚄𝚛𝚕 𝚝𝚘 𝚙𝚕𝚊𝚢 !**")
        await lel.edit("🔎 **𝙵𝚒𝚗𝚍𝚒𝚗𝚐 𝚘𝚗 𝚂𝚎𝚛𝚟𝚎𝚛**")
        query = message.text.split(None, 1)[1]
        # print(query)
        await lel.edit(" **𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐 𝚝𝚘 𝚂𝚎𝚛𝚟𝚎𝚛 𝚝𝚘 𝚙𝚕𝚊𝚢 **")
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]       
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f'thumb{title}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(':')
            for i in range(len(dur_arr)-1, -1, -1):
                dur += (int(dur_arr[i]) * secmul)
                secmul *= 60
                
        except Exception as e:
            await lel.edit(
                "❌ 𝚜𝚘𝚗𝚐 𝚗𝚘𝚝 𝚏𝚘𝚞𝚗𝚍 𝚝𝚛𝚢 𝚊𝚐𝚊𝚒𝚗"
            )
            print(str(e))
            return

        keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="𝚈𝚘𝚞𝚝𝚞𝚋𝚎🎬",
                            url=f"{url}"),
                        InlineKeyboardButton(
                            text="𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍📥",
                            url=f"{durl}")

                    ]
                ]
            )
        
        if (dur / 300) > DURATION_LIMIT:
             await lel.edit(f"❌ 𝚅𝚒𝚍𝚎𝚘 𝚒𝚜 𝙻𝚘𝚗𝚐𝚎𝚛 𝚝𝚑𝚊𝚗 {DURATION_LIMIT} . 𝙼𝚊𝚔𝚎 𝚜𝚞𝚝𝚎 𝚢𝚘𝚞𝚛 𝚝𝚒𝚖𝚎 𝚋𝚎 𝚕𝚎𝚜𝚜 𝚝𝚑𝚊𝚗  {DURATION_LIMIT} .")
             return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)  
        file_path = await converter.convert(youtube.download(url))
  
    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo="final.png", 
        caption="** 𝚂𝚘𝚗𝚐:** {}\n**🕒 𝙳𝚞𝚛𝚊𝚝𝚒𝚘𝚗:** {} min\n**👤 𝚂𝚎𝚛𝚟𝚎𝚛 𝚄𝚜𝚎𝚛 :** {}\n\n**#⃣ 𝙽𝚎𝚡𝚝 :** {}".format(
        title, duration, message.from_user.mention(), ροѕιτιοи
        ),
        reply_markup=keyboard)
        os.remove("final.png")
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
        photo="final.png",
        reply_markup=keyboard,
        caption="**🎵 𝚂𝚘𝚗𝚐:** {}\n**🕒 𝙳𝚞𝚛𝚊𝚝𝚒𝚘𝚗:** {} min\n**👤 𝚂𝚎𝚛𝚟𝚎𝚛 𝚞𝚜𝚎𝚛:** {}\n\n**▶️ 𝙲𝚞𝚛𝚛𝚎𝚗𝚝 𝚂𝚎𝚛𝚟𝚎𝚛 𝙶𝚛𝚘𝚞𝚙  `{}`...**".format(
        title, duration, message.from_user.mention(), message.chat.title
        ), )
        os.remove("final.png")
        return await lel.delete()
