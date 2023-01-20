import os
import shutil

folder_to_zip = '/path/to/folder'
zip_file_name = '/path/to/zip/file.zip'

shutil.make_archive(zip_file_name, 'zip', folder_to_zip)

# Delete the folder and its contents
shutil.rmtree(folder_to_zip)
