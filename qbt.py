import subprocess
import json

# Login to Mega
email = input("Enter your email: ")
password = input("Enter your password: ")
login = subprocess.run(["megatools", "login", email, password], capture_output=True)

# check if login is successful
if login.returncode != 0:
    print("Error: Invalid email or password")
    exit()

# Get user info
user_info = subprocess.run(["megatools", "info"], capture_output=True)
user_info = json.loads(user_info.stdout)

# Print user info
print("Name:", user_info["name"])
print("Email:", user_info["email"])
print("Storage:", user_info["storage"])

# Get list of files
files = subprocess.run(["megatools", "ls", "/Root"], capture_output=True)
files = json.loads(files.stdout)

# Print list of files
print("\nList of files:")
for file in files:
    print(file["name"])

