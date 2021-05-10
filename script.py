class script(object):

    START_TEXT = """<b>Hai ,
    
I'm A simple Zee5 link downloader bot With Permanent Thumbnail Support💯.

Please send me any Zee5 link, I can upload it to telegram as File & Video.

Click /help for more details....</b>"""


    HELP_USER = """<b>Hai, Follow these steps..
 
1. Send Custom Thumbnail (Optional)

2. Send your zee5 url and select desired option.

3. Enjoy..!!

NOTE: Download may take some time! So please wait for it to complete!</b>"""


    ABOUT_TEXT = """<b>My Name : <a href='https://t.me/Zee5_dl_robot'>★Zᴇᴇ5 Dᴏᴡɴʟᴏᴀᴅᴇʀ Bᴏᴛ By pro_morningstar​★</a></b>\n
<b>Channel : <a href='https://t.me/movies_Unloaded'>• Movies Unloaded •</a></b>\n
<b>Version : <a href='https://t.me/Movies_Unloaded'>0.1 beta</a></b>\n
<b>Source : <a href='https://github.com/ak3052005'>Click Here</a></b>\n
<b>Server : <a href='https://heroku.com'>Heroku</a></b>\n
<b>Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>\n
<b>Language : <a href='https://www.python.org'>Python 3.9.4</a></b>\n
<b>Developer : <a href='https://t.me/pro_morningstar'>✯°• [🇮🇳] 👁️⃤PAPA#TheStarkArmy [¢∆] 𒁂ᐯᗷ𒁂 •°✯</a></b>\n
<b>Powered By : <a href='https://t.me/movies_unloaded'>• movies Unloaded •</a></b>\n"""



    FORMAT_SELECTION = """<b>Choose appropriate option</b> <a href='{}'>⬇️</a>

🎞  - Stream format
📁  - File format

<b>NOTE : Taking high resolutions may result in files above 2GB and hence cannot Upload to TG. So better select a medium resolution.</b> 😇
"""    
    
    UPGRADE_TEXT = "<b>PING at @pro_morningstar</b>"
    
    DOWNLOAD_START = "<b>Trying to download to my server. This may take a while 😴</b>"
    
    UPLOAD_START = "<b>Uploading Now ⬆️</b>"
    
    RCHD_TG_API_LIMIT = "<b>Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations.</b>"

    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "**<b>Thank you for Using Meh! Share Our Service\ @pro_morningstar ! ❤️**</b>"
    
    SAVED_CUSTOM_THUMB_NAIL = "<b>✅Custom thumbnail Saved.\nThis thumbnail will be Permanent for all future uploads\n\nDo /delthumb to clear your thumbnail!</b>"
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "</b>✅ Custom Thumbnail cleared succesfully.</b>"
    
    SHOW_THUMB = "<b>@ML_BotUpdates\n\nUse /delthumb to clear this thumbnail.</b>"
    
    NO_THUMB = "<b>SED😕 No saved thumbnails Found!!</b>"
    
    CUSTOM_CAPTION_UL_FILE = "<b>{newname}\n\n©️ @movies_unloaded</b>"
    
    TIMEOUT = "<b><i>Sorry for the delay. It'll help reduce the flood wait</i> 😇\n\nWait for {} sec and try again.</b>"
    
