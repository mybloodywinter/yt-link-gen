import requests
import random
import colorama
from colorama import Fore
from colorama import Style


colorama.init()
URL = "https://www.youtube.com/watch?v="
CHAR = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
LENGTH = 11

def generate_link():
    VIDEO_ID = ''
    for _ in range(LENGTH):
        URL_SYMBOL = random.choice(CHAR)
        VIDEO_ID = VIDEO_ID + URL_SYMBOL
    LINK = URL + VIDEO_ID
    return LINK

def check_if_available_to_view(LINK):
    RESPONSE = requests.get(LINK)
    if "detected unusual traffic from your computer network" in RESPONSE.text.lower() or "Nos systèmes ont détecté un trafic exceptionnel sur votre" in RESPONSE.text.lower():
        return "Blocked"
    if "this video isn't available anymore" in RESPONSE.text.lower() or "cette vidéo n'est plus disponible" in RESPONSE.text.lower():
        return False
    else:
        return True

print("\n[...] Generating :\n")

while True:
    LINK = generate_link()
    print(f"{Fore.RED}{LINK}{Style.RESET_ALL}")
    if check_if_available_to_view(LINK) == "Blocked":
        print(f"{Fore.CYAN}Your IP just got blocked !{Style.RESET_ALL}\n")
        break
    if check_if_available_to_view(LINK):
        print(f"\n{Fore.GREEN}{LINK} | FOUND ! Working URL{Style.RESET_ALL}\n")
        break
