"""
* psutil library is a cross-platform library for retrieving
* information on running processes and system utilization
"""
import psutil
from datetime import datetime
# Resources' threshold may be changed to any prefered values
CPU_THRESHOLD = 85
DISK_THRESHOLD = 80
MEMORY_THRESHOLD = 90
log_file = "D:\\monitor\\pc_resources_monitor\\pc_resource_log.txt"

cpu_usage = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory()
# To choose or change which disk you want to track its usage, modify psutil.disk_usage('<disk here>\')
disk_usage = psutil.disk_usage('C:\\')

def check_system_resource(resource_usage, resource_threshold, resource_name):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if resource_usage > resource_threshold:
        return(f"[{current_time}] Warning: {resource_name} usage is above {resource_threshold}%")
    else:
        return(f"[{current_time}] {resource_name} usage is within acceptable limits.")

disk_status = check_system_resource(disk_usage.percent, DISK_THRESHOLD, "Disk")
cpu_status =   check_system_resource(cpu_usage, CPU_THRESHOLD, "CPU")
memory_status = check_system_resource(memory_info.percent, MEMORY_THRESHOLD, "Memory")

with open(log_file, "a") as log:
    log.write(f"{disk_status}\n{cpu_status}\n{memory_status}\n")

print(disk_status)
print(cpu_status)
print(memory_status)