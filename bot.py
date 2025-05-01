# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | @NT_BOTS_SUPPORT | LISA-KOREA/UPLOADER-BOT-V4
# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/UPLOADER-BOT-V4

import os
from plugins.config import Config
from pyrogram import Client as PyroClient

if __name__ == "__main__":

    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)

    plugins = dict(root="plugins")

    # Set up the proxy configuration with your credentials
    proxy = None
    if Config.HTTP_PROXY:
        proxy_host, proxy_port = Config.HTTP_PROXY.split(":")
        proxy = {
            "scheme": "http",  # Use "socks5" if hide.me provides SOCKS proxy
            "hostname": proxy_host,
            "port": int(proxy_port),
            "username": "marwin04",  # Your hide.me username
            "password": "Marwin2002@"  # Your hide.me password
        }

    # Create the PyroClient (your bot client)
    app = PyroClient(
        name=Config.SESSION_NAME,
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=300,
        plugins=plugins,
        proxy=proxy  # Use the proxy configuration here
    )

    print("🎊 I AM ALIVE 🎊  • Support @NT_BOTS_SUPPORT")

    app.run()
    
