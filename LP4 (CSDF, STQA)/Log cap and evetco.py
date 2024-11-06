import re
import time

log_patterns = [
    (r'Error', 'Error detected'),
    (r'Warning', 'Warning detected'),
    (r'Success', 'Successful operation')
]
event_correlations = {}

def process_log(log_line):
    for pattern, action in log_patterns:
        if re.search(pattern, log_line):
            event_correlations.setdefault(action, []).append(log_line)
            return True
    return False

with open('log_2.txt', 'r') as log_file:
    for log_line in log_file:
        log_line = log_line.strip()
        if log_line and process_log(log_line):
            print(f"Event Correlated: {log_line}")

time.sleep(5)
for action, logs in event_correlations.items():
    print(f"Action: {action}\nCorrelated Logs:")
    print('\n'.join(logs), '\n')
