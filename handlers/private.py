from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**HELLO, I'm {bn} 🎵

I CAN PLAY MUSIC IN YOUR GROUP'S VC. OWNER OF THIS BOT [𝐐𝐔𝐄𝐄𝐍](https://t.me/forever_angel_0).

LO AB PADH LIYA HO TO GROUP M CHLE ?😁.MERE KO ADD KRO OR GAANE SUNO. !**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎸𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞🎸", url="https://github.com/mehtaarvi/GroupMusicPlayerBot")
                  
                    InlineKeyboardButton(
                        "🎀𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥🎀", url="https://t.me/ABOUT_ARVI"
                    ),]
                   [ InlineKeyboardButton(
                        "🤿𝐂𝐡𝐚𝐥𝐨 𝐌𝐞𝐫𝐞 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞🪔.", url="https://t.me/WORLD_WIDE_CHAT"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕𝐀𝐝𝐝 𝐊𝐚𝐫𝐥𝐨 𝐌𝐞𝐫𝐞𝐤𝐨 𝐆𝐫𝐨𝐮𝐩 𝐦𝐞➕", url="https://t.me/arvi_music_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎀𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥🎀", url="https://t.me/ABOUT_ARVI")
                ]
            ]
        )
   )


