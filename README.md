# pc_resources_monitor
A simple python script that monitors you CPU, RAM and Disk usage; gives you warnings when the specified usage limits are exceeded. It is built to learn the fundamentals of system monitoring. And to improve it to become mature enough for my personal use.

## Features
- Gives out the usage percentage of the disk, memory and CPU.
- Test the percentage of each status against specified threshold.
- If the percentage exceeds the threshold it prints out a warning message.

## Requirements
- Python 3 or above installed
- psutil library installed

## Installation and usage
- Install python 3 or above
- Install psutil using the command ```pip install psutil```
- Run the code using the command ```python pc_resource_monitor.py``` in the terminal and you will get the output immediately

## Example output
```[2026-06-26 22:28:38] Warning: Disk usage is above 80%```

```[2026-06-26 22:28:38] CPU usage is within acceptable limits.```

```[2026-06-26 22:28:38] Memory usage is within acceptable limits.```
