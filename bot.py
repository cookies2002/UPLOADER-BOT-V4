# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | @NT_BOTS_SUPPORT | LISA-KOREA/UPLOADER-BOT-V4
# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/UPLOADER-BOT-V4

import os
from plugins.config import Config
from pyrogram import Client as PyroClient  # avoid name conflict

if __name__ == "__main__":

    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)

    plugins = dict(root="plugins")

    proxy = None
    if Config.HTTP_PROXY:
        proxy_host, proxy_port = Config.HTTP_PROXY.split(":")
        proxy = {
            "scheme": "http",  # or "socks5" if your proxy is SOCKS
            "hostname": proxy_host,
            "port": int(proxy_port)
        }

    app = PyroClient(
        name=Config.SESSION_NAME,
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=300,
        plugins=plugins,
        proxy=proxy
    )

    print("🎊 I AM ALIVE 🎊  • Support @NT_BOTS_SUPPORT")

    app.run()  # This line should be properly indented
