import os
from datetime import datetime
ROOT_DIR = os.getcwd()#to get current working directory

CONFIG_DIR = "config"
CONFIG_FILENAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILENAME)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y=%m-%d_%H-%M-%S')}"

# Training pipeline related variable
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"


# Data Ingestion related variable

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"


# data validation variabel

DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_ARTIFACT_DIR = "data_validation"
DATA_VALIDATION_SCHEMA_DIR = "schema_file_name"

# Data Transformation Variabel

DATA_TRANSFORMATION_CONFIG_KEY = "data_transformation_config"
DATA_TRANSFORMATION_ARTIFACT_KEY = "data_transformation"
DATA_ADD_BEDROOM_KEY = "add_bedroom_per_room"
DATA_TRANSFORMED_DIR = "transformed_dir"
DATA_TRANSFORMED_TRAIN_DIR = "transformed_train_dir"
DATA_TRANSFORMED_TEST_DIR = "transformed_test_dir"
DATA_PROCESSING_DIR = "preprocessing_dir"
DATA_PROCESSED_FILE_NAME = "preprocessed_object_file_name"


# Data model train config

MODEL_TRAIN_CONFIG = "model_trainer_config"
MODEL_TRAIN_ARTIFACT = "model_train"
MODEL_TRAIN_DIR_KEY = "trained_model_dir"
MODEL_FILE_NAME = "model_file_name"
MODEL_BASE_ACCURACY = "base_accuracy"


# MODEL EVALUATIUON CONFIG

MODEL_EVAL_CONFIG = "model_evaluation_config"
MODEL_EVAL_ARTIFACT = "model_evaluation"
MODEL__EVAL_FILE_NAME = "model_evaluation_file_name"
