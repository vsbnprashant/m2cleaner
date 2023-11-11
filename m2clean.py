import os
import datetime
import shutil

# Replace this with the path to your .m2 repository
path_to_m2_repository = r"C:\Users\...YourRepoDirectory...\.m2"

# Define the cutoff date in the format (year, month, day)
cutoff_date = datetime.datetime(2023, 1, 1)

# Function to remove files older than the cutoff date
def remove_old_files(directory, cutoff_date):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_modification_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_modification_date < cutoff_date:
                os.remove(file_path)
                print(f'Deleted {file_path}')

# Call the function to start the process
remove_old_files(path_to_m2_repository, cutoff_date)
