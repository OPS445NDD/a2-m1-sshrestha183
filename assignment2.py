#!/usr/bin/env python3

'''
OPS445 Assignment 2 - Summer2026
Program: assignment2.py
Author: "Sanjib Shrestha"
The python code in this file is original work written by
"Sanjib Shrestha". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Description: Milestone 1 submission. This script reads the system's overall
             memory information from /proc/meminfo and visualizes the total
             memory in use with a scaled text-based bar graph.

Date: July 17, 2026
'''

import sys
import os

def percent_to_graph(percent: float, length: int=20) -> str:
    """Converts a float percentage (0.0 to 1.0) into a bar graph of hashes and spaces."""
    num_hashes = int(round(percent * length))
    num_spaces = length - num_hashes
    return '#' * num_hashes + ' ' * num_spaces

def get_sys_mem() -> int:
    """Returns the total system memory in kB from /proc/meminfo."""
    with open('/proc/meminfo', 'r') as f:
        for line in f:
            if line.startswith('MemTotal:'):
                return int(line.split()[1])
    return 0

def get_avail_mem() -> int:
    """Returns the total available system memory in kB from /proc/meminfo."""
    mem_free = 0
    swap_free = 0
    with open('/proc/meminfo', 'r') as f:
        for line in f:
            if line.startswith('MemAvailable:'):
                return int(line.split()[1])
            elif line.startswith('MemFree:'):
                mem_free = int(line.split()[1])
            elif line.startswith('SwapFree:'):
                swap_free = int(line.split()[1])
                
    # Fallback formula for environments without MemAvailable (like WSL)
    return mem_free + swap_free

# --- Milestone 2 Placeholders ---

def parse_command_args() -> object:
    """Placeholder for command line argument parsing (Milestone 2)."""
    pass

def pids_of_prog(app_name: str) -> list:
    """Placeholder for getting program PIDs (Milestone 2)."""
    pass

def rss_mem_of_pid(proc_id: str) -> int:
    """Placeholder for calculating PID resident memory (Milestone 2)."""
    pass

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    """Placeholder for converting bytes to human readable string (Milestone 2)."""
    pass

# --- Main Execution for Milestone 1 ---

if __name__ == "__main__":
    # Fetch system memory metrics
    total_mem = get_sys_mem()
    avail_mem = get_avail_mem()
    used_mem = total_mem - avail_mem
    
    # Calculate usage percentage
    if total_mem > 0:
        percent = used_mem / total_mem
    else:
        percent = 0.0
        
    # Generate and print the visual report
    graph = percent_to_graph(percent, length=20)
    print(f"Memory [{graph} | {int(round(percent * 100))}%] {used_mem}/{total_mem}")
