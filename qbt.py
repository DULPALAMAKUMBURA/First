import subprocess

# Ask for magnet link
magnet_link = input("Enter magnet link: ")

# Ask for save path
save_path = input("Enter the path to save the torrent file: ")

# Download torrent using qbittorrent-nox
subprocess.run(["qbittorrent-nox", "-d", magnet_link, "--save-path=", save_path])

# Wait for download to complete
subprocess.run(["qbittorrent-nox", "-q"])

# Print success message
print("Torrent downloaded successfully")
