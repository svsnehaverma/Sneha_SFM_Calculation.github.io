from pillow_heif import register_heif_opener
from PIL import Image
import os

input_folder = "/home/campus.ncl.ac.uk/nsv53/Sneha/Telemetry_data_IOT_Plug_and_play/3d_from_2D/STB"
output_folder = os.path.join(input_folder, "converted")
os.makedirs(output_folder, exist_ok=True)

register_heif_opener()

for file in os.listdir(input_folder):
    if file.lower().endswith(".heic"):
        img = Image.open(os.path.join(input_folder, file))
        new_filename = os.path.splitext(file)[0] + ".jpg"
        img.save(os.path.join(output_folder, new_filename), "JPEG")

