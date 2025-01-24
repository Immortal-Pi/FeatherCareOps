
from FeatherCareOps import logger
from FeatherCareOps.pipeline.stg_01_data_ingestion import DataIngestionTrainingPipeline
from FeatherCareOps.pipeline.stg_02_prepare_base_model import PrepareBaseModelPipeline
from FeatherCareOps.pipeline.stg_03_training import ModelTrainingPipeline
from FeatherCareOps.pipeline.stg_04_model_evaluation import EvaluationPipeline

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


STAGE_NAME='training'

try:
    logger.info(f'**********************')
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<<<\n\nx=========x')
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME='Evaluation stage'

try:
    logger.info(f'*****************')
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    obj=EvaluationPipeline()
    obj.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x')
except Exception as e:
    raise e 