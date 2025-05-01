import logging
import os
import requests
import libtorrent as lt
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def humanbytes(byte_size):
    """
    Converts byte size to a human-readable format.
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if byte_size < 1024.0:
            return "%3.1f %s" % (byte_size, x)
        byte_size /= 1024.0
    return "%3.1f PB" % byte_size


def DetectFileSize(url):
    """
    Detects the size of a file via HTTP request headers.
    """
    r = requests.get(url, allow_redirects=True, stream=True)
    total_size = int(r.headers.get("content-length", 0))
    return total_size


def DownLoadFile(url, file_name, chunk_size, client, ud_type, message_id, chat_id):
    if os.path.exists(file_name):
        os.remove(file_name)

    if not url:
        return file_name

    # Handle magnet links with libtorrent
    if url.startswith("magnet:"):
        logger.info("Handling as magnet link")
        return download_torrent(url, file_name, client, ud_type, message_id, chat_id)

    # Handle HTTP/FTP links
    if not url.startswith("http://") and not url.startswith("https://"):
        logger.error(f"Unsupported URL scheme: {url}")
        raise ValueError(f"Unsupported URL scheme: {url}")

    # Proceed to download HTTP file
    r = requests.get(url, allow_redirects=True, stream=True)
    total_size = int(r.headers.get("content-length", 0))
    downloaded_size = 0

    with open(file_name, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            if chunk:
                fd.write(chunk)
                downloaded_size += len(chunk)
            if client is not None:
                try:
                    client.edit_message_text(
                        chat_id,
                        message_id,
                        text="{}: {} of {}".format(
                            ud_type,
                            humanbytes(downloaded_size),
                            humanbytes(total_size)
                        )
                    )
                except:
                    pass
    return file_name


def download_torrent(magnet_link, file_name, client=None, ud_type="", message_id=None, chat_id=None):
    """
    Downloads a torrent from a magnet link.
    """
    ses = lt.session()
    ses.listen_on(6881, 6891)

    params = {
        'save_path': os.path.dirname(file_name),
        'storage_mode': lt.storage_mode_t.storage_mode_sparse
    }

    handle = lt.add_magnet_uri(ses, magnet_link, params)
    logger.info(f"Downloading torrent: {magnet_link}")

    print("Fetching metadata...")
    while not handle.has_metadata():
        time.sleep(1)
        logger.info("Waiting for metadata...")

    info = handle.get_torrent_info()
    total_size = info.total_size()
    downloaded_size = 0

    logger.info(f"Starting torrent download...")

    while not handle.is_seed():
        status = handle.status()
        downloaded_size = status.total_done
        logger.info(f"Download speed: {status.download_rate / 1000:.2f} kB/s, "
                    f"Downloaded: {humanbytes(downloaded_size)} of {humanbytes(total_size)}")

        if client is not None:
            try:
                client.edit_message_text(
                    chat_id,
                    message_id,
                    text="{}: {} of {}".format(
                        ud_type,
                        humanbytes(downloaded_size),
                        humanbytes(total_size)
                    )
                )
            except:
                pass
        time.sleep(1)

    logger.info(f"Download completed: {file_name}")
    return file_name
  
