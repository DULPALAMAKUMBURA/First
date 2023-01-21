# Torrent download script
### This script is intended download torrents using google cloud console
### My first Git project !
### First Method
1. Open cloudshell [Here](https://shell.cloud.google.com)
2. Copy the below code to cloud shell console

```
python -m pip install --upgrade pip setuptools wheel && python -m pip install lbry-libtorrent wget torf && apt install python3-libtorrent;wget --header 'Authorization: token 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' https://raw.githubusercontent.com/DULPALAMAKUMBURA/Torrent-Download-Cloudshell/main/python.py; chmod 777 python.py; python python.py
```

3. Paste the magnet link of your torrent file when prompted
4. After download has finished download the torrent.zip you downloaded through the Explorer (file location >> /Home/user)

### Second Method
1. Open cloudshell [Here](https://shell.cloud.google.com)
2. Copy the below code to cloud shell console

```
sudo apt install transmission-cli; wget --header 'Authorization: token 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' https://raw.githubusercontent.com/DULPALAMAKUMBURA/Torrent-Download-Cloudshell/main/transmission.py; python transmission.py
```

3. Paste the magnet link of your torrent file when prompted
4. Enter the prefered location you want torrent file to get downloaded
5. Hit CTRL+C to interupt seeding after download finished
6. Save the downloaded torrent using Explorer

Note - The above commands expires from 90 days from 2023/01/21 as the user token expires, after that period you will have to create another token and modify the code.
