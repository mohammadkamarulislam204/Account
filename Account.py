#!/usr/bin/env python3
# Account.py
# Run: python3 Account.py
import os
import sys
import time

# ---------------- CONFIG ----------------
EXPECTED_ACCOUNT = "111101299132"
EXPECTED_PIN     = "549265"
BALANCE_FILE     = "balance.txt"
INITIAL_BALANCE  = 150000000
GIT_REPO_URL     = "https://github.com/mohammadkamarulislam204/Account.git"

# ANSI COLORS
RESET   = "\033[0m"
BOLD    = "\033[1m"
GREEN   = "\033[32m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
RED     = "\033[31m"
CYAN    = "\033[36m"

# ---------------- FUNCTIONS ----------------
def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def read_balance():
    try:
        with open(BALANCE_FILE, 'r') as f:
            return int(f.read().strip())
    except:
        return INITIAL_BALANCE

def write_balance(new_balance):
    with open(BALANCE_FILE, 'w') as f:
        f.write(str(int(new_balance)))

def format_taka(n):
    return f"{n:,} Taka"

def show_ui(balance):
    clear()
    # VIP Banner
    vip_banner = f"{BOLD}{GREEN}VIP{RESET}"
    print(vip_banner.center(60))
    print()
    # BINANCE
    print(f"{BLUE}BINANCE{RESET}")
    # Bank Name
    print(f"{MAGENTA}DUTCEH-BANGLA BANK LIMITED{RESET}")
    # Name
    print(f"{RED}MOHAMMAD KAMARUL ISLAM{RESET}")
    # Account number + Balance
    print(f"{GREEN}Account number : {EXPECTED_ACCOUNT}{RESET}")
    print(f"{GREEN}Balance : {format_taka(balance)}{RESET}")
    print()
    # Options
    print(f"{BLUE}1. Refresh{RESET}")
    print("0. Exit")
    print()

def authenticate():
    clear()
    print(f"{BOLD}Login required{RESET}")
    for _ in range(3):
        acc = input("Account number: ").strip()
        pin = input("PIN: ").strip()
        if acc == EXPECTED_ACCOUNT and pin == EXPECTED_PIN:
            return True
        else:
            print(f"{RED}Invalid credentials. Try again.{RESET}")
    return False

def refresh_tool():
    print(f"{BLUE}Checking for updates...{RESET}")
    time.sleep(1)
    result = os.system("git pull")
    if result == 0:
        print(f"{GREEN}Tool updated successfully! Restart to apply changes.{RESET}")
    else:
        print(f"{RED}Update failed. Make sure Git is installed and repository exists.{RESET}")
    input("Press Enter to continue...")

def main():
    if not os.path.exists(BALANCE_FILE):
        write_balance(INITIAL_BALANCE)

    if not authenticate():
        print(f"{RED}Too many failed attempts. Exiting.{RESET}")
        sys.exit(1)

    while True:
        balance = read_balance()
        show_ui(balance)
        choice = input("Select option: ").strip()
        if choice == "1":
            refresh_tool()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print(f"{RED}Unknown option.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting.")
