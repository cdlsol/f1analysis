import kaggle
from dotenv import load_dotenv
import os

load_dotenv()  # Load the variables from the .env file

#Kaggle Dataset info
dataset_name = 'rohanrao/formula-1-world-championship-1950-2020'

#Target directory to save the data
# data_dir = '/home/carlos/f1/f1_analysis/f1_analysis/data' #map and change to container data dir in the future
data_dir = '/app/data'

#Check if directory exists (create it if it doesn't)
os.makedirs(data_dir, exist_ok=True)

#Download and unzip the dataset into the specified directory
kaggle.api.dataset_download_files(dataset_name, path=data_dir, unzip=True)

# Confirm that the dataset has been downloaded
print(f"Downloaded Dataset to {data_dir}")