import subprocess

# Ask for magnet link
magnet_link = input("Enter magnet link: ")

# Download torrent using qbittorrent-nox
subprocess.run(["qbittorrent-nox","-d", magnet_link])

