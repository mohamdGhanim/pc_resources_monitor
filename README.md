# pc_resources_monitor
A simple python script that monitors you CPU, RAM and Disk usage; gives you warnings when the specified usage limits are exceeded. It is built to learn the fundamentals of system monitoring. And to improve it to become mature enough for my personal use.

## Features
- Gives out the usage percentage of the disk, memory and CPU.
- Test the percentage of each status against specified threshold.
- If the percentage exceeds the threshold it prints out a warning message.
- The output is saved into a log file. It will be created in the first use and then the output will continue to be appended in the same file.

## Requirements
- Python 3 or above installed
- psutil library installed

## Installation
- Install python 3 or above
- Install psutil using the command ```pip install psutil```
- To test it run the code using the command ```python pc_resource_monitor.py``` in the terminal and you will get the output immediately
## How to create the resourses monitor routine

The script runs once and exits, so it's designed to be triggered on a schedule by the operating system rather than looping internally. Replace the bracketed paths with your own. To find your python path execute the command ```where python```

### Windows (Task Scheduler)

Run in **Command Prompt** (not PowerShell, due to quote escaping). Uses `pythonw.exe` so it runs silently with no console window:

```
schtasks /create /tn "System Resource Monitor" /tr "\"[PATH_TO_pythonw.exe]\" \"[PATH_TO_SCRIPT]\"" /sc minute /mo 30
```
- In the ```/mo 30``` you can change the interval between calls. Here I set it to every 30 minutes.
You can manage the task by executing the commands:

```
schtasks /query  /tn "System Resource Monitor" /v /fo list   :: view status
schtasks /change /tn "System Resource Monitor" /disable      :: pause
schtasks /change /tn "System Resource Monitor" /enable       :: resume
schtasks /delete /tn "System Resource Monitor" /f            :: remove
```

> **Note:** Schedulers run the script from a minimal environment, not the project
> folder, so the log path in the script is set as an absolute path to ensure the
> log is always written to the same location regardless of where the script is launched.

