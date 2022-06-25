from collections import namedtuple

DataIngestionCongif = namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])


DataValidationConfig = namedtuple("DataValidationConfig",["schema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig",[])

ModelTrainerConfig = namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])

ModelEvaluationCongif = namedtuple("ModelEvaluationCongif",["model_evaluation_file_path","time_stamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig",["export_dir_path"])

