import platform
import os
import psutil
import argparse
from datetime import datetime
from tabulate import tabulate

def get_basic_os_info():
    return {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Architecture": platform.architecture(),
        "OS Uptime": str(datetime.now() - datetime.fromtimestamp(psutil.boot_time()))
    }

def get_cpu_info():
    return {
        "Physical Cores": psutil.cpu_count(logical=False),
        "Total Cores": psutil.cpu_count(logical=True),
        "Max Frequency (MHz)": psutil.cpu_freq().max,
        "Min Frequency (MHz)": psutil.cpu_freq().min,
        "Current Frequency (MHz)": psutil.cpu_freq().current,
        "CPU Usage Per Core (%)": psutil.cpu_percent(percpu=True, interval=1),
        "Total CPU Usage (%)": psutil.cpu_percent(interval=1),
        "Load Average": os.getloadavg()
    }

def get_memory_info():
    svmem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return {
        "Total Memory (GB)": svmem.total / (1024 ** 3),
        "Available Memory (GB)": svmem.available / (1024 ** 3),
        "Used Memory (GB)": svmem.used / (1024 ** 3),
        "Percentage Used (%)": svmem.percent,
        "Total Swap (GB)": swap.total / (1024 ** 3),
        "Free Swap (GB)": swap.free / (1024 ** 3),
        "Used Swap (GB)": swap.used / (1024 ** 3),
        "Swap Percentage Used (%)": swap.percent
    }

def get_disk_info():
    partitions = psutil.disk_partitions()
    disk_usage = {part.mountpoint: psutil.disk_usage(part.mountpoint)._asdict() for part in partitions}
    return disk_usage

def get_network_info():
    net_io = psutil.net_io_counters()
    return {
        "Bytes Sent (MB)": net_io.bytes_sent / (1024 ** 2),
        "Bytes Received (MB)": net_io.bytes_recv / (1024 ** 2),
        "Packets Sent": net_io.packets_sent,
        "Packets Received": net_io.packets_recv,
        "Error In": net_io.errin,
        "Error Out": net_io.errout,
        "Drop In": net_io.dropin,
        "Drop Out": net_io.dropout
    }

def display_info(title, info):
    print(f"\n{title}")
    print(tabulate(info.items(), headers=["Key", "Value"], tablefmt="grid"))

def main():
    parser = argparse.ArgumentParser(description="Display comprehensive information about the operating system.")
    parser.add_argument("--basic", action="store_true", help="Display basic OS information")
    parser.add_argument("--cpu", action="store_true", help="Display CPU information")
    parser.add_argument("--memory", action="store_true", help="Display memory information")
    parser.add_argument("--disk", action="store_true", help="Display disk information")
    parser.add_argument("--network", action="store_true", help="Display network information")
    parser.add_argument("--all", action="store_true", help="Display all information")

    args = parser.parse_args()

    if args.basic or args.all:
        display_info("Basic OS Information", get_basic_os_info())
    if args.cpu or args.all:
        display_info("CPU Information", get_cpu_info())
    if args.memory or args.all:
        display_info("Memory Information", get_memory_info())
    if args.disk or args.all:
        display_info("Disk Information", get_disk_info())
    if args.network or args.all:
        display_info("Network Information", get_network_info())

if __name__ == "__main__":
    main()
