import os
import requests
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def humanbytes(size):
    # Converts bytes to human-readable format
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"

def DownLoadFile(url, file_name, chunk_size=1024 * 1024, client=None, ud_type="Downloading", message_id=None, chat_id=None):
    if os.path.exists(file_name):
        os.remove(file_name)
    if not url:
        return file_name

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        with requests.get(url, allow_redirects=True, stream=True, headers=headers, timeout=30) as r:
            r.raise_for_status()
            total_size = int(r.headers.get("content-length", 0))
            downloaded_size = 0
            last_percent_reported = -1

            with open(file_name, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    if chunk:
                        fd.write(chunk)
                        downloaded_size += len(chunk)

                        if client and total_size:
                            percent = int((downloaded_size / total_size) * 100)
                            if percent % 5 == 0 and percent != last_percent_reported:
                                last_percent_reported = percent
                                try:
                                    client.edit_message_text(
                                        chat_id,
                                        message_id,
                                        text=f"{ud_type}: {humanbytes(downloaded_size)} of {humanbytes(total_size)} ({percent}%)"
                                    )
                                except Exception as e:
                                    logger.debug(f"Update failed: {e}")

        return file_name

    except requests.exceptions.RequestException as e:
        logger.error(f"Download failed: {e}")
        return None
      
