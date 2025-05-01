import os
from plugins.config import Config
from pyrogram import Client

if __name__ == "__main__":

    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)

    plugins = dict(root="plugins")

    app = Client(
        session_name=Config.SESSION_STR,  # Use your user session
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=300,
        plugins=plugins
    )

    print("🎊 USER BOT IS ALIVE 🎊  • Support @NT_BOTS_SUPPORT")
    app.run()
    
