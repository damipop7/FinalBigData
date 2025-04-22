# This script orchestrates the entire data pipeline, from ingestion to visualization.
# It initializes all components, runs them in sequence, and handles any exceptions that may occur.

import os
import pandas as pd
import kaggle
import requests
from bs4 import BeautifulSoup
import logging
import yaml
from typing import Dict, List
from dotenv import load_dotenv

class DataIngestion:
    def __init__(self, config_path: str):
        # Load environment variables
        load_dotenv()
        
        # Verify Kaggle credentials are loaded
        self._verify_credentials()
        
        # Load config
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        
        self.setup_logging()
        
    def _verify_credentials(self):
        """Verify that Kaggle credentials are properly loaded"""
        required_vars = ['KAGGLE_USERNAME', 'KAGGLE_KEY']
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            raise EnvironmentError(
                f"Missing required environment variables: {', '.join(missing_vars)}\n"
                "Please ensure your .env file contains KAGGLE_USERNAME and KAGGLE_KEY"
            )
            
        # Configure Kaggle client
        kaggle.api.authenticate()
    
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def download_historical_data(self):
        """Downloads the Big Five European Soccer Leagues dataset"""
        try:
            dataset = self.config['data_sources']['historical']['kaggle_dataset']
            output_path = self.config['paths']['raw_data']
            
            self.logger.info(f"Downloading historical dataset: {dataset}")
            kaggle.api.dataset_download_files(
                dataset,
                path=output_path,
                unzip=True
            )
            self.logger.info(f"Successfully downloaded dataset to {output_path}")
            
        except Exception as e:
            self.logger.error(f"Error downloading historical data: {str(e)}")
            raise
            
    def scrape_current_season(self):
        """Scrapes current season data for top 5 leagues"""
        leagues = self.config['data_sources']['current_season']['leagues']
        season = self.config['data_sources']['current_season']['season']
        
        for league in leagues:
            try:
                self.logger.info(f"Scraping current season data for {league}")
                # Implement FBref scraping logic here
                # Save to raw data directory
                pass
            except Exception as e:
                self.logger.error(f"Error scraping {league} data: {str(e)}")
                
    def validate_data(self):
        """Validates that all required data files are present"""
        required_files = [
            # Add required file names here
        ]
        
        raw_data_path = self.config['paths']['raw_data']
        missing_files = []
        
        for file in required_files:
            if not os.path.exists(os.path.join(raw_data_path, file)):
                missing_files.append(file)
                
        if missing_files:
            raise FileNotFoundError(f"Missing required files: {missing_files}")
    
    def run(self):
        """Executes the full data ingestion process"""
        self.download_historical_data()
        self.scrape_current_season()
        self.validate_data()