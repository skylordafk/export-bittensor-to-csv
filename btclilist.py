import subprocess
import csv

output = subprocess.check_output(['btcli', 'subnet', 'list']).decode('utf-8')

lines = output.strip().split('\n')
header = [h.strip() for h in lines[0].split()]
data = [line.split() for line in lines[1:]]

with open('subnet_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(data)