import os
from plugins.config import Config
from pyrogram import Client

if __name__ == "__main__":
    # Ensure the download location exists
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)

    # Define the plugins location
    plugins = dict(root="plugins")

    # Ensure the session string or session file name is shorter
    session_name = "userbot_session"  # You can change this to something short

    # Initialize the pyrogram Client
    app = Client(
        session_name,  # <-- Use a short session name
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workdir="sessions"  # Optional: Define a custom directory for session files
    )

    print("🎊 USERBOT ONLINE (4GB upload supported) 🎊  • Support @NT_BOTS_SUPPORT")
    app.run()
    
