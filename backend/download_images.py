from pathlib import Path

from ftp_downloader import FTPDownloader

FTP_HOST = '84.201.179.203'
FTP_PORT = '21'
FTP_USER = 'neuro_models'
FTP_PASSWORD = 'dkkjaw12m0'


labels = ['2017']

for label in labels:
    BASE_DIR = Path(__file__).resolve().parent
    IMAGES_FOLDER = f'media/{label}'
    IMAGES_PATH = BASE_DIR.joinpath(IMAGES_FOLDER)
    FTP_DOWNLOAD_MODELS_PATH = label
    if __name__ == '__main__':
        ftp_client = FTPDownloader(FTP_HOST, FTP_PORT, FTP_USER, FTP_PASSWORD)
        ftp_client.download_dir(
            download_from_dir=FTP_DOWNLOAD_MODELS_PATH,
            upload_to_dir=IMAGES_PATH,
            exclude_ext=['.zip'],
            with_root_path=False
        )
