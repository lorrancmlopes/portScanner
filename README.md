# Port Scanner

This Python script is a simple port scanner that allows scanning either a single host or a range of hosts within a network for open ports. It utilizes multithreading to improve efficiency and can scan a range of ports for each target.

## Usage

1. **Single Host Scan:**
    - Enter `1` when prompted for the type of target.
    - Enter the host to be scanned when prompted.
    - Specify the range of ports to be scanned in the format `start_port-end_port` when prompted.
    - The script will then scan the specified host for open ports within the specified range.

2. **Network Scan:**
    - Enter `2` when prompted for the type of target.
    - Enter the IP address of the network (e.g., `192.168.0.0`) when prompted.
    - Specify the starting and ending range of IP addresses to be scanned within the network.
    - Specify the range of ports to be scanned in the format `start_port-end_port`.
    - The script will then scan each IP address within the specified range of the network for open ports within the specified port range.

## Requirements

- Python 3.x
- `socket` library (built-in)
- `time` library (built-in)
- `threading` library (built-in)
- `queue` module (built-in)

## How It Works

1. The script defines a `scan()` function which takes a target (host or network) and a range of ports to scan.
2. It utilizes threading to concurrently scan multiple ports for a given target.
3. For each port in the specified range, the script attempts to establish a connection.
4. If the connection is successful, it prints that the port is open.
5. The main function `main()` takes user input to determine whether to scan a single host or a network of hosts, and then initiates the scanning process accordingly.

## Notes

- This script utilizes threading to improve the speed of port scanning. However, depending on the network and system resources, scanning too many ports or hosts simultaneously may lead to performance issues or network congestion.
- This script is for educational purposes. 