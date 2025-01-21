
from FeatherCareOps import logger
from FeatherCareOps.pipeline.stg_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME='DATA INGESTION STAGE'

try:
    logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<< \n\n x==========x')
except Exception as e:
    logger.exception(e)
    raise e 

