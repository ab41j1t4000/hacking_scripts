ARP-Poisoning Script
Author: Abhijith P Kumar

This is a simple script demonstrating the ARP cache poisoning.

Before using the script make sure you have necessary packages by running the following command:
	pip install -r requirements.txt

Make sure IP forwarding is enabled on your computer which is executing this script.
Command for Linux Users: echo 1 > /proc/sys/net/ipv4/ip_forward

For Windows Users:
Go to the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters.
Create a new REG_DWORD value named IPEnableRouter. 
Set IPEnableRouter to 1 and reboot.

After executing the script you may disable IP forwarding.
