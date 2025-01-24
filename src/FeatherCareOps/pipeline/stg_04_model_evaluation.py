from FeatherCareOps.components.evaluation import Evaluation
from FeatherCareOps.config.configuration import ConfigurationManager
from FeatherCareOps import logger

STAGE_NAME='Evaluation stage'

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        eval_config=config.get_validation_config()
        evaluation=Evaluation(eval_config)
        evaluation.evalutation()
        evaluation.save_score()



if __name__=='__main__':
    try:
        logger.info(f'*****************')
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
        obj=EvaluationPipeline()
        obj.main()
        logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x')
    except Exception as e:
        raise e 