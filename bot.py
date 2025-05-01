import os
from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.config import Config

# Ensure the download location exists
if not os.path.isdir(Config.DOWNLOAD_LOCATION):
    os.makedirs(Config.DOWNLOAD_LOCATION)

# Define the plugins location
plugins = dict(root="plugins")

# Ensure the session directory exists and is writable
session_dir = "/home/ubuntu/UPLOADER-BOT-V4/sessions"
if not os.path.exists(session_dir):
    os.makedirs(session_dir)

# Initialize the pyrogram Client with session and upload directory settings
app = Client(
    session_name="userbot_session",  # Short session name
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=plugins,
    workdir=session_dir  # Use the full path to your session folder
)

print("🎊 USERBOT ONLINE (4GB upload supported) 🎊  • Support @NT_BOTS_SUPPORT")

# Handle file uploads up to 4GB
@app.on_message(filters.document)
async def handle_document(client: Client, message: Message):
    try:
        # Get the file to upload
        file = message.document
        file_size = file.file_size

        # Check if the file size exceeds 4GB
        if file_size > 4 * 1024 * 1024 * 1024:
            await message.reply("⚠️ File size exceeds the 4GB limit!")
            return

        # Download the file (if it's not already in the DOWNLOAD_LOCATION)
        file_path = os.path.join(Config.DOWNLOAD_LOCATION, file.file_name)
        if not os.path.exists(file_path):
            downloaded_file = await message.download(file_path)
            print(f"Downloaded {file.file_name} to {file_path}")
        else:
            downloaded_file = file_path

        # Upload the file to another chat or channel
        # Example: Upload to your own Telegram channel
        chat_id = Config.CHAT_ID  # Set your target chat ID
        await client.send_document(chat_id, downloaded_file)

        await message.reply("✅ File uploaded successfully!")

    except Exception as e:
        print(f"Error occurred: {e}")
        await message.reply("❌ An error occurred while processing your file.")

# Run the client to listen for messages
app.run()
