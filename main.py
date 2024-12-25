#!/usr/bin/env python3
import psutil

cpu_usage = psutil.cpu_percent(interval=1)
print(f'CPU usage: {cpu_usage}%')

memory_info = psutil.virtual_memory()
memory_usage = memory_info.percent
print(f'Memory usage: {memory_usage}%')