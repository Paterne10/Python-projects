import socket
import sys
import subprocess
from datetime import datetime
import random

# print(random.choice())

subprocess.call('clear', shell=True)

server_ip_address = input('Enter the server ip: ')

time_start = datetime.now()

for x in range(1, 1025):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        response = s.connect_ex((server_ip_address, x)) 
        if response == 0:
            print('Port {} is open.'.format(x))
        s.close()
    except KeyboardInterrupt as interrupt:
        print('The program was interrupted.')
        sys.exit()
    except socket.error:
        print('The connection with the server is impossible.')
time_end = datetime.now()

total_time = time_end - time_start
print('Total time scan: ', total_time)

