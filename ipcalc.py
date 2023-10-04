# ipcalc.py is Subnet Calculator for IPV4
'''  
Description:

ipcalc.py is a is Subnet Calculator for IPV4 that allows users to input one or more IP subnets in CIDR notation and calculates and prints all the included IP addresses within each subnet. It also provides the total number of IP addresses in each subnet.

How-to Guide:

    Running the Script:

    To use ipcalc.py, follow these steps:
        Ensure you have Python installed on your system.
        Download or create the ipcalc.py script.
        Open your terminal or command prompt and navigate to the directory where ipcalc.py is located.

    Executing the Script:

        Run the script by entering the following command:

        python ipcalc.py

    Entering Subnets:
        The script will prompt you to enter one or more subnets. Subnets should be in CIDR notation (e.g., 10.0.0.0/21).
        You can enter multiple subnets separated by commas (,) without spaces (e.g., 10.0.0.0/21,192.168.0.0/16).
        To exit the script, type 'exit' and press Enter.

    Viewing Results:
        The script will display the IP addresses within each subnet.
        It will also show the total number of IP addresses in each subnet.

Credit:

    This script was created by x.com/MohamedNab1l
    https://github.com/bigb0x/ipcalc/
''' 
import ipaddress

def print_ips_in_subnet(subnet_str):
    try:
        subnet = ipaddress.ip_network(subnet_str, strict=False)
        print(f"Total IPs in {subnet}:")
        print(f"Total number of IPs in {subnet}: {subnet.num_addresses}")
        for ip in subnet:
            print(ip)
    except ValueError:
        print(f"Invalid subnet format: {subnet_str}")

def main():
    while True:
        subnet_input = input("Enter one or more subnets separated by commas (e.g., 10.0.0.0/21,192.168.0.0/16) or 'exit' to quit: ")
        if subnet_input.lower() == 'exit':
            break
        subnets = subnet_input.split(',')
        for subnet in subnets:
            subnet = subnet.strip()  # Remove leading/trailing whitespace
            print_ips_in_subnet(subnet)

if __name__ == "__main__":
    main()
