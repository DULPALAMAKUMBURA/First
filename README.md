# Torrent download script
### This script is intended to download torrents using google cloud console
### My first Git project !
### First Method
1. Open cloudshell [Here](https://shell.cloud.google.com)
2. Copy the below code to cloud shell console

```
python3 -m pip install --upgrade pip setuptools wheel && python3 -m pip install lbry-libtorrent wget torf && apt install python3-libtorrent;wget --header 'Authorization: token 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' https://raw.githubusercontent.com/DULPALAMAKUMBURA/Torrent-Download-Cloudshell/main/torrentzip.py; chmod 777 torrentzip.py; python3 torrentzip.py
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
5. Hit CTRL+C to interrupt seeding after download has finished
6. Save the downloaded torrent using Explorer

### Alternatively you can use google colab from <a href="https://colab.research.google.com/drive/1Kw2sSGgVvUNIGWAfc3x6RVkz-Uup5XkK?usp=sharing" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

### Also try Gitpod for downloaading very large torrent files, open gitpod [HERE](https://www.gitpod.io)
Note: Use IntelliJ IDEA as editor

Note - The above commands expires from 90 days from 2023/01/21 as the user token expires, after that period you will have to create another token and modify the code.
