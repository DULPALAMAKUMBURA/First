import os
import shutil

folder_to_zip = '/home/torrent'
zip_file_name = 'torrent.zip'

shutil.make_archive(zip_file_name, 'zip', folder_to_zip)
