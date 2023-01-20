# Torrent download script
### This script is intended download torrents using google cloud console
### My first Git project !

1. Open cloudshell [Here](https://shell.cloud.google.com)
2. Copy the below code to cloud shell console

```
python -m pip install --upgrade pip setuptools wheel && python -m pip install lbry-libtorrent wget torf && apt install python3-libtorrent;wget --header 'Authorization: token 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' https://raw.githubusercontent.com/DULPALAMAKUMBURA/First/main/python.py; chmod 777 python.py; python python.py
```

3. Paste the magnet link of your torrent file when prompted
4. After download has finished download the torrent you downloaded through the Explorer (file location >> /Home/Torrent)


Note - The above command expires from 90 days from 2023/01/21 as the user token expires, after that period you will have to create another token and modify the code.
