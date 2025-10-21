import requests
import json
import threading
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

terminal_width = os.get_terminal_size().columns

banner = [
    "███╗   ██╗██╗   ██╗██╗     ██╗     ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗",
    "████╗  ██║██║   ██║██║     ██║     ██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝",
    "██╔██╗ ██║██║   ██║██║     ██║     ███████║██║   ██║██║   ██║█████╔╝ ",
    "██║╚██╗██║██║   ██║██║     ██║     ██╔══██║██║   ██║██║   ██║██╔═██╗ ",
    "██║ ╚████║╚██████╔╝███████╗███████╗██║  ██║╚██████╔╝╚██████╔╝██║  ██╗",
    "╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝"
]

print("\033[91m")
for line in banner:
    print(line.center(terminal_width))
print("\033[0m")
print("-@soln".center(terminal_width))
print()

webhook = input("> Webhook: ")
message = input("> Message: ")
name = input("> Custom Name: ")
count = int(input("> Count: "))

start_time = time.time()

def send_message():
    data = {
        'content': message,
        'username': name
    }
    while True:
        try:
            requests.post(webhook, json=data, timeout=1)
            break
        except:
            continue

threads = []
for i in range(count):
    thread = threading.Thread(target=send_message)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Completed in {end_time - start_time:.2f} seconds")

input("\nPress Enter to exit...")