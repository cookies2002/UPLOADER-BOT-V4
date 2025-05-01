from pyrogram import Client
import os

# 1. Paste your actual session string, API ID and hash here
SESSION_STRING = "BQGLuVoATGjDdJJADRCABfCrVMz98w4M0ZOy2HjMDG6Y59ikghbHxBj5TYn97hp9BmtFOfVGl6uBxWvd4jbN6T_scF02FlqYK-aI1tGEpKFRBKCXdhk8czby34wF5I6NUz0krKQcejaKOQhSnCZo70WD0VpcPA1CdeXa4cL4lY8eqdMjS205QJfnJ3z5Wa8bgbDIplpOAvcijFZ5reBgxvaYt9B_LWeFxEvtaWBo4lxtqnMyMRt3INP15EATbXDnXnSEdt50jeCO0C9c0uIyy7laYo8hb9emXgxT3uOJB3bYieGFpdkeGUs7voJ-REsZ-y2TWTPv869b1OpQZX_FEB0NGstATAAAAAHYECwWAA"  # Replace with your session string
API_ID = 25934170  # Replace with your actual API ID
API_HASH = "d199295026b1e44ec3c72ef53f806a1f"

# 2. File and chat target
TARGET_CHAT = "me"  # or channel username like "@YourChannel"
FILE_PATH = "./DOWNLOADS/myvideo.mp4"  # change the filename to your downloaded file

# 3. Upload logic
app = Client(session_name=SESSION_STRING, api_id=API_ID, api_hash=API_HASH)

with app:
    print("Uploading file...")
    app.send_document(
        TARGET_CHAT,
        document=FILE_PATH,
        caption="Uploaded via userbot - 4GB support!",
        file_name=os.path.basename(FILE_PATH)
    )
    print("Upload complete!")
    
