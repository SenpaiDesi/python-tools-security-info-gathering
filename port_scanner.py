
import subprocess
import sys
from datetime import date, datetime
from socket import *

#Clear screen
subprocess.call('cls', shell=True)

#Ask for inpute
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = gethostbyname(remoteServer)

# Fancy shit
print("-" *  100)
print(f"Scanning.... Please do not close or stop the proccess\n")
print("-" * 100)

# time and information
current_time = datetime.now()


# Defining ports using range()
# Error handeling included

try:
    for port in range(1, 1025):
        sock = socket(AF_INET, SOCK_STREAM)
        results = sock.connect_ex((remoteServerIP, port))
        print("Scanning port {}".format(port))
        if results == 0:
            print(" Port {} open!\n".format(port))
        else:
            print("Port {} is closed \n".format(port))
        sock.close()

except KeyboardInterrupt:
    print("-" * 100)
    print("Close signal detected. Closed all pending tasks.")
    print("-" * 100)
    sys.exit()

except gaierror:
    print("-" * 100)
    print(f"ERROR. host name  not be  resolved  {remoteServer}. Exiting")
    print("-" * 100)
    sys.exit()

except error:
    print("-" * 100)
    print("ERROR: Could not connect to the server.")
    print("-" * 100)

#check time again
current_time_two = datetime.now()

# Calculate elapsed time
elapsed_time = current_time_two - current_time

# Print result to the screen
print("-" * 100)
print("FINISHED IN :", elapsed_time)
print("-" * 100)



