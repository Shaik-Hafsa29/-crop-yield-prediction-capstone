import kagglehub
import os
import shutil

def download_data():
    try:
        print("Downloading dataset using kagglehub...")
        path = kagglehub.dataset_download("patelris/crop-yield-prediction-dataset")
        print("Path to dataset files:", path)

        # Copy files to current directory
        for filename in os.listdir(path):
            source = os.path.join(path, filename)
            destination = os.path.join(os.getcwd(), filename)
            if os.path.isfile(source):
                shutil.copy(source, destination)
                print(f"Copied {filename} to {destination}")
        print("Data download complete.")
    except Exception as e:
        print(f"Error downloading data: {e}")
        print("Please ensure you have kaggle authentication if required.")

if __name__ == "__main__":
    download_data()
