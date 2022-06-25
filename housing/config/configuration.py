
from housing.component import data_validation
from housing.entity.congif_entity import DataIngestionConfig, DataTransformationConfig,DataValidationConfig,   \
ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig,TrainingPipelineConfig
from housing.util.util import read_yaml_file
from housing.logger import logging
import sys,os
from housing.constant import *
from housing.exception import HousingException




class Configuration:

    def __init__(self,
    config_file_path = CONFIG_FILE_PATH,
    current_time_stamp = CURRENT_TIME_STAMP,
    ) -> None:
        self.config_info = read_yaml_file(file_path=config_file_path)
        self.training_pipeline_config = self.get_training_pipeline_config()
        self.time_stamp = current_time_stamp
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir=os.path.join(
                artifact_dir,
                DATA_INGESTION_CONFIG_KEY,
                self.time_stamp
            )
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            tgz_download_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]
            )
            raw_data_dir = os.path.join(data_ingestion_artifact_dir,
            data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY]
            )

            ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY]
            )
            ingested_train_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]
            )
            ingested_test_dir =os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]
            )


            data_ingestion_config=DataIngestionConfig(
                dataset_download_url=dataset_download_url, 
                tgz_download_dir=tgz_download_dir, 
                raw_data_dir=raw_data_dir, 
                ingested_train_dir=ingested_train_dir, 
                ingested_test_dir=ingested_test_dir
            )
            logging.info(f"Data Ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise HousingException(e,sys) from e





    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_validation_artifact_dir=os.path.join(
                artifact_dir,
                DATA_VALIDATION_ARTIFACT_DIR,
                self.time_stamp
            )
            data_validation_info = self.config_info[DATA_VALIDATION_CONFIG_KEY]
            data_schema = os.path.join(data_validation_artifact_dir,data_validation_info[DATA_VALIDATION_SCHEMA_DIR])

            data_validation_config = DataValidationConfig(schema_file_path=data_schema)

            logging.info(f"data validation part : {data_validation_config}")
            return data_validation_config
        except Exception as e:
            raise HousingException(e,sys) from e





    def get_data_transformation_config(self)-> DataTransformationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_transformation_artifact_dir=os.path.join(
                artifact_dir,
                DATA_TRANSFORMATION_ARTIFACT_KEY,
                self.time_stamp
            )
            Data_transformation_info = self.config_info[DATA_TRANSFORMATION_CONFIG_KEY]
            add_bedroom_per_room = os.path.join(artifact_dir,str(Data_transformation_info[DATA_ADD_BEDROOM_KEY]))
            transformed_dir = os.path.join(artifact_dir,Data_transformation_info[DATA_TRANSFORMED_DIR])
            transformed_train_dir = os.path.join(transformed_dir,Data_transformation_info[DATA_TRANSFORMED_TRAIN_DIR])
            transformed_test_dir = os.path.join(transformed_dir,Data_transformation_info[DATA_TRANSFORMED_TEST_DIR])
            preprocessing_dir= os.path.join(artifact_dir,Data_transformation_info[DATA_PROCESSING_DIR])
            preprocessed_object_file_name = os.path.join(preprocessing_dir,Data_transformation_info[DATA_PROCESSED_FILE_NAME])

            data_transformation_config = DataTransformationConfig(add_bedroom_per_room=add_bedroom_per_room,
            transformed_test_dir=transformed_test_dir,
            transformed_train_dir=transformed_train_dir,
            preprocessed_object_file_path=preprocessed_object_file_name)
            logging.info(f"data transformation part : {data_transformation_config}")

            return data_transformation_config

        except Exception as e:
            raise HousingException(e,sys) from e





    def get_model_trainer_config(self) -> ModelTrainerConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_transformation_artifact_dir=os.path.join(
                artifact_dir,
                MODEL_TRAIN_ARTIFACT,
                self.time_stamp
            )
            model_train_info = self.config_info[MODEL_TRAIN_CONFIG] 
            trained_model_dir = os.path.join(data_transformation_artifact_dir,model_train_info[MODEL_TRAIN_DIR_KEY])
            model_file_name = os.path.join(data_transformation_artifact_dir,model_train_info[MODEL_FILE_NAME])
            base_accuracy = str(model_train_info[MODEL_BASE_ACCURACY])

            model_train_config = ModelTrainerConfig(trained_model_file_path=trained_model_dir,base_accuracy=base_accuracy)

            logging.info(f"model tainer :{model_train_config}")
            return model_train_config
        except Exception as e:
            raise HousingException(e,sys)




    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            Model_eval_artifact_dir=os.path.join(
                artifact_dir,
                MODEL_EVAL_ARTIFACT,
                self.time_stamp
            )
            model_eval_info = self.config_info[MODEL_EVAL_CONFIG]
            model_evaluation_file_name= os.path.join(Model_eval_artifact_dir,model_eval_info[MODEL__EVAL_FILE_NAME])

            model_eval_config = ModelEvaluationConfig(model_evaluation_file_path=model_evaluation_file_name,time_stamp=self.time_stamp)
            logging.info(f"model evaluation : {model_eval_config}")
            return model_eval_config
        except Exception as e:
            raise HousingException(e,sys)
    def get_model_pusher_congif(self) -> ModelPusherConfig:
        pass
    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipleine config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e