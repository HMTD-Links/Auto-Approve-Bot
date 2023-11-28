from configs import rkn1
from pyrogram import Client, filters, enums
from pyrogram.errors import UserNotParticipant
from RknDeveloper.untils.database import add_user
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@Client.on_callback_query(filters.regex("rkn_developer"))
async def chk(bot, cb : CallbackQuery):
    try:
        await bot.get_chat_member(rkn1.UPDATECHANNEL_ID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("─シ｡Aʙᴏᴜᴛ｡シ─", callback_data = "about")
                    ],[
                InlineKeyboardButton("𖣘 Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url="https://t.me/Star_Bots_Tamil"),
                InlineKeyboardButton("⚘ Sᴜᴘᴘᴏʀᴛ ⚘", url="https://t.me/Star_Bots_Tamil_Support")
                ],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ࿇", url="https://t.me/Auto_Approve_Star_Bot?startchannel=Bots4Sale&admin=invite_users+manage_chat+change_info")],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ࿇", url="https://t.me/Auto_Approve_Star_Bot?startgroup=Bots4Sale&admin=invite_users+manage_chat+change_info")
                
            ]])            
            add_user(cb.from_user.id)
            await cb.message.edit("**🦊 Hᴇʟʟᴏ {}!\n\nI'ᴍ Aɴ Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇ [Auto Approve Star Bots]({}) Bᴏᴛ.\nI Cᴀɴ Aᴘᴘʀᴏᴠᴇ Usᴇʀs Iɴ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs.Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Aɴᴅ Gʀᴏᴜᴘ ᴀɴᴅ Pʀᴏᴍᴏᴛᴇ Mᴇ Tᴏ Aᴅᴍɪɴ Wɪᴛʜ Aᴅᴅ Mᴇᴍʙᴇʀs Pᴇʀᴍɪssɪᴏɴ.\n\n__Pᴏᴡᴇʀᴅ Bʏ : @Star_Bots_Tamil__**".format(cb.from_user.mention, "https://t.me/Auto_Approve_Star_Bot"), reply_markup=keyboard, disable_web_page_preview=True)
            
        print(cb.from_user.first_name +" Is started Your Bot!")
    except UserNotParticipant:
        await cb.answer(f"Hey, {cb.from_user.first_name}\nI Lɪᴋᴇ Yᴏᴜʀ Sᴍᴀʀᴛɴᴇss, Bᴜᴛ Dᴏɴ'ᴛ Bᴇ Oᴠᴇʀsᴍᴀʀᴛ! 🤓 \nJᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Fɪʀsᴛ 🥇‌‌", show_alert=True)

#🔥 Please Don't Remove Credit 💳 # ❣️ 
@Client.on_callback_query(filters.regex('about'))
async def about(bot,update):
	await update.message.edit_text(
	    #⚠️ don't change source code & source link ⚠️ #
	    text = """<b>» Mʏ Nᴀᴍᴇ: <a href='https://t.me/Auto_Approve_Star_Bot'>Auto Approve Star Bots</a>
‣ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/TG_Karthik'>Karthik</a>
‣ Lɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org'>Pʏʀᴏɢʀᴀᴍ</a>
‣ Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org'>Pʏᴛʜᴏɴ 3</a>
‣ Dᴀᴛᴀ Bᴀsᴇ : <a href='https://www.mongodb.com/'>Mᴏɴɢᴏ Dʙ</a>
‣ Bᴏᴛ Sᴇʀᴠᴇʀ : VPS
‣ Sᴏᴜʀᴄᴇ : Coming Soon..!
‣ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ3.8.5 [sᴛᴀʙʟᴇ]</b>""",
	    reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ ❣️", url="https://t.me/Star_Bots_Tamil")],[
               InlineKeyboardButton("→ Bᴀᴄᴋ", callback_data = "rkn_developer")
               ]]
            )
    )
