
from FeatherCareOps import logger
from FeatherCareOps.pipeline.stg_01_data_ingestion import DataIngestionTrainingPipeline
from FeatherCareOps.pipeline.stg_02_prepare_base_model import PrepareBaseModelPipeline


STAGE_NAME='DATA INGESTION STAGE'

try:
    logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<< \n\n x==========x')
except Exception as e:
    logger.exception(e)
    raise e 



STAGE_NAME='Prepare base model'

try:
    logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
    obj=PrepareBaseModelPipeline()
    obj.main()
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<<\n\nx==========x')
except Exception as e:
    logger.exception(e)
    raise e 
