import pandas as pd
import shutil
import os


def move_files(csv_file):
    df = pd.read_csv(csv_file)

    for index, row in df.iterrows():
        source_path = row["source"].replace("\\", "/")
        desired_path = row["desired-source"].replace("\\", "/")

        source_path = os.path.normpath(source_path)
        desired_path = os.path.normpath(desired_path)

        # Ensure the destination folder exists, create it if not
        destination_folder = os.path.dirname(desired_path)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        try:
            shutil.move(source_path, desired_path)
            print(f"Moved '{source_path}' to '{desired_path}'")
        except FileNotFoundError:
            print(f"File '{source_path}' not found.")
        except shutil.Error as e:
            print(f"Error while moving '{source_path}' to '{desired_path}': {e}")


if __name__ == "__main__":
    csv_file = "res/card-deck-data.csv"  # Replace with your actual CSV file path
    move_files(csv_file)
