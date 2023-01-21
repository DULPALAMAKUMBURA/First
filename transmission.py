import subprocess
import os
import shutil

magnet_link = input("Enter the magnet link: ")
save_path = input("Enter the save path (e.g. /path/to/save/directory): ")

if not os.path.exists(save_path):
    os.makedirs(save_path)

if shutil.which("transmission-cli") is None:
    print("transmission-cli is not installed.")
else:
    subprocess.run(['transmission-cli', magnet_link, '-w', save_path])
    print("download started")
    
# Wait for download to finish
    subprocess.run(['transmission-cli', '-l']) 
# Stop seeding
    subprocess.run(['transmission-cli', '--stop-seed', magnet_link])

