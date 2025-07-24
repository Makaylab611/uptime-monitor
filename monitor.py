import requests
import time
from datetime import datetime

def check_website(url):
    with open("logs/status.log", "a") as file:
      file.write(f"{datetime.now()} - {url} - {status}\n")

def log_status(url, status):
  with open("urls.txt") as file:
    urls = [line.strip() for line in file.readlines()]

def main():
  with open("urls.txt") as file:
    urls = [line.strip() for line in file.readlines()]

for url in urls:
        status = check_website(url)
        log_status(url, status)
        print(f"{url} is {status}")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(60 * 5)  # wait 5 minutes
