#!/usr/bin/env python3

import os
import re
import ipaddress
from rich.console import Console
from rich.table import Table

def parse_gnmap_files():
    hosts_data = {}
    gnmap_files = [f for f in os.listdir(".") if f.endswith(".gnmap")]

    for filename in gnmap_files:
        with open(filename, "r") as f:
            for line in f:
                if line.startswith("Host:") and "Ports:" in line:
                    parts = line.split()
                    ip = parts[1]
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
                                hosts_data[ip] = set()
                            hosts_data[ip].add((portid, service if service else "unknown"))
    return hosts_data


def print_table(hosts_data):
    console = Console()
    table = Table(header_style="bold magenta", show_lines=True)

    table.add_column("HOST", style="cyan", no_wrap=True)
    table.add_column("PORTS", style="green")
    table.add_column("SERVICES", style="yellow")

    for host, entries in sorted(hosts_data.items(), key=lambda x: ipaddress.ip_address(x[0])):
        entries_sorted = sorted(entries, key=lambda x: int(x[0]))
        ports_str = "\n".join(p for p, _ in entries_sorted)
        services_str = "\n".join(s for _, s in entries_sorted)
        table.add_row(host, ports_str, services_str)

    console.print(table)


if __name__ == "__main__":
    hosts = parse_gnmap_files()
    if hosts:
        print_table(hosts)
