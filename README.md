# Soccer Analytics Pipeline

This repository contains an end-to-end data pipeline for soccer analytics, focusing on player performance insights and league table predictions.

## Project Structure

```
soccer-analytics-pipeline/
├── airflow/
│   ├── dags/
│   │   └── soccer_pipeline_dag.py
│   └── plugins/
│       └── helpers/
│           └── __init__.py
├── config/
│   └── pipeline_config.yaml
├── data/
│   ├── raw/              # Git LFS tracked
│   ├── processed/        # Git LFS tracked  
│   └── .gitattributes
├── models/
│   └── trained/
├── notebooks/
│   ├── eda.ipynb
│   └── model_evaluation.ipynb
├── reports/
│   └── figures/
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_cleaning.py
│   │   └── feature_engineering.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── model_training.py
│   │   └── model_evaluation.py
│   └── visualization/
│       ├── __init__.py
│       └── visualize.py
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
└── run_pipeline.py
```

## Setup and Installation

1. Clone this repository:
```cmd
git clone <repository-url>
cd FinalBigData
```

2. Create and activate a virtual environment:
```cmd
python -m venv .venv
.venv\Scripts\activate
```

3. Install required packages:
```cmd
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Configure Kaggle API credentials:
   - Create a `.env` file in the project root
   - Add your Kaggle credentials:
   ```properties
   KAGGLE_USERNAME=your_username_here
   KAGGLE_KEY=your_key_here
   FBREF_RATE_LIMIT=3
   ```

5. Set up Airflow (Windows):
```cmd
pip install apache-airflow

set AIRFLOW_HOME=%CD%\airflow
airflow db init

airflow users create ^
    --username admin ^
    --firstname Admin ^
    --lastname User ^
    --role Admin ^
    --email admin@example.com ^
    --password admin
```

## Running the Pipeline

### Option 1: Using Airflow (Recommended)
```bash
# Start Airflow web server
airflow webserver --port 8080

# In a new terminal, start Airflow scheduler
airflow scheduler

# Access the Airflow UI at http://localhost:8080
# Trigger the 'soccer_analytics_pipeline' DAG
```

### Option 2: Command-Line Execution
```bash
python run_pipeline.py
```

## Pipeline Components

### 1. Data Ingestion
- Downloads datasets from Kaggle
- Performs web scraping for current season data
- Saves raw data to `data/raw/` directory

### 2. Data Cleaning and Processing
- Standardizes player and team names across datasets
- Handles missing values
- Converts data types
- Merges datasets when necessary

### 3. EDA and Feature Engineering
- Generates player performance metrics
- Creates aggregated team statistics
- Extracts temporal patterns
- Prepares features for predictive modeling

### 4. Model Training
- Trains models to predict league table standings
- Uses historical data (1995-2015)
- Implements cross-validation
- Saves trained models

### 5. Model Evaluation
- Compares predictions with actual 2024/25 results
- Calculates performance metrics
- Identifies strengths and weaknesses

### 6. Visualization
- Creates interactive dashboards
- Generates player performance charts
- Visualizes prediction accuracy