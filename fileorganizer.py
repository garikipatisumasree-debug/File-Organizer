import os
import shutil

folder = "test_folder"

for file in os.listdir(folder):
    if file.endswith(".txt"):
        shutil.move(f"{folder}/{file}", f"{folder}/TextFiles/{file}")