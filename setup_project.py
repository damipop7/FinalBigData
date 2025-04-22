# This script orchestrates the entire data pipeline, from ingestion to visualization.
# It initializes all components, runs them in sequence, and handles any exceptions that may occur.
import os
import yaml

def create_project_structure():
    # Define the directory structure
    directories = [
        'airflow/dags',
        'airflow/plugins/helpers',
        'config',
        'data/raw',
        'data/processed',
        'models/trained',
        'notebooks',
        'reports/figures',
        'src/data',
        'src/models',
        'src/visualization'
    ]
    
    # Create directories
    for dir_path in directories:
        os.makedirs(dir_path, exist_ok=True)
        
    # Create __init__.py files
    python_packages = [
        'src',
        'src/data',
        'src/models',
        'src/visualization'
    ]
    
    for package in python_packages:
        init_file = os.path.join(package, '__init__.py')
        if not os.path.exists(init_file):
            open(init_file, 'a').close()
            
    # Create config file
    config = {
        'data_sources': {
            'historical': {
                'name': 'Big Five European Soccer Leagues',
                'kaggle_dataset': 'hikne707/big-five-european-soccer-leagues',
                'years': '1995-2015'
            },
            'current_season': {
                'leagues': [
                    'Premier League',
                    'La Liga',
                    'Bundesliga',
                    'Serie A',
                    'Ligue 1'
                ],
                'season': '2024-2025'
            }
        },
        'paths': {
            'raw_data': 'data/raw',
            'processed_data': 'data/processed',
            'models': 'models/trained',
            'reports': 'reports/figures'
        }
    }
    
    with open('config/pipeline_config.yaml', 'w') as f:
        yaml.dump(config, f)

if __name__ == "__main__":
    create_project_structure()