import shutil
import subprocess

if shutil.which("transmission-cli") is None:
    print("transmission-cli is not installed.")
else:
    subprocess.run(['transmission-cli', magnet_link, '-w', save_path])



magnet_link = 'magnet:?xt=urn:btih:HASH'
save_path = '/path/to/save/directory'

subprocess.run(['transmission-cli', magnet_link, '-w', save_path])
