import os
import subprocess

# Define your paths
database_path = "/home/campus.ncl.ac.uk/nsv53/Sneha/Telemetry_data_IOT_Plug_and_play/3d_from_2D/database.db"
image_path = "/home/campus.ncl.ac.uk/nsv53/Sneha/Telemetry_data_IOT_Plug_and_play/3d_from_2D/STB/converted/"

# Function to check if paths exist
def check_path(path):
    if not os.path.exists(path):
        print(f" Error: Path does not exist -> {path}")
        exit(1)

# Validate paths before running COLMAP
check_path(database_path)
check_path(image_path)

# Format paths to handle spaces
database_path_escaped = f'"{database_path}"'
image_path_escaped = f'"{image_path}"'

# Run COLMAP GUI
print("Opening COLMAP GUI with the correct paths...")
subprocess.run(f'colmap gui --database_path {database_path_escaped} --image_path {image_path_escaped}', shell=True)

