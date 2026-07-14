import sys
import subprocess
from colorama import Fore, Style, init
from pyfiglet import Figlet

init(autoreset=True)

f = Figlet(font="slant")
print(Fore.GREEN + f.renderText("Reconductor"))
print(Fore.GREEN + "Offensive Reconnaissance Toolkit")

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <target-ip>")
    sys.exit(1)

if len(sys.argv) > 2:
    print(f"Error: {sys.argv[0]} too many arguments")
    sys.exit(1)

target = sys.argv[1]
print(f"Received the target: {target}")

print("\nThese are the two scan profiles")
print("[1] Full TCP scan (All Ports)")
print("[2] Detailed scan on specific ports (Version + default scripts)")
print("[3] Full 1000 UDP ports scan")

choice = input("Choose a profile: ")

if choice == "1":
    print("Running full TCP scan...")
    subprocess.run([
        "nmap", "-T4", "--min-rate=5000", "--max-retries=1",
        "-p-", target, "-oN", "nmap_tcp_full.txt"
    ])

elif choice == "2":
    ports = input("Enter ports to scan (e.g. 80,443,22): ")
    print(f"Running detailed scan on ports {ports}...")
    subprocess.run([
        "nmap", "-T4", "-sC", "-sV", "-p", ports,
        target, "-oA", "nmap_service"
    ])

elif choice == "3":
    print("Running UDP scan...")
    subprocess.run(["nmap", "-sUV", "-vv", "--reason", "--version-intensity", 
                    "0", "--min-rate", "1300", "--max-retries", "1", "--top-ports", "1000", target, "-Pn"])

else:
    print("You have chosen an invalid profile")

