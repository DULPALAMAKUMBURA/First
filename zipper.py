import os
import shutil

folder_to_zip = '/home/Torrent'
zip_file_name = 'torrent.zip'

shutil.make_archive(zip_file_name, 'zip', folder_to_zip)

# Delete the folder and its contents
shutil.rmtree(folder_to_zip)
print(f"{zip_file_name} created successfully.")
