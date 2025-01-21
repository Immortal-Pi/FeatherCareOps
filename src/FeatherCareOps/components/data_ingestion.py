import os 
import zipfile
import gdown 
from FeatherCareOps import logger
from FeatherCareOps.utils.common import get_size
from FeatherCareOps.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self)-> str:
        """ 
        Fetch data from the URL 
        """
        try:
            dataset_url=self.config.source_URL
            zip_download_dir=self.config.local_data_file
            if not os.path.exists(self.config.local_data_file):
                os.makedirs('artifacts/data_ingestion',exist_ok=True)
                logger.info(f'Downlading data from {dataset_url} into file {zip_download_dir}')
                file_id=dataset_url.split('/')[-2]
                prefix='https://drive.google.com/uc?/export=download&id='
                gdown.download(prefix+file_id,zip_download_dir)
                logger.info(f'Downloaded data from {dataset_url} into file {zip_download_dir}')
            else:
                logger.info(f'File already exists of size: {get_size(Path(self.config.local_data_file))}')   

        except Exception as e:
            raise e 
        

    def extract_zip_file(self):
        """ 
        extract the zip file into the data directory 
        Return: 
            None 
        """
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f'Extracted the zip file contents')
            