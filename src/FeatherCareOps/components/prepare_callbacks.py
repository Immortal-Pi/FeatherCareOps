import os 
from urllib.request import Request
from zipfile import ZipFile
import tensorflow as tf 
import time 
from FeatherCareOps.config.configuration import PrepareCallBackConfig




class PrepareCallback:
    def __init__(self,config:PrepareCallBackConfig):
        self.config=config

    @property
    def _create_tb_callbacks(self):
        """ 
        generates a unique sub-directort for tensorboard logs
        based on current timestamp
        Returns:
            tf.keras.callbacks.TensorBoard: tensorboard object configured to save logs to the generated directory
        """
        timestamp=time.strftime('%Y-%m-%d-%H-%M-%S')
        tb_running_log_dir=os.path.join(
            self.config.tensorboard_root_log_dir,
            f'tb_logs_at_{timestamp}'
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    
    @property 
    def _create_ckpt_callbacks(self):
        """ 
        creates a model checkpoint callbacks: to save the model's weight whenever it achieves the best performance during training 

        """
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True 
        )
    
    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]