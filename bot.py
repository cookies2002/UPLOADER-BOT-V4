# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | @NT_BOTS_SUPPORT | LISA-KOREA/UPLOADER-BOT-V4
# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/UPLOADER-BOT-V4

import os
from plugins.config import Config
from pyrogram import Client

if __name__ == "__main__":

    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)

    plugins = dict(root="plugins")

    Client = Client(
        session_name=Config.SESSION_NAME,
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=300,
        plugins=plugins,
        proxy=dict(
            hostname=Config.HTTP_PROXY.split("//")[-1].split(":")[0],
            port=int(Config.HTTP_PROXY.split(":")[-1])
        ) if Config.HTTP_PROXY else None
    )

    print("🎊 I AM ALIVE 🎊  • Support @NT_BOTS_SUPPORT")

    Client.run()
    
