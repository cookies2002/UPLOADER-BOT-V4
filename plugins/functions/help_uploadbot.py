import logging
import os
import requests
from concurrent.futures import ThreadPoolExecutor
import time

# Set up logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def DetectFileSize(url):
    r = requests.get(url, allow_redirects=True, stream=True)
    total_size = int(r.headers.get("content-length", 0))
    return total_size

def humanbytes(size):
    # Convert byte size to a human-readable format
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0
    return "%3.1f %s" % (size, 'PB')

def download_chunk(url, start_byte, end_byte, chunk_index, file_name):
    headers = {'Range': f"bytes={start_byte}-{end_byte}"}
    r = requests.get(url, headers=headers, stream=True)
    
    with open(f"{file_name}.part{chunk_index}", 'wb') as f:
        f.write(r.content)
    
    logger.debug(f"Downloaded chunk {chunk_index} from {start_byte} to {end_byte}")

def merge_files(file_name, total_chunks):
    with open(file_name, 'wb') as f_out:
        for i in range(total_chunks):
            with open(f"{file_name}.part{i}", 'rb') as f_in:
                f_out.write(f_in.read())
            os.remove(f"{file_name}.part{i}")  # Clean up chunk files

    logger.debug(f"Merge completed for {file_name}")

def DownLoadFile(url, file_name, chunk_size, client, ud_type, message_id, chat_id):
    if os.path.exists(file_name):
        os.remove(file_name)

    if not url:
        return file_name

    r = requests.get(url, allow_redirects=True, stream=True)
    total_size = int(r.headers.get("content-length", 0))

    total_chunks = (total_size // chunk_size) + 1
    logger.debug(f"Total size: {total_size}, Total chunks: {total_chunks}")

    # Use ThreadPoolExecutor to download file chunks in parallel
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        for i in range(total_chunks):
            start_byte = i * chunk_size
            end_byte = min((i + 1) * chunk_size - 1, total_size - 1)
            futures.append(executor.submit(download_chunk, url, start_byte, end_byte, i, file_name))

        # Wait for all threads to finish
        for future in futures:
            future.result()

    # Merge all downloaded parts
    merge_files(file_name, total_chunks)

    # Optionally, you can update the download progress via client (if provided)
    if client is not None:
        try:
            client.edit_message_text(
                chat_id,
                message_id,
                text="Download completed: {} of {}".format(humanbytes(total_size), humanbytes(total_size))
            )
        except Exception as e:
            logger.error(f"Failed to update message: {e}")

    return file_name
  
