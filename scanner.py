import socket
import ipaddress
import time

target = input("Enter The Target IP: ")

try:
    check_ip = ipaddress.ip_address(target)
except ValueError:
    print("Invalid IP address.")
    exit()

start = int(input("Enter Start Port: "))
end = int(input("Enter End Port: "))
count = 0

if start < 1 or end > 65535:
    print("Ports must be between 1 and 65535")
    exit()

if start > end:
    print("Start Port must be less than End Port")
    exit()

print(f"\nScanning Target: {target}\n")
    
start_time = time.time()

socket.setdefaulttimeout(0.2)
for port in range(start, end + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = s.connect_ex((target, port))

    if result == 0:
        try:
            service = socket.getservbyport(port, 'tcp')
        except OSError:
            service = "Unknown Service"
        print(f"[OPEN] Port {port} -> {service}")
        count += 1

    s.close()

end_time = time.time()
print(f"\nScanning Completed in {end_time - start_time:.2f} seconds.")
print(f"Total Open Ports Found: {count}")
input("Press Enter to Exit...")