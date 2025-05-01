import os
from plugins.config import Config
from pyrogram import Client

if __name__ == "__main__":
    # Ensure the download location exists
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)

    # Define the plugins location
    plugins = dict(root="plugins")

    # Ensure the session directory exists
    session_dir = "/home/ubuntu/UPLOADER-BOT-V4/sessions"
    if not os.path.exists(session_dir):
        os.makedirs(session_dir)

    # Initialize the pyrogram Client with a full path for session storage
    session_name = "userbot_session"  # Short session name
    app = Client(
        session_name,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workdir=session_dir  # Use the full path to your session folder
    )

    print("🎊 USERBOT ONLINE (4GB upload supported) 🎊  • Support @NT_BOTS_SUPPORT")
    app.run()
    
