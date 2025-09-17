#!/usr/bin/env python3

import os
import re
from rich.console import Console
from rich.table import Table

def parse_gnmap(filename):
    hosts_data = {}
    with open(filename, "r") as f:
        for line in f:
            if line.startswith("Host:"):
                parts = line.split()
                ip = parts[1]
                if "Ports:" not in line:
                    continue
                ports_part = line.split("Ports:")[1].strip()
                ports = ports_part.split(",")
                for port in ports:
                    port = port.strip()
                    if not port:
                        continue
                    m = re.match(r"(\d+)/open/(\w+)//([^/]*)///?", port)
                    if m:
                        portid, proto, service = m.groups()
                        if ip not in hosts_data:
                            hosts_data[ip] = []
                        hosts_data[ip].append((portid, proto, service))
    return hosts_data


def print_table(hosts_data, filename):
    console = Console()
    table = Table(header_style="bold magenta", show_lines=True, caption=f"{filename}", caption_style="dim")

    table.add_column("HOST", style="cyan", no_wrap=True)
    table.add_column("PORTS", style="green")
    table.add_column("SERVICES", style="yellow")

    for host, ports in hosts_data.items():
        ports_sorted = sorted(ports, key=lambda x: int(x[0]))
        ports_str = "\n".join(f"{p}" for p, _, _ in ports_sorted)  # only numbers
        services_str = "\n".join(s if s else "unknown" for _, _, s in ports_sorted)
        table.add_row(host, ports_str, services_str)

    console.print(table)


if __name__ == "__main__":
    gnmap_files = [f for f in os.listdir(".") if f.endswith(".gnmap")]
    for gnmap in gnmap_files:
        hosts = parse_gnmap(gnmap)
        if hosts:
            print_table(hosts, gnmap)
