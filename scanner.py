import socket

target = input("Enter The Target IP: ")

start = int(input("Enter Start Port: "))
end = int(input("Enter End Port: "))

print(f"\nScanning Target: {target}\n")

for port in range(start, end + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.2)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")

    s.close()

print("\nScanning Completed.")
input("Press Enter to Exit...")