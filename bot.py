import os
from plugins.config import Config
from pyrogram import Client

if __name__ == "__main__":
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)

    plugins = dict(root="plugins")

    app = Client(
        Config.SESSION_STR,  # <-- This is your session string
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )

    print("🎊 USERBOT ONLINE (4GB upload supported) 🎊  • Support @NT_BOTS_SUPPORT")
    app.run()
    
