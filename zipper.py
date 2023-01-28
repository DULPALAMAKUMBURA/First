import zipfile
import shutil

print("Starting to zip downloaded torrent file pls wait...")
folder_to_zip = input("Enter the folder path you want to zip")
zip_file_name = input("Enter the name of the zip file")

shutil.make_archive(zip_file_name, 'zip', folder_to_zip)
