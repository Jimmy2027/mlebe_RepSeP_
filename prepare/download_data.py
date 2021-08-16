"""
Download the data dir from Nextcloud.
"""

import os
import tempfile
from pathlib import Path


def maybe_getfrom_url(download_url: str, out_path: Path):
    """Download from url and extract to out_path if not already there."""
    if not out_path.exists():
        out_path.mkdir()
        print(f'{out_path} does not exist. Downloading...')
        filename = "data"
        with tempfile.TemporaryDirectory() as tmpdirname:
            wget_command = f'wget {download_url} -O {tmpdirname}/{filename}.zip'
            print(f'Getting {download_url}.')
            os.system(wget_command)

            unzip_command = f'unzip {tmpdirname}/{filename + ".zip"} -d {out_path}/'
            os.system(unzip_command)
    else:
        print(f'{out_path} exists. Skipping...')


if __name__ == '__main__':
    data_url = "https://hendrikklug.xyz/nextcloud/index.php/s/feFD6ws95EDXEGK/download"
    out_path = Path(__file__).parent.parent

    maybe_getfrom_url(download_url=data_url, out_path=out_path)
