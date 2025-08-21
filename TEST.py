import os
import subprocess

# Define paths
images_folder = "/home/campus.ncl.ac.uk/nsv53/Sneha/Telemetry_data_IOT_Plug_and_play/3d_from_2D/STB/converted"  # Change this to your folder path
workspace_folder = "/home/campus.ncl.ac.uk/nsv53/Sneha/Telemetry_data_IOT_Plug_and_play/3d_from_2D"  # Output path

# Create workspace directories
os.makedirs(os.path.join(workspace_folder, "sparse"), exist_ok=True)
os.makedirs(os.path.join(workspace_folder, "dense"), exist_ok=True)

# Step 1: Feature Extraction
subprocess.run(["colmap", "feature_extractor",
                "--database_path", os.path.join(workspace_folder, "database.db"),
                "--image_path", images_folder])

# Step 2: Feature Matching
subprocess.run(["colmap", "exhaustive_matcher",
                "--database_path", os.path.join(workspace_folder, "database.db")])

# Step 3: Sparse Reconstruction
subprocess.run(["colmap", "mapper",
                "--database_path", os.path.join(workspace_folder, "database.db"),
                "--image_path", images_folder,
                "--output_path", os.path.join(workspace_folder, "sparse")])

# Step 4: Convert to dense format
subprocess.run(["colmap", "model_converter",
                "--input_path", os.path.join(workspace_folder, "sparse", "0"),
                "--output_path", os.path.join(workspace_folder, "sparse", "sparse.ply"),
                "--output_type", "PLY"])

# Step 5: Dense Reconstruction
subprocess.run(["colmap", "image_undistorter",
                "--image_path", images_folder,
                "--input_path", os.path.join(workspace_folder, "sparse", "0"),
                "--output_path", os.path.join(workspace_folder, "dense"),
                "--output_type", "COLMAP"])

subprocess.run(["colmap", "patch_match_stereo",
                "--workspace_path", os.path.join(workspace_folder, "dense"),
                "--workspace_format", "COLMAP",
                "--PatchMatchStereo.geom_consistency", "true"])

subprocess.run(["colmap", "stereo_fusion",
                "--workspace_path", os.path.join(workspace_folder, "dense"),
                "--workspace_format", "COLMAP",
                "--input_type", "photometric",
                "--output_path", os.path.join(workspace_folder, "dense", "fused.ply")])

# Step 6: Visualize Results
print("Run the following command to visualize:")
print(f"colmap gui --project_path {workspace_folder}")

