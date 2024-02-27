import socket
import time
import threading
from queue import Queue

socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()


def scan(target, ports):
    try:
        t_IP = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid host.")
        return

    print("Starting scan on host:", t_IP)

    def portscan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect((t_IP, port))
            with print_lock:
                if port in range(0, 1024): #well-known ports
                    print(f"Port {port} ({socket.getservbyport(port)}) is open")
                else:
                    print(f"Port {port}  is open")
            con.close()
        except:
            pass

    def threader():
        while True:
            worker = q.get()
            portscan(worker)
            q.task_done()

    q = Queue()
    startTime = time.time()

    for x in range(100):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    for worker in ports:
        q.put(worker)

    q.join()
    print('Time taken:', time.time() - startTime)

def main():
    target_type = input("Enter '1' for single host or '2' for network: ")

    if target_type == '1':
        target = input('Enter the host to be scanned (e.g., localhost): ')
        ports_range = input('Enter the range of ports to be scanned (e.g., 1-100): ')
        start_port, end_port = map(int, ports_range.split('-'))
        ports = range(start_port, end_port + 1)
        scan(target, ports)
    elif target_type == '2':
        net = input("Enter the IP address of the network (e.g., 192.168.0.0): ")
        net_split = net.split('.')
        network = '.'.join(net_split[:-1]) + '.'
        start_range = int(input("Enter the starting range (e.g., 1): "))
        end_range = int(input("Enter the ending range (e.g., 254): "))
        ports_range = input('Enter the range of ports to be scanned (e.g., 1-100): ')
        start_port, end_port = map(int, ports_range.split('-'))
        ports = range(start_port, end_port + 1)
        for i in range(start_range, end_range + 1):
            target = network + str(i)
            scan(target, ports)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

#Source of inspiration: https://medium.com/@ibo1916a/network-scanner-python-eb22e4ce75d4