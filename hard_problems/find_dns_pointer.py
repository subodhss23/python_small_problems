''' Write a function that takes an IP address and returns the domain name using PTR
    DNS records.'''

import socket

def get_domain(ip_address):
    dest = socket.gethostbyaddr(ip_address)
    return dest[0]

print(get_domain("8.8.8.8"))
print(get_domain("8.8.4.4"))