import os
from pathlib import Path
import logging

# logging string
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

project_name = "spforecasting"

list_of_files = [
    ".github/workflows/.gitkeep",
    "docs/",
    "flowchart/",
    "infrastructure/",
    "notebooks/data"
    "notebooks/data_collection.ipynb",
    "notebooks/data_preprocessing.ipynb",
    "notebooks/EDA.ipynb",
    "notebooks/feature_engineering.ipynb",
    "notebooks/model_training_evaluation.ipynb",
    "scripts/",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/artifact/__init__.py",
    f"src/{project_name}/cloud_storage/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/model_pusher.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/constants/application.py",
    f"src/{project_name}/constants/database.py",
    f"src/{project_name}/constants/env_variable.py",
    f"src/{project_name}/constants/s3_bucket.py",
    f"src/{project_name}/constants/prediction_pipeline/__init__.py",
    f"src/{project_name}/constants/training_pipeline/__init__.py",
    f"src/{project_name}/data_access/__init__.py",
    f"src/{project_name}/data_access/stock_data.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/artifact_entity.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/ml/__init__.py",
    f"src/{project_name}/ml/metric/__init__.py",
    f"src/{project_name}/ml/model/__init__.py",
    f"src/{project_name}/ml/model/estimator.py",
    f"src/{project_name}/ml/model/s3_estimator.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/pipeline/train_pipeline.py",
    f"src/{project_name}/utils/__init__.py",
    "static/",
    "templates/"
    "app.py",
    "config/config.yaml",
    "params.yaml",
    "Dockerfile",
    "deployment.yaml",
    "mysql-deployment.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


for filepath in list_of_files:
    # Convert to Path object
    path = Path(filepath)
    
    # If path ends with a '/', treat it as a directory
    if filepath.endswith('/'):
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            logging.info(f"Creating directory: {filepath}")
        else:
            logging.info(f"Directory {filepath} already exists.")
    else:
        # Ensure parent directory exists
        if not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            logging.info(f"Creating directory: {path.parent}")

        # Create the file if it doesn't exist or is empty
        if not path.exists() or path.stat().st_size == 0:
            path.touch()
            logging.info(f"Creating empty file: {filepath}")
        else:
            logging.info(f"File {filepath} already exists or is not empty.")

logging.info("Project structure created successfully.")
    