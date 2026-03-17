import os
current_directory = os.getcwd()
print("Current directory:", current_directory)
print("\ndirectory contents:")
for item in os.listdir(current_directory):
    print(item)

os.mkdir("new_folder")
os.makedirs("path/to/new/directory", exist_ok=True)
os.rmdir("new_folder")
import shutil
shutil.rmtree("path/to/remove", ignore_errors=True)
