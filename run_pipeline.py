# simple pipeline execution script
# Import necessary libraries
import logging
from src.data.data_ingestion import DataIngestion
from src.data.data_cleaning import DataCleaning
from src.data.feature_engineering import FeatureEngineering
from src.models.model_training import ModelTraining
from src.models.model_evaluation import ModelEvaluation
from src.visualization.visualize import Visualizer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_pipeline():
    try:
        # Initialize components
        data_ingestion = DataIngestion('config/pipeline_config.yaml')
        data_cleaning = DataCleaning('config/pipeline_config.yaml')
        feature_engineering = FeatureEngineering('config/pipeline_config.yaml')
        model_training = ModelTraining('config/pipeline_config.yaml')
        model_evaluation = ModelEvaluation('config/pipeline_config.yaml')
        visualizer = Visualizer('config/pipeline_config.yaml')
        
        # Execute pipeline steps
        logger.info("Starting data ingestion...")
        data_ingestion.run()
        
        logger.info("Starting data cleaning...")
        data_cleaning.run()
        
        logger.info("Starting feature engineering...")
        feature_engineering.run()
        
        logger.info("Starting model training...")
        model_training.run()
        
        logger.info("Starting model evaluation...")
        model_evaluation.run()
        
        logger.info("Generating visualizations...")
        visualizer.run()
        
        logger.info("Pipeline completed successfully!")
        
    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}")
        raise

if __name__ == "__main__":
    run_pipeline()